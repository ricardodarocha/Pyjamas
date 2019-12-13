import sqlite3
connection = sqlite3.connect('c:/dados/fabrica/fabrica.db')

cursor = connection.cursor()
dados = cursor.execute ('select * from produto')
for d in dados:
  print(d)


connection.commit()
connection.close()