import sqlite3

#Conectando...
conn = sqlite3.connect("escola.db")

#Definindo o cursor...
cursor = conn.cursor()

#Criando as tabelas...
cursor.execute("""
CREATE TABLE Turma (
        Codigo VARCHAR(20) NOT NULL PRIMARY KEY,
        Turno VARCHAR(20) NOT NULL,
        Serie VARCHAR(20) NOT NULL
);

CREATE TABLE Disciplina (
        Nome_Disciplina VARCHAR(20) NOT NULL PRIMARY KEY
);

CREATE TABLE Sala (
        Num_Sala VARCHAR(20) NOT NULL PRIMARY KEY
);

CREATE TABLE Aula (
        Num_Sala VARCHAR(20) NOT NULL,
        Data VARCHAR(20) NOT NULL,
        Horario VARCHAR(20) NOT NULL,
        Dia VARCHAR(20) NOT NULL,
        PRIMARY KEY (Num_Sala, Data, Horario),
  		FOREIGN KEY (Num_Sala) REFERENCES Sala(num_sala)
);

CREATE TABLE Aluno (
        CPF VARCHAR(20) NOT NULL PRIMARY KEY,
        Matricula VARCHAR(20) NOT NULL,
        Nota INT NOT NULL,
        Situacao VARCHAR(20) NOT NULL,
        Nome VARCHAR(20) NOT NULL,
        Data_Nasc VARCHAR(20) NOT NULL,
        Sexo VARCHAR(20) NOT NULL,
        Email VARCHAR(20) NOT NULL,
        End_CEP VARCHAR(20) NOT NULL,
        End_Bairro VARCHAR(20) NOT NULL,
        End_Logradouro VARCHAR(20) NOT NULL
);

CREATE TABLE Professor (
        CPF VARCHAR(20) NOT NULL PRIMARY KEY,
        Salario VARCHAR(20) NOT NULL,
        ID_Prof INT NOT NULL,
        Especialidade VARCHAR(20) NOT NULL,
        Nome VARCHAR(20) NOT NULL,
        Data_Nasc VARCHAR(20) NOT NULL,
        Sexo VARCHAR(20) NOT NULL,
        Email VARCHAR(20) NOT NULL,
        End_CEP VARCHAR(20) NOT NULL,
        End_Bairro VARCHAR(20) NOT NULL,
        End_Logradouro VARCHAR(20) NOT NULL
);

CREATE TABLE Ministra (
        CPF VARCHAR(20) NOT NULL PRIMARY KEY,
        Nome_Disciplina VARCHAR(20) NOT NULL,
		FOREIGN KEY (Nome_Disciplina) REFERENCES Disciplina(nome_disciplina)
);

CREATE TABLE Pertence (
        CPF VARCHAR(20) NOT NULL PRIMARY KEY,
        Codigo VARCHAR(20) NOT NULL,
  		FOREIGN KEY (codigo) REFERENCES Turma(codigo)
);

CREATE TABLE Possui (
        Codigo VARCHAR(20) NOT NULL,
        Nome_Disciplina VARCHAR(20) NOT NULL,
        Horario VARCHAR(20) NOT NULL,
        Data VARCHAR(20) NOT NULL,
        PRIMARY KEY (Codigo, Nome_Disciplina)
);

CREATE TABLE Coordena (
        Coordenador VARCHAR(20) NOT NULL,
        Coordenado_Por VARCHAR(20) NOT NULL,
        PRIMARY KEY (Coordenador, Coordenado_Por),
  		FOREIGN KEY (Coordenador) REFERENCES Professor(cpf),
  		FOREIGN KEY (Coordenado_Por) REFERENCES Professor(cpf)
);

""")

print('Tabelas criadas com sucesso.')

arquivo = open("dados.csv", "r")

cont = 0

#Inserindo dados na tabela Turma
for line in arquivo:
    if cont == 12:
        break
    elif cont == 0:
        cont += 1
        continue
    linha = line.split(";")
    cod = linha[0]
    turno = linha[1]
    serie = linha[2]
    cont += 1
    cursor.execute("INSERT INTO Turma(Codigo,Turno,Serie) VALUES(cod,turno,serie)")

#Inserindo dados na tabela Disciplina
cont = 0

for line in arquivo:
    if cont == 25:
        break
    elif cont < 14:
        cont += 1
        continue
    linha = line.split(";")
    nome_disciplina = linha[0]
    cont += 1
    cursor.execute("INSERT INTO Disciplina(Nome_Disciplina) VALUES(nome_disciplina)")

#Inserindo dados na tabela Sala
cont = 0

for line in arquivo:
    if cont == 36:
        break
    elif cont < 27:
        cont += 1
        continue
    linha = line.split(";")
    num_sala = linha[0]
    cont += 1
    cursor.execute("INSERT INTO Sala(Num_Sala) VALUES(num_sala)")

#Inserindo dados na tabela Aula
cont = 0

for line in arquivo:
    if cont == 47:
        break
    elif cont < 38:
        cont += 1
        continue
    linha = line.split(";")
    num_sala = linha[0]
    data = linha[1]
    horario = linha[2]
    dia = linha[3]
    cont += 1
    cursor.execute("INSERT INTO Aula(Num_Sala,Data,Horario,Dia) VALUES(num_sala,data,horario,dia)")

#Inserindo dados na tabela Aluno
cont = 0

for line in arquivo:
    if cont == 94:
        break
    elif cont < 49:
        cont += 1
        continue
    linha = line.split(";")
    cpf = linha[0]
    matricula = linha[1]
    nota = linha[2]
    situacao = linha[3]
    nome = linha[4]
    data_nasc = linha[5]
    sexo = linha[6]
    email = linha[7]
    end_cep = linha[8]
    end_bairro = linha[9]
    end_logradouro = linha[10]
    cont += 1
    cursor.execute("INSERT INTO Aluno(CPF,Matricula,Nota,Situacao,Nome,Data_Nasc,Sexo,Email,End_CEP,End_Bairro,End_Logradouro) VALUES(cpf,matricula,nota,situacao,nome,data_nasc,sexo,email,end_cep,end_bairro,end_logradouro)")

#Inserindo dados na tabela Professor
cont = 0

for line in arquivo:
    if cont == 107:
        break
    elif cont < 96:
        cont += 1
        continue
    linha = line.split(";")
    cpf = linha[0]
    salario = linha[1]
    id_prof = linha[2]
    especialidade = linha[3]
    nome = linha[4]
    data_nasc = linha[5]
    sexo = linha[6]
    email = linha[7]
    end_cep = linha[8]
    end_bairro = linha[9]
    end_logradouro = linha[10]
    cont += 1
    cursor.execute("INSERT INTO Professor(CPF,Salario,ID_Prof,Especialidade,Nome,Data_Nasc,Sexo,Email,End_CEP,End_Bairro,End_Logradouro) VALUES(cpf,salario,id_prof,especialidade,nome,data_nasc,sexo,email,end_cep,end_bairro,end_logradouro)")

#Inserindo dados na tabela Ministra
cont = 0

for line in arquivo:
    if cont == 120:
        break
    elif cont < 109:
        cont += 1
        continue
    linha = line.split(";")
    cpf = linha[0]
    nome_disciplina = linha[1]
    cont += 1
    cursor.execute("INSERT INTO Ministra(CPF,Nome_Disciplina) VALUES(cpf,nome_disciplina)")

#Inserindo dados na tabela Pertence
cont = 0

for line in arquivo:
    if cont == 167:
        break
    elif cont < 122:
        cont += 1
        continue
    linha = line.split(";")
    cpf = linha[0]
    cod = linha[1]
    cont += 1
    cursor.execute("INSERT INTO Pertence(CPF,Codigo) VALUES(cpf,cod)")

#Inserindo dados na tabela Possui
cont = 0

for line in arquivo:
    if cont == 180:
        break
    elif cont < 169:
        cont += 1
        continue
    linha = line.split(";")
    cod = linha[0]
    nome_disciplina = linha[1]
    horario = linha[2]
    data = linha[3]
    cont += 1
    cursor.execute("INSERT INTO Possui(Codigo,Nome_Disciplina,Horario,Data) VALUES(cod,nome_disciplina,horario,data)")

#Inserindo dados na tabela Coordena
cont = 0

for line in arquivo:
    if cont == 193:
        break
    elif cont < 182:
        cont += 1
        continue
    linha = line.split(";")
    coordena = linha[0]
    coordenado = linha[1]
    cont += 1
    cursor.execute("INSERT INTO Coordena(Coordenador,Coordenado_Por) VALUES(coordena,coordenado)")

#Desconectando...
conn.close()
