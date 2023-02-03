import os # Biblioteca para usar funcionalidades do SO

print("#" * 60) # Imprime o # 60 vezes
ip_ou_host = input("Digite um IP ou Host: ") # Pedindo o usuário para ele digitar um IP
print("-" * 60) # Imprime o - 60 vezes
os.system("ping -c 7 {}".format(ip_ou_host))
 # Executando o ping a partir do método system da biblioteca os
 # -c é a quantidade de vezes que o ping será executado
print("-" * 60) # Imprime o - 60 vezes