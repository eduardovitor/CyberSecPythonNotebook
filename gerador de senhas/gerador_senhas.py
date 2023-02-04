import random, string

caracteres_todos = string.ascii_letters + string.digits + "!@#$%¨&*()-+ç.,/?;:|"
caracteres_minus_numeros = string.ascii_lowercase + string.digits
caracteres_maius_simbolos = string.ascii_uppercase + "!@#$%¨&*()-+ç.,/?;:|"
caracteres_numeros = string.digits
rand_obj = random.SystemRandom()

def gerar_senha(tipo_senha,tamanho):
    if tipo_senha == 1:
        senha = ""
        for i in range(tamanho):
            senha = senha + rand_obj.choice(caracteres_todos)
        return senha
    elif tipo_senha == 2:
        senha = ""
        for i in range(tamanho):
            senha = senha + rand_obj.choice(caracteres_minus_numeros)
        return senha
    elif tipo_senha == 3:
        senha = ""
        for i in range(tamanho):
            senha = senha + rand_obj.choice(caracteres_maius_simbolos)
        return senha
    elif tipo_senha == 4:
        senha = ""
        for i in range(tamanho):
            senha = senha + rand_obj.choice(caracteres_numeros)
        return senha

tamanho = int(input("Digite o tamanho da senha: "))
tipo_senha = int(input("Tipo de senha:\n1- Letras maiúsculas e minúsculas, símbolos e números\n2- Letras minúsculas e números\n3- Letras maiúsculas e símbolos\n4- Apenas números\n"))
senha = gerar_senha(tipo_senha, tamanho)
print("A senha gerada foi {}".format(senha))