import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

host = "localhost"
porta_servidor = 5432
msg = "\nOlá cliente, tudo certo por aqui parceiro"

sock.bind((host,porta_servidor)) 
# O bind faz com que o host funcione como um servidor que recebe mensagens na porta escolhida

while 1:
    dados, end = sock.recvfrom(4096) # Canal de comunicação UDP
    if dados:
        print("Servidor: enviando a mensagem ...")
        sock.sendto(dados + (msg.encode()), end)