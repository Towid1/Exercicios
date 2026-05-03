#EXsistemadecadastros

def sistema(nome,idade):
    if idade < 18:
        faixa = "menor de idade"
    elif idade <= 59:
        faixa = "adulto"
    else:
        faixa = "idoso"
    return f"{nome} é classificado como {faixa}"

nome = input("Digite o nome: ")
idade = int(input("Digite a idade: "))

print(sistema(nome,idade))