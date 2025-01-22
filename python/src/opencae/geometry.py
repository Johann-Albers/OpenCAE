import ctypes
from ctypes import Structure, POINTER, c_int, c_char_p, byref
import os

libopencae = os.path.join(os.path.dirname(__file__), "../../../core/lib", "libopencae.so")
opencae = ctypes.CDLL(libopencae)

class Geometry(Structure):
    _fields_ = [
        ("_path", c_char_p),
    ]
    
    @property
    def path(self):
        if self._path:
            return self._path.decode("utf-8")
        return None

opencae.from_step.restype = c_int
opencae.from_step.argtypes = [POINTER(Geometry), c_char_p]

def from_step(path):
    geometry = Geometry()
    status = opencae.from_step(byref(geometry), path.encode("utf-8"))

    if status != 0:
        raise RuntimeError(f"from_step failed with error code {status}")

    return geometry
