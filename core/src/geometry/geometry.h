#ifndef GEOMETRY_H
#define GEOMETRY_H

struct Geometry {
	const char* path;
};

int from_step(struct Geometry* g, const char* path);

#endif

