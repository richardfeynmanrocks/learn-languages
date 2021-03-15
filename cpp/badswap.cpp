#include <iostream>
#include <thread>

static void assign(int& a, int& b)
{
    a = b;
}

void swap(int& a, int& b)
{
    int x, y;
    do {
	x = a;
	y = b;
	std::thread t1(assign, std::ref(x), std::ref(y));
	std::thread t2(assign, std::ref(y), std::ref(x));
	t1.join();
	t2.join();
    } while (x == a || x == y);
    a = x;
    b = y;
}

int main()
{
    int a = 1;
    int b = 2;
    swap(a, b);
    std::cout << "A: " << a << " B: " << b << "\n";
}
