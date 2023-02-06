import hashlib

menu = '''Calculador de hashes de uma string
1) MD5
2) SHA1
3) SHA256
4) SHA512          
'''
print(menu)
string = input("Digite a string a ser usada na geração do hash: ")
op = int(input("Digite a opção de algoritmo de hash (1, 2, 3 ou 4): "))

if op == 1:
    hash_md5 = hashlib.md5(string.encode("utf-8"))
    print("O hash md5 gerado foi {}".format(hash_md5.hexdigest()))

elif op == 2:
    hash_sha1 = hashlib.sha1(string.encode("utf-8"))
    print("O hash sha1 gerado foi {}".format(hash_sha1.hexdigest()))

elif op == 3:
    hash_sha256 = hashlib.sha256(string.encode("utf-8"))
    print("O hash sha256 gerado foi {}".format(hash_sha256.hexdigest()))

elif op == 4:
    hash_sha512 = hashlib.sha512(string.encode("utf-8"))
    print("O hash sha512 gerado foi {}".format(hash_sha512.hexdigest()))
    
else:
    print("Opção digitada é inválida, tente novamente")

