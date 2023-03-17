from Function import *
from Classes import *
f = open("regitsro.txt", "r")
for linha in f:
    escola.lista.append(linha)
f.close()
resp = True
while resp:
    op = menu()
    if op == 1:
        cadastrar()
    elif op == 2:
        pesquisar()
    elif op == 3:
        imprimir()
    elif op == 4:
        cadastrar_prof()
    elif op == 5:
        cadastrar_aluno()
    elif op == 6:
        lancar_notas()
    elif op == 7:
        listar_alunos()
    elif op == 8:
        listar_notas()
    elif op == 9:
        f = open("regitsro.txt", "w")
        for i in escola.lista:
            f.write(str(i) + '\n')
        f.close()
        print('O código acabou...')
        resp = False
