import requests
import json
url = 'http://localhost:8082/api/medicoes' #servidor Rest Dataware
r = requests.get(url)
medicoes = json.loads(r.text)
root = 'result'
for medicao in medicoes[root]:
  print(medicao['data_base'])
  
print('Isso que eu chamo de Json')
print('Comunidade RDW e Python Brasil', 'tmj')