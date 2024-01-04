/*
 * Input/Output
 */

#include <stdio.h>
#include <wchar.h>
#include <locale.h>
#include <errno.h>

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

    errno = 0;

    wint_t wc;
    while ((wc = fgetwc(doc)) != WEOF) {
        printf("%lc", wc);
    }

    if (fclose(doc) == EOF) {
        fputs("Can not close README.adoc properly", stderr);
        return;
    }
}

void read_and_put() {
    int retry = 3;
    int c;
    while (retry > 0) {
        c = getchar();
        if (c != '\n')
            printf("%x, %d\n", c, c);
        if (putc(c, stdout) == EOF)
            printf("output error");

        retry--;
    }
}
