/* Problem 4: Primaen
lest einen Wert ein und berechnet alle Primaen, bis zu dieser a
Berechnung der Primaen muss manuell erfolgen */

#include <stdio.h>

int main(){
    int num;
    printf("Insert a natural number: ");
    scanf("%d", &num);
    printf("\n");
    int a = 2;
    int prim_array[num];
    int nonprim_array[num];

    for (int prim = 2; prim <= num; prim++){
        for (int a = 2; a <= num ; a++){
            if (prim / a != 1){
                if (prim % a == 0){
                    nonprim_array[a] = prim;
                }
            }
            else{
                if (prim != nonprim_array[a]){
                    prim_array[a] = prim;
                    printf("%d \n", prim);
                }
            }
        }

    }
    //printf("%d \n",prim_array);
}