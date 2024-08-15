import requests
#ATIVE CASO UTILIZE WINDOWS
#import os
import json
import clipboard

ip=clipboard.paste()

# if dart != ".":
#   print("Você não copiou um número IP válido!")
res=requests.get('http://ipinfo.io/{}'. format(ip))

resJson=json.loads(res.text)
# print(resJson)
print("")
ip=resJson['ip']
host=resJson['org']
city=resJson['city']
pais=resJson['country']
loc=resJson['loc']

print("O ip é:",ip)
print("Org:",host)
print("Cidade: ",city)
print("País: ",pais)
print("Geo Localização: ",loc)
print("")
#ATIVE CASO UTILIZE WINDOWS
#os.system("pause")
