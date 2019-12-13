import sqlite3

def magica():
  return 42
  
#retorna o registro como um objeto
def conversor(cursor, linha):
    d = {}
    for seq, col in enumerate(cursor.description):
        d[col[0]] = linha[seq]
    return d

connection = sqlite3.connect('c:/dados/fabrica/fabrica.db')
connection.create_function("magica", 0, magica)
connection.row_factory = conversor

cursor = connection.cursor()
dados = cursor.execute ('select magica() as result, produto.* from produto')
for d in dados:
  print(d['Descricao'], d['Preco'])


connection.commit()
connection.close()