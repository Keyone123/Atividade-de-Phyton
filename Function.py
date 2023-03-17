from Classes import *


def menu():
    print('\n--------------------- Menu Acadêmico ---------------------\n')
    print('1.Cadastrar Disciplina')
    print('2. Pesquisar disciplina')
    print('3. Listar disciplinas cadastradas')
    print('4. Cadastrar professor em disciplina')
    print('5. Matricular aluno em disciplina')
    print('6. Lançar notas do aluno em uma disciplina')
    print('7. Listar alunos de uma disciplina')
    print('8. Listar notas dos alunos de uma disciplina')
    print('9. Sair')
    print('\n-------------------------------------------------------------\n')
    op = int(input('Digite a opção que deseja: '))
    return op


def cadastrar():
    disciplina.cod = int(input('Digite o código da disciplina: '))
    for i in escola.lista:
        if i[0] == disciplina.cod:
            print('\nCódigo já cadastrado!!!!!\n')
            return
    disciplina.nome = input('Digite o nome da disciplina: ')
    disciplina.semestre = int(input('Digite o semestre que a disciplina está: '))
    disciplina.periodo = int(input('Digite o periodo que se encontra o ano {}: '.format(disciplina.semestre)))
    disciplina.carga = int(input('Digite a quantidade de horas que há na disciplina: '))
    horario = int(input('Digite o horário que a disciplina se encontra: '))
    d = int(input('Quantos dias na semana serão a disciplina: '))
    if d == 2:
        dia1 = int(input('Digite o primeiro dia da semana da disciplina {}: '.format(disciplina.nome)))
        dia2 = int(input('Digite o segundo dia da semana da disciplina {}: '.format(disciplina.nome)))
        tupla_dia = (dia1, dia2)
        disciplina.horario = [tupla_dia, horario]
    elif d == 3:
        dia1 = int(input('Digite o primeiro dia da semana da disciplina {}: '.format(disciplina.nome)))
        dia2 = int(input('Digite o segundo dia da semana da disciplina {}: '.format(disciplina.nome)))
        dia3 = int(input('Digite o terceiro dia da semana da disciplina {}: '.format(disciplina.nome)))
        tupla_dia = (dia1, dia2, dia3)
        disciplina.horario = [tupla_dia, horario]
    lista_disciplina = (
        disciplina.cod, disciplina.nome, disciplina.semestre, disciplina.periodo, [], [], disciplina.carga,
        disciplina.horario)
    escola.lista.append(lista_disciplina)
    print('\nDisciplina cadastrada!!!\n')


def pesquisar():
    dis = input('Digite o nome da disciplina que será pesquisada: ')
    for i in escola.lista:
        if i[1] == dis:
            print('\nDisciplina encontrada!!!\n')
            print(i)


def imprimir():
    for i in escola.lista:
        print(i)


def cadastrar_prof():
    dis = input('Digite a disciplina que será introduzida o professor: ')
    for i in escola.lista:
        if i[1] == dis:
            print('\nDisciplina encontrada!!!!\n')
            cod = int(input('Digite o código do professor: '))
            for j in i[4]:
                if j[0] == cod:
                    print('\nCódigo já cadastrado!!!!\n')
                    return
            nome = input('Digite o nome do professor a ser cadastrado: ')
            tupla_prof = (cod, nome)
            i[4].append(tupla_prof)
            print('\nProfessor foi cadastrado!!\n')


def cadastrar_aluno():
    dis = input('Digite a disciplina que será introduzida o aluno: ')
    for i in escola.lista:
        if i[1] == dis:
            print('\nDisciplina encontrada!!!!!\n')
            cod = int(input('Digite o código do aluno: '))
            for j in i[5]:
                if j[0] == cod:
                    print('\nCódigo já cadastrado!!!!\n')
                    return
            nome = input('Digite o nome do aluno: ')
            curso = input('Digite o curso do aluno: ')
            tupla_aluno = (cod, nome, curso, aluno.lista_aluno, aluno.lmedia)
            i[5].append(tupla_aluno)
            print('\nAluno cadastrado com sucesso!!!!!\n')


def lancar_notas():
    dis = input('Digite a disciplina que será pesquisada: ')
    for i in escola.lista:
        if i[1] == dis:
            print('\nDisciplina encontrada!!!!!\n')
            name = input('Digite o nome do aluno que será pesquisado: ')
            for j in i[5]:
                if j[1] == name:
                    print('Aluno encontrado!!!!!\n')
                    aluno.nota1 = float(input('Digite a primeira nota: '))
                    aluno.nota2 = float(input('Digite a segunda nota: '))
                    aluno.nota3 = float(input('Digite a terceira nota: '))
                    tupla_aluno = (aluno.nota1, aluno.nota2, aluno.nota3)
                    aluno.media = (aluno.nota3 + aluno.nota2 + aluno.nota1) / 3.0
                    j[3].append(tupla_aluno)
                    tupla_media = aluno.media
                    j[4].append(tupla_media)


def listar_alunos():
    dis = input('Digite a disciplina que será pesquisada: ')
    for i in escola.lista:
        if i[1] == dis:
            print('\nDisciplina encontrada!!!!!\n')
            for j in i[5]:
                print(j[1])


def listar_notas():
    dis = input('Digite a disciplina que será pesquisada: ')
    for i in escola.lista:
        if i[1] == dis:
            print('\nDisciplina encontrada!!!!!\n')
            for j in i[5]:
                print('{}: {}'.format(j[1], j[3]))

