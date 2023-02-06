import itertools
string = input("Digite a string a ser usada como base: ")

iteracoes = itertools.permutations(string,len(string)) 
# O resultado disso será uma lista que conterá caracteres permutados em cada indice

for iter in iteracoes:
    palavra = ''.join(iter) # Juntando os caracteres de cada indice para formar uma palavra
    print(palavra)