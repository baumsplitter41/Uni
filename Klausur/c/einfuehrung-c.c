#include <stdio.h> // Einbinden der Standard-Ein-/Ausgabe-Bibliothek 
#include <stdlib.h> // Einbinden der Standard-Bibliothek für Speicherverwaltung
/*#include <string.h> // Einbinden der String-Bibliothek für Zeichenkettenoperationen
#include <stdbool.h> // Einbinden der Bibliothek für boolesche Datentypen
#include <math.h> // Einbinden der Mathematik-Bibliothek für mathematische Funktionen
#include <time.h> // Einbinden der Zeit-Bibliothek für Zeitfunktionen
#include <ctype.h> // Einbinden der Bibliothek für Zeichenklassifikation
#include <limits.h> // Einbinden der Bibliothek für Grenzwerte von Datentypen
#include <float.h> // Einbinden der Bibliothek für Grenzwerte von Gleitkommaaen
#include <errno.h> // Einbinden der Bibliothek für Fehlercodes
#include <assert.h> // Einbinden der Bibliothek für Assertions
#include <stddef.h> // Einbinden der Bibliothek für Standard-Definitions
#include <stdint.h> // Einbinden der Bibliothek für feste Breiten von Ganzaen
#include <inttypes.h> // Einbinden der Bibliothek für formatierte Ein-/Ausgabe von Ganzaen
#include <locale.h> // Einbinden der Bibliothek für Lokalisierung
#include <wchar.h> // Einbinden der Bibliothek für breite Zeichen
#include <wctype.h> // Einbinden der Bibliothek für breite Zeichenklassifikation
#include <stdarg.h> // Einbinden der Bibliothek für variable Argumentlisten
#include <tgmath.h> // Einbinden der Bibliothek für typgenerische Mathematik
#include <complex.h> // Einbinden der Bibliothek für komplexe aen
#include <fenv.h> // Einbinden der Bibliothek für Fließkomma-Umgebungen
#include <signal.h> // Einbinden der Bibliothek für Signalbehandlung
#include <setjmp.h> // Einbinden der Bibliothek für nicht-lokale Sprünge
#include <stddef.h> // Einbinden der Bibliothek für Standard-Definitions
#include <uchar.h> // Einbinden der Bibliothek für UTF-16 und UTF-32 Zeichen
// Dies sind die wichtigsten Standard-Bibliotheken in C17. Je nach Anwendungsfall können weitere Bibliotheken erforderlich sein.

https://www.learn-c.org/de  zum lernen von C

*/


// Beispiel einer Funktion in C
int foo(int bar) {
    /* do something */
    return bar * 2;
}


// Funktionsdeklaration print_big
int print_big(int number);


// Definition einer Struktur (Person) in C
struct person {
	char * name;
	int age;
};




// Hauptfunktion des Programms
int main() {
    printf("Dies ist ein Beispielprogramm\n");


    int a = 0, b = 1, c = 2, d = 3, e = 4;
    a = b - c + d * e;
    printf("%d\n", a); /* will print 1-2+3*4 = 11 */






  // Notendurchschnitt berechnen via Array
    int grades[3];
    int average;

    grades[0] = 80;
    grades[1] = 85;
    grades[2] = 90;

    average = (grades[0] + grades[1] + grades[2]) / 3;
    printf("The average of the 3 grades is: %d\n", average);


    int numbers[10]; // Deklaration eines Arrays mit 10 Ganzaen
    for (int i = 0; i < 10; i++) {
        numbers[i] = (i + 1) * 10; // Initialisierung des Arrays mit Vielfachen von 10
        printf("numbers[%d] = %d\n", i, numbers[i]); // Ausgabe der Werte im Array
    }




    // Berechnung der Fakultät von 10 via Array und for-Schleife
    int array[] = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };
    int factorial = 1;
    int i;

    for (i = 0; i < 10; factorial *= array[i++]);
    printf("10! is %d.\n", factorial);

    int n = 0;
    while (1) {
        n++;
        if (n == 10) {
            break;
        }
    }



    // Aufruf der Funktion print_big mit verschiedenen Werten
    int array2[] = { 1, 11, 2, 22, 3, 33 };
    int j;
    printf("Print Big Funktion\n");
    for (j = 0; j < sizeof(array2) / sizeof(array2[0]); j++) {
        print_big(array2[j]);
    }



    // Funktion Foo aufrufen
    foo(5);
    printf("%d Foo Funktion\n", foo(5));





    //pointer Beispiel
    int f = 1;
    int * pointer_to_f = &f; /* pointer_to_f speichert die Adresse von f */

    printf("Der Wert von f ist %d\n", f);
    printf("Der Wert von f ist auch %d\n", *pointer_to_f); /* dereferenzieren des Zeigers */

    /* lass uns die Variable f veraendern */
    f += 1;

    /* wir haben die Variable f gerade schon wieder veraendert! */
    *pointer_to_f += 1;

    /* wir werden 3 ausgeben */
    printf("Der Wert von f ist jetzt %d\n", f);


    // Struktur Beispiel 
    typedef struct {
    char * brand;
    int model;
    }   vehicle;

    vehicle mycar;
    mycar.brand = "Ford";
    mycar.model = 2007;

    printf("Mein Auto ist ein %s Modell %d\n", mycar.brand, mycar.model);




// Ende Hauptfunktion des Programms
    return 0;
} 



// Funktion, die prüft, ob eine a größer als 10 ist und eine Nachricht ausgibt
int print_big(int number) {
    if(number > 10){
        printf("%d ist groß\n", number);
    }
}
