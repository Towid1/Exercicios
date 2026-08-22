//Exercicio de calculadora de IMC
#include <stdio.h>
#include <math.h>

int main() {
    float peso, altura, IMC;

    printf("Digite seu peso(kg): ");
    scanf("%f", &peso);
    printf("Digite sua altura(m): ");
    scanf("%f", &altura);

    IMC = peso / pow(altura, 2);

    printf("O IMC de uma pessoa com peso %.2fkg e altura %.2fm é igual a %.2f.", peso, altura, IMC);
    return 0;
}