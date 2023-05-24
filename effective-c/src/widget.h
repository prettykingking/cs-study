/* Widget
 */

#ifndef EFFECTIVE_C_WIDGET_H
#define EFFECTIVE_C_WIDGET_H

typedef struct {
    int num;
    int data[];
} widget;

int len(void);
void flex_array(int array_size);

#endif /* EFFECTIVE_C_WIDGET_H */
