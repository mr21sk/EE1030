import ctypes

ellipse_lib = ctypes.CDLL('/home/krishna/git/EE1030/assign04/codes/area.so')

ellipse_lib.areaOfEllipse.argtypes = (ctypes.c_double, ctypes.c_double)
ellipse_lib.areaOfEllipse.restype = ctypes.c_double

semi_major_axis = 2.0
semi_minor_axis = 3.0
area = ellipse_lib.areaOfEllipse(semi_major_axis, semi_minor_axis)

print(f"The area of the ellipse is: {area:.2f}")

