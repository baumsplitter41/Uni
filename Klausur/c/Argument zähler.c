#include <stdio.h>

int main(int argc, char* argv[]){
    printf("el. Parameter gibt anzahl Komandozeilen");
    printf("in diesem Fall %d argumente.\n", argc);

    printf("Name des Programms ist %s\n", argv[0]);

    printf("Die weiteren Argumente sind:\n");
    for (int i = 1; i < argc; i++) {
        printf("Argument #%d %s \n", i, argv[i]);   
    }


}