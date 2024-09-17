import sqlite3

connection = sqlite3.connect("login.db")
cursor = connection.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS Abrigo (nome TEXT, cpf INTEGER, pontuacao INTEGER)")

nome = input("Digite o nome do abrigado: ")
cpf = input("Digite o CPF do abrigado: ")
cursor.execute("INSERT INTO Abrigo VALUES ('"+nome+"', '"+cpf+"', 0)")

newscore = input("Digite a nova pontuação: ")
cpfs = input("Digite o seu CPF para salvar sua pontuação: ")
save = cursor.execute("UPDATE Abrigo SET pontuacao = "+ newscore +" WHERE cpf = "+ cpfs)

connection.commit()