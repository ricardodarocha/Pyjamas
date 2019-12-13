import requests
import json
import base64

url = 'http://localhost:8082/api/avatar' #Servidor Rest Dataware
r = requests.get(url)
avatar = json.loads(r.text)
root = "PARAMS"
imgstring = avatar[root][0]['ASBITMAP']
imgdata = base64.b64decode(imgstring)
with open('avatar.png', 'wb') as f:
  f.write(imgdata)
  print('Download efetuado com sucesso')
  