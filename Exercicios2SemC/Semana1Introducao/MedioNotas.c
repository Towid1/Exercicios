//Exercicio me media de notas
#include <stdio.h>

float nota1;
float nota2;
float nota3;

int main(){
    printf("Digite a primeira nota: ");
    scanf("%f", &nota1);
    printf("Digite a segunda nota: ");
    scanf("%f", &nota2);
    printf("Digite a terceira nota: ");
    scanf("%f", &nota3);

    float media;
    media = (nota1 + nota2 + nota3) / 3;

    printf("A sua média é %.2f.", media);
}