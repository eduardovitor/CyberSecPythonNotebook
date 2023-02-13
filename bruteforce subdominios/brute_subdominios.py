import dns.resolver

res = dns.resolver.Resolver()
subdominios = open("subdominios.txt","r").read().splitlines()
alvo = "bancocn.com"

try:
    for subdominio in subdominios:
        sub_alvo = "{}.{}".format(subdominio,alvo)
        resultado = res.resolve(sub_alvo)
        for r in resultado:
            print("{} -> {}".format(sub_alvo,r))
except:
    pass