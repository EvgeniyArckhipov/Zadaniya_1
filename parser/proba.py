import requests
import json

w = requests.get('https://api.github.com')
print(w.content)

s = w.json()
print(s)



#j = w.json()
#print(j)