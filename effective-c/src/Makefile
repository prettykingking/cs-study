# Main Makefile

PROJ_NAME = effective-c
BUILD_DIR = ../build

PROJ_CC = $(CC)
PROJ_LD = $(LD)
MKDIR = mkdir -p

SRC = $(shell ls *.c)
OBJ = $(patsubst %.c,$(BUILD_DIR)/%.o,$(SRC))

.PHONY: all

all: $(BUILD_DIR)/$(PROJ_NAME)
	@echo ""
	@echo "Hint: It's a good idea to run 'make test' ;)"
	@echo ""

$(BUILD_DIR)/$(PROJ_NAME): $(SRC)
	$(MKDIR) $(dir $@)
	$(PROJ_CC) -Wall -W -o $@ $^
