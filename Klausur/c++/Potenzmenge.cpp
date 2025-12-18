using namespace std;                   // import everything from 'std' into current
#include <stdio.h>                     // Standard Input Output
#include <string.h>
int main (int argc, char* argv[]) {
  const int cardinality = 10;          // cardinality of the set
  const int elements = cardinality + 1;
  int control[elements];               // control vector
  char delimiter[3];                   // character string to be output between the data elements

  for (int i = 0; i < elements; control[i++] = 0); // initialize control vector
  while (control[0] == 0) {            // end of processing upon transfer to MSB
    printf ("{");                      // beginning of the set elements
    strcpy (delimiter, "");            // first elements without preceding characters
    for (int i = 1; i <= cardinality; i++) // analyze control vector
      if (control[i]) {                // Should the element be included in the result set?
        printf ("%s%d", delimiter, i - 1);
        strcpy (delimiter, ", ");
      }
    printf ("}\n");                    // end of set elements
    for (int i = elements; control[--i]++; control[i] = 0); // one addition
  }
  return 0;
}