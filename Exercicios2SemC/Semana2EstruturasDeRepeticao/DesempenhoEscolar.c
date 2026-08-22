//Exercicio de calculo de desempenho escola com média e presença
#include <stdio.h>

void desempenho(float media, int presenca) {
    if (presenca < 75.0) {
        printf("Voce foi REPROVADO pois possui menos que 75%% de presença!\n");
    } else { if (media >= 7.5) {
            printf("Você foi APROVADO!\n");
        } else {
            printf("Você ficou DE EXAME!\n");
        }
    }
}

int main() {
    float media;
    int presenca;

    printf("Digite sua Média(0-10): ");
    scanf("%f", &media);
    printf("Digite sua Porcentagem de Presença(0-100): ");
    scanf("%d", &presenca);

    desempenho(media, presenca);
}