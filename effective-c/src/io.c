/*
 * Input/Output
 */

#include <stdio.h>
#include <stdlib.h>

void print_to_stdout(char *txt) {
    if (fputs(txt, stdout) == EOF) {
        printf("failed to print \"%s\" to stdout", txt);
    }
}
