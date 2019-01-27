import requests
#ATIVE CASO UTILIZE WINDOWS
#import os
import json
import clipboard

trum=clipboard.paste()
dart=(trum[3:4])

if dart != ".":
  print("Você não copiou um número IP válido!")

else:
  req=requests.get('http://ipinfo.io/{}'. format(trum))

  trat=json.loads(req.text)

  print("")
  ip=trat['ip']
  host=trat['hostname']
  city=trat['city']
  pais=trat['country']
  loc=trat['loc']

  print("O ip é:",ip)
  print("Hostname:",host)
  print("Cidade: ",city)
  print("País: ",pais)
  print("Geo Localização: ",loc)
  print("")
  #ATIVE CASO UTILIZE WINDOWS
  #os.system("pause")
