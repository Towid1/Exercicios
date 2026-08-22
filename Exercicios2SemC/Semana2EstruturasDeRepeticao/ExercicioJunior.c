//Exercicio junior de numero sorteado
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    srand(time(NULL));
    int numSorteado = 1 + (rand() % 100);
    int acerto = 0;
    while (acerto != numSorteado)
    {
        printf("Numero: %d\n", numSorteado);
        printf("Digite seu palpite: ");
        scanf("%d", &acerto);

        if (acerto < numSorteado) {
            printf("Você chutou muito alto! O valor correto é menor\n");
        } else {
            printf("Você chutou muito baixo! O valor correto é maior\n");
        }
    }
    printf("Parabéns!!! Você acertou! O número sorteado era %d!", numSorteado);
}