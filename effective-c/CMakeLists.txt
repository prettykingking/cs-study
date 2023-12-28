cmake_minimum_required(VERSION 3.20)
project(effective-c)

set(CMAKE_C_STANDARD 99)

add_executable(effective-c src/main.c
        src/alloc.c
        src/io.c)
