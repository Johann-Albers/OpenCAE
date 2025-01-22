#include "geometry/geometry.h"
#include <assert.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

int main(void) {
	struct Geometry g = {};
	int ret = from_step(&g, "../../examples/raw/io1-ac-214.stp");

	assert(ret == 0);
	assert(strcmp(g.path, "../../examples/raw/io1-ac-214.stp") == 0);

	return EXIT_SUCCESS;
}
