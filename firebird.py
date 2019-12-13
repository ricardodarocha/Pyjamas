import fdb
con = fdb.connect(dsn='C:\dados\Demonstracao\PYJAMAS.FDB', user='sysdba', password='masterkey', charset='UTF8')

cur = con.cursor()

# Execute the SELECT statement:
cur.execute("select * from produto")

# Retrieve all rows as a sequence and print that sequence:
#print (cur.fetchall())

#for (nome, codigo) in cur:
#  print  ('%s has been publicly available since %d.'.format(nome, codigo)   )

# 2. Equivalently:
#cur.execute(SELECT)
#for row in cur:
#    print ('{} = {}.'.format(row[0], row[1])  )

# 3. Using mapping-iteration rather than sequence-iteration:
#cur.execute(SELECT)
#for row in cur.itermap():
#  print(row)
#  print ('{NOME} possui o código {CODIGO}'.format(row) )