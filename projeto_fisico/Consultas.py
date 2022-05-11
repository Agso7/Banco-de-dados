import sqlite3

#Conectando...
conn = sqlite3.connect("escola.db")

#Definindo o cursor...
cursor = conn.cursor()

#Definicao da consulta a ser realizada
numero = int(input("Qual consulta deseja executar (1 - 10): "))

#Alunos reprovados - nota < 7
if numero == 1:
    r = cursor.execute("SELECT CPF,Nome,Matricula,Nota from Aluno WHERE Situacao = 'REPROVADO';")

    for linha in r.fetchall():
        print(linha)

#Aulas que irao acontecer na Data X(disciplina,horario,serie)
if numero == 2:
    r = cursor.execute("""SELECT Turma_Disciplina_Aula.Nome_Disciplina,Turma_Disciplina_Aula.Horario,Turma.Serie
                        FROM Turma_Disciplina_Aula JOIN Turma ON Turma_Disciplina_Aula.Codigo = Turma.Codigo 
                         WHERE Turma_Disciplina_Aula.Data = "23/05/2022";""")

    for linha in r.fetchall():
        print(linha)

#Professor que tem mais quantidade de subordinados
if numero == 3:
    r = cursor.execute("""Select Coordenado_Por, count(Coordenado_Por) AS Total_De_Subordinados 
                       from Coordena group by Coordenado_Por having count(Coordenado_Por)=
                       (Select max(Totais.Total_De_Subordinados) from (Select count(Coordenado_Por) as Total_De_Subordinados from Coordena group by (Coordenado_Por)) as Totais);""")

    for linha in r.fetchall():
        print(linha)

#Alunos que tao com a media acima da media geral dos Alunos
if numero == 4:
    r = cursor.execute("SELECT Matricula,Nome From Aluno WHERE Nota > (SELECT avg(Nota) from Aluno);")

    for linha in r.fetchall():
        print(linha)

#Nome do alunos e seus respectivos turnos e series
if numero == 5:
    r = cursor.execute("SELECT Aluno.Nome, Turma.Serie,Turma.Turno FROM Aluno JOIN Aluno_Turma ON Aluno.CPF = Aluno_Turma.CPF JOIN Turma ON Aluno_Turma.Codigo = Turma.Codigo;")

    for linha in r.fetchall():
        print(linha)

#As pessoas cadastradas no sistema (professores + alunos)
if numero == 6:
    r = cursor.execute("SELECT CPF,NOME FROM ALUNO UNION SELECT CPF,NOME FROM PROFESSOR;")

    for linha in r.fetchall():
        print(linha)

#A materia que um professor 'X' ensina
if numero == 7:
    r = cursor.execute("SELECT Ministra.Nome_Disciplina FROM Ministra JOIN Professor ON Ministra.CPF = Professor.CPF WHERE Professor.Nome = 'Juliana';")

    for linha in r.fetchall():
        print(linha)

#Todos os CPFs dos Alunos com suas respectivas data de aula e disciplina
if numero == 8:
    r = cursor.execute("""SELECT Aluno_Turma.CPF, Turma_Disciplina_Aula.Nome_Disciplina, Turma_Disciplina_Aula.Data
                       FROM Aluno_Turma LEFT JOIN Turma_Disciplina_Aula ON Aluno_Turma.Codigo = Turma_Disciplina_Aula.Codigo;""")

    for linha in r.fetchall():
        print(linha)

#Selecionar nomes e matriculas dos alunos de um codigo de turma X
if numero == 9:
    r = cursor.execute("SELECT Aluno.Nome,Aluno.Matricula FROM Aluno WHERE EXISTS(SELECT CPF FROM Aluno_Turma WHERE Aluno.CPF = Aluno_Turma.CPF AND Codigo = '124589');")

    for linha in r.fetchall():
        print(linha)

#Selecionar Nome e Matricula do Professor cujo nao ensinem determinadas materias
if numero == 10:
    r = cursor.execute("""SELECT Professor.Nome,Professor.ID_Prof FROM Professor
                       WHERE Professor.CPF NOT IN
                       (SELECT CPF FROM Ministra WHERE Professor.CPF = Ministra.CPF AND Nome_Disciplina IN ('Literatura','Historia','Geografia','Sociologia'));""")

    for linha in r.fetchall():
        print(linha)