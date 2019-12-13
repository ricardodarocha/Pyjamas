import requests
import json
import matplotlib.pyplot as plt # Biblioteca de gráficos do pyhton
import math
#-------------------------------------------------------------------------------

titulo = ''' 
Gráfico de medições  
                                                      Py4Delphi + Rest Dataware
''' 
url = 'http://localhost:8082/api/medicoes' #servidor Rest Dataware
valores = []  
tipo = 'linha' # escolha o tipo do gráfico (linha, barra, hist, calor, violino )

req = requests.get(url)
#req = requests.get(url, auth=('testserver', 'testserver'))
medicoes = json.loads(req.text)
root = 'result'   
                                                                                
#===============================================================================
for medicao in medicoes[root]:
  valores.append(medicao['valor'])
#===============================================================================

print(valores)  
# Gerar o gráfico
rotulos = range(len(valores))
serie={}
serie['medicoes'] = valores
seno = lambda val : [ 100000 * math.sin(x) for x in val ]
senoide = seno(valores)

if tipo == 'linha':
  plt.plot(rotulos,serie['medicoes'])
  plt.plot(senoide)
  
elif tipo == 'barra':
  plt.bar(rotulos,serie['medicoes'])

elif tipo == 'hist':
  plt.hist(serie['medicoes'],8, density=True, histtype='bar', facecolor='g', alpha=0.75) # histtype='stepfilled'

elif tipo == 'calor':
  plt.hist2d(serie['medicoes'],rotulos) 

  
plt.title(titulo) 
plt.xlabel('Indicador')
plt.ylabel('$')
plt.show()