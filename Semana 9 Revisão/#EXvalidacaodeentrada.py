#EXvalidacaodeentrada


def classificacao(idade):
    if idade <= 12:
        return "criança"
    elif idade < 18:
        return "adolecente"
    else:
        return "adulto"

def validacao(idade):
    if idade >= 0:
        return classificacao(idade)
    else:
        return "Idade inválida"
    
print(validacao(int(input("Digite a idade: "))))