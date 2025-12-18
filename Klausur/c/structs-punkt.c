#include <stdio.h>
#include <stdlib.h>

typedef struct point3D{
    char name;
    float x;
    float y;
    float z;
} point3D;

int main() {
    point3D *vp;
    vp = (point3D*) malloc(sizeof(point3D));



    point3D p ;
    vp->name = 'V';
    printf("Bitte x,y,z eingeben: \n");
    scanf("%f",&vp->x);
    scanf("%f",&vp->y);
    scanf("%f",&vp->z);

    printf("Die Koordinanten von %c sind (%f, %f, %f) ",vp->name,vp->x,vp->y,vp->z);



}