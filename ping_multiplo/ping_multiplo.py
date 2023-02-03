import os
import time

arquivo = open("hosts.txt")
linhas_ip = arquivo.readlines()
arquivo.close()
for linha in linhas_ip:
    print("Verificando o ip: {}".format(linha))
    print("#" * 60)
    os.system("ping -c 2 {}".format(linha))
    print("-" * 60)
    time.sleep(5) # Espera cinco segundos para mandar executar o próximo ping
