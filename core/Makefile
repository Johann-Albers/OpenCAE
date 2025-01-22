CC = gcc
CFLAGS = -Wall -g -fPIC
LDFLAGS = -shared

TEST_CFLAGS = -Wall -g

SRC_DIR = src
INC_DIR = src
LIB_DIR = lib
OBJ_DIR = lib
ABS_LIB_DIR = $(shell realpath $(LIB_DIR))
TEST_DIR = test
TEST_OBJ_DIR = bin

LIB = $(LIB_DIR)/libopencae.so
SRC = $(shell find $(SRC_DIR) -name "*.c")
OBJ = $(patsubst %.c,$(OBJ_DIR)/%.o,$(notdir $(SRC)))
TEST_SRC = $(shell find $(TEST_DIR) -name "*.c")
TEST_OBJ = $(patsubst %.c,$(TEST_OBJ_DIR)/%.out,$(notdir $(TEST_SRC)))

all: $(LIB)

$(LIB): $(OBJ)
	$(CC) $(LDFLAGS) -o $@ $^

$(OBJ_DIR)/%.o:
	@mkdir -p $(dir $@)
	$(CC) $(CFLAGS) -I$(INC_DIR) -o $@ -c $(shell find $(SRC_DIR) -name "$(patsubst %.o,%.c,$(notdir $@))")

test: $(LIB) $(TEST_OBJ)

test_only: $(TEST_OBJ)

test_all: $(TEST_OBJ)
	@$(foreach file, $(TEST_OBJ), echo "[TEST] $(file)"; ./$(file);)

$(TEST_OBJ_DIR)/%.out:
	@mkdir -p $(dir $@)
	$(CC) $(TEST_CFLAGS) -I$(INC_DIR) -L$(LIB_DIR) -lopencae -Wl,-rpath,$(ABS_LIB_DIR) -o $@ $(shell find $(TEST_DIR) -name "$(patsubst %.out,%.c,$(notdir $@))")

clean:
	rm -rf $(LIB_DIR) $(TEST_OBJ_DIR)

.PHONY: all test test_only test_all clean
