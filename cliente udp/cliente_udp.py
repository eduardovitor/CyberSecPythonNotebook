import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
# SOCK_DGRAM é um tipo de soquete usado para comunicações UDP

host = "localhost" 
porta_servidor = 5432
msg = "Olá servidor, tudo bem?"

try:
    sock.sendto(msg.encode(), (host,porta_servidor)) 
    # É necessário empacotar a mensagem como um pacote UDP: msg.encode()
    dados, end = sock.recvfrom(4096) 
    # sock.recvfrom é o canal de comunicação UDP para onde os dados chegam
    # end é o endereço do host
    dados = dados.decode() # decode para desempacotar
    print("Cliente: {}".format(dados))
finally:
    sock.close()
    print("Cliente: Fechando a conexão")

