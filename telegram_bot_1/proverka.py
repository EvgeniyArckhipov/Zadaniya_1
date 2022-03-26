import telebot
import configure
import requests
import json

TOKEN_API = str(configure.config['token_api'])
nal = requests.get(f'http://api.exchangeratesapi.io/v1/symbols?access_key={TOKEN_API}')
slovar_values = json.loads(nal.content)['symbols']
q = []
for key,value in slovar_values.items():
    q.append(key+':'+value)
print(q)
ss = '\n'.join(q)
print(ss)


#print(l)
#print(type(vse_values))
#print(vse_values)

#print(q)
#print(vse_values)
#print(TOKEN_API)