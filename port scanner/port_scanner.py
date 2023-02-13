import socket

portas = open("portas.txt").readlines()
for i in range(0,len(portas)):
    portas[i] = portas[i].strip()

for porta in portas:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.75)
    cod_status = sock.connect_ex(("bancocn.com",int(porta)))
    if cod_status == 0:
        print(porta,"aberta")