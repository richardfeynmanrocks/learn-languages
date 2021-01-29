    .global main
    .text
main:
    pushq   %rbp
    movq    %rsp, %rbp
    movw    $4, %bx
    movb    $0x4B, %al
    movb    %al, -4(%rip)
    inc     %bx
    popq    %rbp
    retq
