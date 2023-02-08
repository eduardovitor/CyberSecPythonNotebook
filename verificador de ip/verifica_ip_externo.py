import json
from urllib.request import urlopen

url = "http://ipinfo.io/json"

resposta = urlopen(url)

dados_json = json.load(resposta)

ip = dados_json["ip"]

cidade = dados_json["city"]

print(f"O ip é {ip} e a cidade é {cidade}")