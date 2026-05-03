#EXcontroledepresença

alunos = ["Leandro","Alexandro","Armando","Firmino","Gerúndio"]
presentes = 0
ausentes = 0

for i in range(5):
    presenca = input(f"{alunos[i]} está presente:(P ou A): ").upper()
    if presenca == "P":
        presentes += 1
    elif presenca == "A":
        ausentes += 1
    else:
        print("Status inválido.")

print(f"{presentes} alunos estão presente e {ausentes} alunos estão ausentes.")