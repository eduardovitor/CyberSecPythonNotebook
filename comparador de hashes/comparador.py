import hashlib

arq1 = "arq1.txt"
arq2 = "arq2.txt"

arq1_bin = open(arq1,"rb").read()
arq2_bin = open(arq2,"rb").read()

hash1 = hashlib.new("sha256") 

hash1.update(arq1_bin) # Atualizando o hash passando o conteúdo do arquivo em binário

hash2 = hashlib.new("sha256") 

hash2.update(arq2_bin) # Atualizando o hash passando o conteúdo do arquivo em binário

if hash1.digest() == hash2.digest(): # Método digest retorna o hash em bytes
    print("Os arquivos são iguais")
    print(f"O hash foi {hash1.hexdigest()}") 
    # Uso diferente do format e da função hexdigest que retorna o hash em string
else:
    print("Os arquivos são diferentes")
    print(f"O hash do arquivo 1 foi {hash1.hexdigest()}") 
    print(f"O hash do arquivo 2 foi {hash2.hexdigest()}")