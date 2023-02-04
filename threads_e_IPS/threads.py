from threading import Thread
import time

def carro(velocidade, modelo):
    trajeto = 0
    vel_max = 100
    while(trajeto<=vel_max):
        time.sleep(0.8)
        print(f"O modelo do carro é {modelo} e o KM é {trajeto} \n")
        trajeto += velocidade


thread_carro1 = Thread(target=carro, args=[5,"Honda Civic"])
thread_carro2 = Thread(target=carro, args=[10, "Porsche 911"])

thread_carro1.start()
thread_carro2.start()