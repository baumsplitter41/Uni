#include <stdio.h>

int main() {

    int matrix[2][3] = { {1,2,3},{4,5,6} };
    int matrixt[3][2] = {{},{}};
    printf("Ausgangsmartrix:\n");


    int i, j;
    for (i = 0; i < 1; i++) {
        for (j = 0; j < 3; j++) {
            printf("%d", matrix[i][j]);
    }
    };
    printf("\n");
    for (i = 1; i < 2; i++) {
        for (j = 0; j < 3; j++) {
            printf("%d", matrix[i][j]);
    }
    printf("\n");

    //Transpnieren
    };

    for (i = 0; i <1; i++){
        for (j=0; j< 3; j++){
            matrixt[j][i] = matrix[i][j];
        }
    }
    for (i = 1; i <2; i++){
        for (j=0; j< 3; j++){
            matrixt[j][i] = matrix[i][j];
        }
    }

    //Print
    printf("Transponierte Matrix:\n");
    for (i = 0; i < 1; i++) {
        for (j = 0; j < 2; j++) {
            printf("%d", matrixt[i][j]);
    }
    };
    printf("\n");
    for (i = 1; i < 2; i++) {
        for (j = 0; j < 2; j++) {
            printf("%d", matrixt[i][j]);
    }
    }

    printf("\n");
    for (i = 2; i < 3; i++) {
        for (j = 0; j < 2; j++) {
            printf("%d", matrixt[i][j]);
    }

    }

}



