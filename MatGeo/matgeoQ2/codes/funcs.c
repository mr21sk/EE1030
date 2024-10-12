#include <stdio.h>
#include <math.h>

void calculate_unit_vector(double *vector, double *unit_vector, int size) {
    double magnitude = 0.0;
    for (int i = 0; i < size; i++) {
        magnitude += vector[i] * vector[i];
    }
    magnitude = sqrt(magnitude);
    if (magnitude == 0) {
        return; 
    }
    for (int i = 0; i < size; i++) {
        unit_vector[i] = vector[i] / magnitude;
    }
}

