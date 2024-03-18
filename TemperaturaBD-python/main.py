import random
import threading
import time
from pymongo import MongoClient

# Configuração do cliente MongoDB
client = MongoClient('localhost', 27017)
db = client.bancoiot
sensores_col = db.sensores


# Função para simular os sensores
def simular(nome_sensor):
    global sensores_col
    aux = False
    while not aux:
        temperatura = random.randint(30, 40)
        sensorAlarmado = temperatura > 38
        print(f"{nome_sensor}: {temperatura}C°")


        sensores_col.update_one({"nomeSensor": nome_sensor}, {
            "$set": {"valorSensor": temperatura, "sensorAlarmado": sensorAlarmado, "unidadeMedida": "C°"}})

        if sensorAlarmado:
            print(f"Atenção! Temperatura muito alta! Verificar {nome_sensor}!")
            break

        time.sleep(5)


th1 = threading.Thread(target=simular, args=("Temp1",))
th2 = threading.Thread(target=simular, args=("Temp2",))
th3 = threading.Thread(target=simular, args=("Temp3",))

th1.start()
th2.start()
th3.start()
