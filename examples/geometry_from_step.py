#!/usr/bin/env python3

from opencae import geometry

if __name__ == "__main__":
    g = geometry.from_step("raw/io1-ac-214.stp")
    print(g.path)
