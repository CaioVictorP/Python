import sqlite3

connection = sqlite3.connect("escola.db")
cursor = connection.cursor()
cursor.execute("CREATE TABLE Tabela1 (nome TEXT, matricula INTEGER, cpf INTEGER, curso TEXT, periodo INTEGER)")

nome = input("Digite o nome do aluno: ")
matricula = input("Digite a matrícula do aluno: ")
cpf = input("Digite o CPF do aluno: ")
curso = input("Digite o curso do aluno: ")
periodo = input("Digite o período do aluno: ")
cursor.execute("INSERT INTO Tabela1 VALUES ('"+nome+"', '"+matricula+"', '"+cpf+"', '"+curso+"', '"+periodo+"')")

rows = cursor.execute("SELECT * FROM Tabela1").fetchall()
print(rows)

pesq = print("Digite o número da matrícula que deseja pesquisar: ")
busc = cursor.execute("SELECT * FROM Tabela1 WHERE cpf LIKE "+pesq+"")