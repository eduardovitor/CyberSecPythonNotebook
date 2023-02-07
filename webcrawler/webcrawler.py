from bs4 import BeautifulSoup
import requests
from collections import Counter
import operator

def coletar_palavras(url):
    lista_palavras = []
    cod_fonte = requests.get(url).content
    soup = BeautifulSoup(cod_fonte,"html.parser")
    for texto in soup.findAll("div",{"class": "entry-content"}):
        conteudo = texto.text
        palavras = conteudo.lower().split()
        for palavra in palavras:
            lista_palavras.append(palavra)
    return lista_palavras

def limpar_palavras(lista_palavras):
    lista_limpa = []
    simbolos = "!@#$%¨&*()-+,.^~?;:/"
    for palavra in lista_palavras:
        for i in range(0,len(simbolos)):
            palavra = palavra.replace(simbolos[i],'')
        if len(palavra)>0:
            lista_limpa.append(palavra)
    return lista_limpa
        
def retornaDictPalavras(lista_palavras):
    palavras_freq_dict = {}
    for palavra in lista_palavras:
        if palavra in palavras_freq_dict:
            palavras_freq_dict[palavra]+=1
        else:
            palavras_freq_dict[palavra]=1
    for key,value in sorted(palavras_freq_dict.items(), key=operator.itemgetter(1)):
        print(f'{key}:{value}')
    contador = Counter(palavras_freq_dict)
    palavras_comuns = contador.most_common(10)
    print(palavras_comuns)

url="https://www.geeksforgeeks.org/python-programming-language/"

lista_palavras = coletar_palavras(url)
lista_limpa = limpar_palavras(lista_palavras)
retornaDictPalavras(lista_limpa)