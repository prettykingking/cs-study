# Main Makefile

PROJ_NAME=effective-c

PROJ_CC=$(CC)
PROJ_LD=$(LD)

PROJ_OBJ=main.o widget.o
ALL_SOURCES=$(sort $(patsubst %.o,%.c,$(PROJ_OBJ)))

all: $(PROJ_NAME)
	@echo ""
	@echo "Hint: It's a good idea to run 'make test' ;)"
	@echo ""

$(PROJ_NAME): $(ALL_SOURCES)
	$(PROJ_CC) -o $@ $^
