#include <stdio.h>

int main() {
    unsigned char a = 5;
    unsigned char b = 0;


    // Using boolean expressions
    if (a && b){
        printf("a and b");
    }
    if (a || b){
        printf("a or b\n");
    }
    if (!b){
        printf("not b\n");
    }
    if (!a && !b){
        printf("not a and not b\n");
    }
    return 0;
}