import ipaddress # Biblioteca que facilita cálculos envolvendo IPs

ip = "192.168.1.24"

ip_obj = ipaddress.ip_address(ip)

print(ip_obj+100) # Calcula 100 endereços de IP a frente de ip_obj

ip_net = "192.168.1.0/24" # Conceitos importantes /24=CIDR e máscara de rede

rede = ipaddress.ip_network(ip_net,strict=False) # Guarda o endereço de uma rede

for ip in rede: 
    print(ip) # Impressão de cada ip possível da rede