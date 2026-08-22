//Exercicio junior de numero sorteado
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    srand(time(NULL));
    int numSorteado = 1 + (rand() % 100);
    int acerto, tentativas = 0;
    while (acerto != numSorteado)
    {
        tentativas++;
        printf("Digite seu palpite: ");
        scanf("%d", &acerto);

        if (acerto < numSorteado) {
            printf("Você chutou muito baixo! O valor correto é maior\n");
        } 
        if (acerto > numSorteado) {
            printf("Você chutou muito alto! O valor correto é menor\n");
        }
    }
    printf("Parabéns!!! Você acertou! O número sorteado era %d! Número acertado em %d tentativas.", numSorteado, tentativas);
}