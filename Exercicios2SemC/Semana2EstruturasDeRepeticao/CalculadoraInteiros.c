//Exercicio de calciuladora
#include <stdio.h>

int main() {
    int x, y;

    printf("Digite um número inteiro:");
    scanf("%d", &x);
    printf("Digite um número inteiro novamente:");
    scanf("%d", &y);

    int soma, sub, mult, div;

    soma = x + y;
    sub = x - y;
    mult = x * y;
    div = x / y;

    printf("Soma: %d\nSubtração: %d\nMultiplicação: %d\nDivisão inteira: %d", soma, sub, mult, div);
    return 0;
}