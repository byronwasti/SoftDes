#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char Get_Compliment( char *nuc){
    switch( *nuc ){
        case 'A': return 'T';
        case 'T': return 'A';
        case 'G': return 'C';
        case 'C': return 'G';
    }
}

void Reverse(char * str)
{
  if (str)
  {
    char * end = str + strlen(str) - 1;

    // swap the values in the two given variables
    // XXX: fails when a and b refer to same memory location
#   define XOR_SWAP(a,b) do\
    {\
      a ^= b;\
      b ^= a;\
      a ^= b;\
    } while (0)

    // walk inwards from both ends of the string, 
    // swapping until we get to the middle
    while (str < end)
    {
      XOR_SWAP(*str, *end);
      str++;
      end--;
    }
#   undef XOR_SWAP
  }
}

int main ( int argc, char *argv[]){
    char nucl = 'A';
    char dna[] = "AGTCGTATAG";
    char *dna2 = (char*)calloc(sizeof(dna), 1);
    char *pdna = dna;
    Reverse(dna);
    printf("%c\n", Get_Compliment( &nucl ) );
    printf("%s\n", dna);

}
