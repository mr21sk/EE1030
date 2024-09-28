import ctypes
import numpy as np

# Load the shared library
vector_lib = ctypes.CDLL('./vector.so')

# Define the function argument and return types
vector_lib.calculate_unit_vector.argtypes = (ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double), ctypes.c_int)

def unit_vector(vector):
    size = len(vector)
    c_vector = (ctypes.c_double * size)(*vector)
    c_unit_vector = (ctypes.c_double * size)()

    vector_lib.calculate_unit_vector(c_vector, c_unit_vector, size)

    return [c_unit_vector[i] for i in range(size)]

def main():
    vector = [1.0, 1.0, 2.0]
    u_vector = unit_vector(vector)
    print("The unit vector is:", u_vector)

if __name__ == "__main__":
    main()

