#EXreajustecomarredondamento
import math

preco = float(input("Digite o preço do produto: "))
preco += (preco * 0.075)

print(f"Novo valor {preco}, Arrendondado pra cima: {math.ceil(preco)} e pra baixo: {math.floor(preco)}")