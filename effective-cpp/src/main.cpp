
#include <iostream>

#include "add.h"

int main() {
    const char* name = "abc";
    std::cout << std::strlen(name) << '\n';

    ++name;
    ++name;
    ++name;
    if (*name == '\0') {
        std::cout << "bull char detected" << '\n';
    } else {
        std::cout << *name << '\n';
    }

    char buf[10];
    std::cin.getline(buf, 10);
    std::cout << buf << '\n';

    int ages [2]{};
    const int res = add(1, ages[0]);

    std::cout << res << '\n';

    return 0;
}
