#include <stdio.h>

int falcutaet(int num) {
    if (num == 1) {
        return 1;
    } else {
        return falcutaet(num - 1) * num;
    }
}

int main() {
    int num;
    printf("Insert a Number: ");
    scanf("%d", &num);

    int solution = falcutaet(num);

    FILE *file = fopen("falcutaet_2.txt", "a");
    if (file != NULL) {
        fprintf(file, "faculaet of %d is %d \n", num, solution);
        fclose(file);
    }

    file = fopen("falcutaet_2.txt", "r");
    if (file != NULL) {
        char buffer[1024];
        while (fgets(buffer, sizeof(buffer), file)) {
            printf("%s", buffer);
        }
        fclose(file);
    }

    return 0;
}
