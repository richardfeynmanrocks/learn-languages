#include <thread>
#include <mutex>
#include <iostream>
#include <vector>
#include <unistd.h>

std::mutex io;

void Sleep(int n)
{
    sleep(n/10);
    io.lock();
    std::cout << n << "\n";
    io.unlock();
}

void sleepsort(std::vector<int> l)
{
    std::vector<std::thread> t;
    for (int i : l) {
        t.emplace_back(&Sleep, i);
    }
    for (int i = 0; i < t.size(); i++) {
        t[i].join();
    }
}

#define MAXNUM 200
#define MAXSIZE 200
int main()
{
    std::vector<int> vec;
    int a = rand() % MAXSIZE + 1; //1 to 20
    for (int i =0; i < a; i++){
        int b = rand() % MAXNUM + 1;
        vec.push_back(b);
    }
    sleepsort(vec);
}
