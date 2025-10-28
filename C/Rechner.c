#include <stdio.h>

int main() {

    char trigger = 'j';
    while (trigger == 'j')
    {
        int a;
        int b;
        char operation;
        printf("Gib die Rechnoperation ein (+,-,*,/): ");
        scanf(" %c", &operation);

        

        printf("Bitte eine Zahl eingeben: ");
        scanf("%d",&a);

        printf("Bitte eine zweite Zahl eingeben: ");
        scanf("%d", &b);

        if (operation == '+')
        {
            int sum = a + b;
            printf("Ergebnis: %d", sum);
        }
        else if (operation == '-')
        {
            int sum = a - b;
            printf("Ergebnis: %d", sum);
        }
        else if (operation == '*')
        {
            int sum = a * b;
            printf("Ergebnis: %d", sum);
        }
        else if (operation == '/')
        {
            float sum = a / b;
            printf("Ergebnis: %d", sum);
        }
        printf("\n");
        printf("Möchtest du eine weitere Berechnung durchführen? (j/n): ");
        scanf(" %c", &trigger);
    }



}