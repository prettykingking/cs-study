/* Effective C
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "widget.h"

int main(void) {
    len();

    flex_array(10);

    char *str = (char *) malloc(24);

    if (str == NULL) {
        return EXIT_FAILURE;
    }

    strncpy(str, "123456789abcdef", 9);
    str[18] = '\0';
    printf("str = %lu,%s\n", strlen(str), str);

    free(str);
    str = NULL;

    printf("size_t: %lu\n", sizeof(size_t));

    return EXIT_SUCCESS;
}
