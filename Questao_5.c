#include <stdio.h>
#include <string.h>

void inverter(char str[]) {
    int tamanho = strlen(str);
    int i;
    int j;
    char temp;

    for (i = 0, j = tamanho - 1; i < j; ++i, --j) {
        temp = str[i];
        str[i] = str[j];
        str[j] = temp;
    }
}

int main() {
    char string[100];

    printf("Digite uma string para inverter: ");
    fgets(string, sizeof(string), stdin);

    string[strcspn(string, "\n")] = '\0';

    inverter(string);

    printf("String invertida: %s\n", string);

    return 0;
}
