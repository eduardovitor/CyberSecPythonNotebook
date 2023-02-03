import socket
import sys # Usada para acessar funções do interpretador Python


def main():
    # Criação de socket para comunicação
    try:
        sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)
        # socket.AF_INET: socket da família de protocolos IP
        # socket.SOCK_STREAM: socket para comunicação TCP
        # 0: protocolo de comunicação TCP
    except socket.error as e:
        print("A criação do socket foi mal-sucedida")
        print("O erro foi: {}".format(e))
        sys.exit()
    print("Criação de socket bem-sucedida")

    # Estabelecimento de conexão
    try:
        host = input("Digite o host ou ip: ")
        porta = input("Digite a porta: ")
        sock.settimeout(30)
        sock.connect((host,int(porta)))

    except socket.error as e:
        print("A conexão foi mal-sucedida no host: {}, porta: {}".format(host,porta))
        print("O erro foi: {}".format(e))
        sys.exit()
    print("A conexão foi bem-sucedida no host: {}, porta: {}".format(host,porta))

if __name__ == "__main__": # Executando a função criada como a principal do programa
    main()