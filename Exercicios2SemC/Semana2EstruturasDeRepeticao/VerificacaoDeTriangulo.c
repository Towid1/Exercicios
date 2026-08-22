//Exercicio de verificação de triângulos
#include <stdio.h>

float a, b, c;

void apresentador(int existe) {
    if (existe == 1) {
        printf("Seu triângulo existe!\n");
    } else {
        printf("Seu triângulo não existe!\n");
    }
}

int verificador(float a, float b, float c){
    if (a < b + c && b < a + c && c < a + b) {
        return 1;
    }
        return 0;
}

int main() {
    printf("Digite o tamanho de um lado do triângulo: ");
    scanf("%f", &a);
    printf("Digite o tamanho de outro lado do triângulo: ");
    scanf("%f", &b);
    printf("Digite o tamanho do último lado do triângulo: ");
    scanf("%f", &c);

    int existe = verificador(a, b, c);
    apresentador(existe);
    return 0;
}