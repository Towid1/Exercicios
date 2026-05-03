#EXadvinheonumero
import random

numero = random.randint(1,10)
chute = 0

while chute != numero:
    chute = int(input("Digite um número de 1 a 10: "))
    if chute > numero:
        print("O número é Menor")
    elif chute < numero:
        print("O número é Maior")

print(f"Acertou! O número era {numero}")
