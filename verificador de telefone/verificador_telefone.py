import phonenumbers

from phonenumbers import geocoder

telefone = input("Digite um número de telefone (formato: +551140028922): ")

tel_obj = phonenumbers.parse(telefone) # Criando um objeto phone number

tel_localizacao = geocoder.description_for_number(tel_obj,"pt")

print("A localização do telefone é {}".format(tel_localizacao))