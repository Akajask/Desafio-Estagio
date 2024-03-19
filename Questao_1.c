#include <stdio.h>

int main()
{
    int indice = 13;
    int k;
    int soma = 0;

    for (k = 0; k < indice; k++){
      soma += k;
    }

    printf("%d", soma);
    return 0;
}
