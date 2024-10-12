#include <stdio.h>
#include <math.h>

int main() {
    FILE *file = fopen("ellipse_points.txt", "w");
    if (file == NULL) {
        fprintf(stderr, "Error opening file.\n");
        return 1;
    }

    double A = 2.0; 
    double B = 3.0; 
    int no_points = 1000;

    for (int i = 0; i < no_points; i++) {
        double t = 2 * M_PI * i / no_points;
        double x = A * cos(t);
        double y = B * sin(t);

        fprintf(file, "%lf, %lf\n", x, y);
    }

    fclose(file); 
    printf("Generated 1000 points on the ellipse and saved to ellipse_points.txt\n");

    return 0; 
}

