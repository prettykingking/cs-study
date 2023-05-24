/* Widget implementation
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <wchar.h>

#include "widget.h"

void flex_array(const int array_size) {
    widget *wp = (widget *) malloc(sizeof(widget) + (sizeof(int) * array_size));

    if (wp == NULL) {
        return;
    }

    wp->num = array_size;
    for (size_t i = 0; i < wp->num; ++i) {
        wp->data[i] = 17;
    }

    printf("%d\n", wp->num);

    free(wp);
    wp = NULL;
}

int len() {
    char s1[] = "here comes the sun";
    printf("size: %lu, length: %lu\n", sizeof(s1), strlen(s1));

    char s2[100] = "\u20AChere comes the sun";
    printf("size: %lu, length: %lu\n", sizeof(s2), strlen(s2));

    wchar_t ws[100] = L"太阳出来了here comes the sun";
    printf("size: %lu, length: %lu\n", sizeof(ws), wcslen(ws));

    printf("%p\n", NULL);

    return 0;
}
