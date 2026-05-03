#EXsalariocombonus

salario = float(input("Digite seu salario: "))
bonus = float(input("Digite sua taxa de bonûs: "))

print(f"Seu novo salário é de {salario + (salario * (bonus / 100))} reais")