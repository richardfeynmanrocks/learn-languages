#include <stdio.h>
#include <unistd.h>
#include <errno.h>
#include <string.h>
#include <sys/mman.h>

// nabbed from stackoverflow, reveals problem may not be very interesting


int change_page_permissions_of_address(void *addr) {
    // Move the pointer to the page boundary
    int page_size = getpagesize();
    addr -= (unsigned long)addr % page_size;

    if(mprotect(addr, page_size, PROT_READ | PROT_WRITE | PROT_EXEC) == -1) {
        return -1;
    }

    return 0;
}

int foo() {
    int a = 1;
    return a;
}

int main()
{
     void *foo_addr = (void*)foo;

    // Change the permissions of the page that contains foo() to read, write, and execute
    // This assumes that foo() is fully contained by a single page
    if(change_page_permissions_of_address(foo_addr) == -1) {
        fprintf(stderr, "Error while changing page permissions of foo(): %s\n", strerror(errno));
        return 1;
    }

    // Call the unmodified foo()
    puts("Calling foo...");
    foo();

    // Change the immediate value in the addl instruction in foo() to 42
    unsigned char *instruction = (unsigned char*)foo_addr + 7;
    *instruction = 0x2A;

    // Call the modified foo()
    puts("Calling foo...");
    printf("%d\n", foo());

    return 0;
}
