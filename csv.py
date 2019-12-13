# todo: Importar CSV, depois com o mesmo código importar xlsx

import pandas
import matplotlib.pyplot as plt # Biblioteca de gráficos do pyhton
#from matplotlib import style

#-------------------------------------------------------------------------------

titulo = ''' 
Gráfico de medições  
                                                      Py4Delphi + Pandas + csv
''' 
url = 'c:\delphi\python\exemplos\medicoes.csv' 
valores = []  
tipo = 'linha' # escolha o tipo do gráfico (linha, barra, hist, calor, violino )

medicoes = pandas.read_csv(url, encoding = 'UTF-8', sep = ';', nrows = 10, decimal  = ',')
#print(csv.shape)
print(medicoes.head(3))

#------------------------------------------------------------------------------
#filtrando
#medicoes = medicoes[medicoes.Nota > 50]
#------------------------------------------------------------------------------
valores = medicoes['Vendas']
metas = medicoes.Meta          
          
#print('valores:')
#print(valores)           

#print('metas:')
#print(metas)
 
# Gerar o gráfico
rotulos = range(len(valores))
serie={}
serie['medicoes'] = valores
serie['metas'] = metas

#print(style.available)
#style.use('fivethirtyeight')

if tipo == 'linha':
  plt.plot(rotulos,serie['medicoes'])
  plt.plot(rotulos, serie['metas'], alpha = 0.5)
  
elif tipo == 'barra':
  plt.bar(rotulos,serie['medicoes'])
  plt.bar(rotulos, serie['metas'])

elif tipo == 'hist':
  plt.hist(serie['medicoes'],8, density=True, histtype='bar', facecolor='g', alpha=0.75) # histtype='stepfilled'

elif tipo == 'calor':
  plt.hist2d(serie['medicoes'],rotulos) 

  
plt.title(titulo) 
plt.xlabel('Indicador')
plt.ylabel('$')
plt.show()
