#include <stdio.h>

int sequencia(int n) {

    int a = 0;
    int b = 1;
    int soma = 0;

    while (soma <= n) {
        if (soma == n) {
            return 1;
        }

        soma = a + b;
        a = b;
        b = soma;

    }
    return 0; 
}

int main() {
    int n;

    printf("Digite um numero para verificar se pertence a sequencia de Fibonacci: ");
    scanf("%d", &n);

    if (sequencia(n)) {
        printf("%d pertence a sequencia.\n", n);
    } else {
        printf("%d nao pertence a sequencia.\n", n);
    }

    return 0;
}
