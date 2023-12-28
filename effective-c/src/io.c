/*
 * Input/Output
 */

#include <stdio.h>
#include <wchar.h>

void print_to_stdout(char *txt) {
    if (fputs(txt, stdout) == EOF) {
        printf("failed to print \"%s\" to stdout", txt);
    }
}

void setting_file_position() {
    FILE *doc = fopen("README.adoc", "r");
    if (doc == NULL) {
        fputs("Can not open README.adoc\n", stderr);
        return;
    }

    long pos = ftell(doc);
    printf("initial position: %ld\n", pos);
    wint_t c = fgetwc(doc);
    printf("character at position %c\n", c);

    if (fseek(doc, 5, SEEK_SET) != 0) {
        fputs("Can not seek position at 5", stderr);
    }

    pos = ftell(doc);
    printf("position after seek: %ld\n", pos);

    c = fgetwc(doc);
    printf("get character at position %c\n", c);

    pos = ftell(doc);
    printf("position after seek: %ld\n", pos);

    if (fclose(doc) == EOF) {
        fputs("Can not close README.adoc properly", stderr);
        return;
    }
}
