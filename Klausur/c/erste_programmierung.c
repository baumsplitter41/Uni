#include <stdio.h>

int main() {
  int a = 5;
  printf("Bitte eine a eingeben:");
  scanf("%d",&a);
  int b = 7;
  if ( a<b ){
    printf("a ist kleiner b\n");
  }
  else{
    printf("b ist kleiner a \n");
  }
  int c = 0;
  scanf("%d",&c);
}