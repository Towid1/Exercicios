#EXvalidacaodesenha

senha = int(input())

while senha != 1234:
    print("Senha incorreta!")
    senha = int(input())
else:
    print("Acesso permitido!")