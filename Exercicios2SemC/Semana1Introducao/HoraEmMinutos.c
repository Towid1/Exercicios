//Exercicio de horas em minutos
#include <stdio.h>

float hora;
float minutos;
float resto;

int main() {
    printf("Digite o horário atual(HH.MM): ");
    scanf("%f", &hora);

    int inteiro = (int)hora;
    resto = hora - inteiro;
    minutos = (inteiro * 60) + (resto * 100);

    printf("As %.2f horas se passaram %.0f minutos no dia.", hora, minutos);
}