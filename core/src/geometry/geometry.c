#include "geometry.h"
#include <stdlib.h>

int from_step(struct Geometry* g, const char* path) {
	g->path = path;

	return EXIT_SUCCESS;
}
