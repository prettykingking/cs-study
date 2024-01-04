/* Effective C
 */

#include <stdlib.h>

#include "io.h"
#include "alloc.h"

int main(void) {
    // io functions
    print_to_stdout("Effective C\n");
    setting_file_position();
    read_and_put();

    // memory allocation
    print_memory_size();

    return EXIT_SUCCESS;
}
