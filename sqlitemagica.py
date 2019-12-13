import sqlite3

def magica():
  return 42

connection = sqlite3.connect('c:/dados/fabrica/fabrica.db')
connection.create_function("magica", 0, magica)

cursor = connection.cursor()
dados = cursor.execute ('select magica()')
for d in dados:
  print(d)


connection.commit()
connection.close()