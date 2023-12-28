# Main Makefile

MAKEFLAGS += --no-print-directory

PROJ = effective-c
CPU = X86_64
C = ${CC} ${CPPFLAGS} -m64 -Wpointer-arith -Wall -Wextra -Wno-implicit-fallthrough -Werror -O2 ${CFLAGS}

MKDIR = mkdir -p

SRC = main.c alloc.c io.c
OBJ = $(patsubst %.c,%.o,$(SRC))

.PHONY: build
build: $(PROJ)
	@echo "Done :)"

# executable
$(PROJ): $(OBJ)
	$(C) -D$(CPU) -o $@ $^

# c source
%.o: %.c
	$(C) -c -D$(CPU) -o $@ $<

.PHONY: clean
clean:
	rm -f $(PROJ) *.o
