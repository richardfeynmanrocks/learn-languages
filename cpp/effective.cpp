#include <iostream>

int main()
{
    int a = 0;
    auto a = 1;
    int& ab = a;
    const char* s = "Abc";
    const char*& c = s;
    std::cout << decltype(a) << " " << decltype((a));
}
