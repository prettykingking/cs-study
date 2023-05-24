#include "add.h"
#include <iostream>


int main() {
    const char* name = "abc";
    ++name;
    std::cout << *name << '\n';

    char buf[10];
    std::cin.getline(buf, 10);
    std::cout << buf << '\n';

    int ages [2]{};
    const int res = add(1, ages[0]);

    std::cout << res << '\n';

    return 0;
}
