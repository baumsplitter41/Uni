#include <stdio.h>

int main() {
    int x = 1;
    int y = 1;
    int lx[11];
    int ly[11];

    for (x = 1; x <= 10; x++) {
        for (y = 1; y <= 10; y++) {
            if (y != 0 && (x / y) == 1) {
                lx[x] = 1;
            } else {
                lx[x] = 0;
            }

            if (y != 0 && (x / y) == 1) {
                ly[y] = 1;
            } else {
                ly[y] = 0;
            }

        }
    }
    for (int i = 1; i <= 10; i++) {
        printf("%d Liste x \n", lx[i]);
    }
    for (int i = 1; i <= 10; i++) {
        printf("%d Liste y \n", ly[i]);
    }

    return 0;
}