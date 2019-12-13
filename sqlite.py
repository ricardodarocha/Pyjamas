import sqlite3
connection = sqlite3.connect('c:/dados/fabrica/fabrica.db')
#connection.row_factory = sqlite3.Row

cursor = connection.cursor()
cursor.execute ('select * from produto')

def Proximo():
  linha = cursor.fetchone()
  if linha is not None:
    print(linha)
  return linha
  
linha = Proximo()

while linha is not None:
  linha = Proximo()


connection.commit()
connection.close()