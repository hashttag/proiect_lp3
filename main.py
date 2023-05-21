import psutil
import logging

# 1.Monitorizare procent incarcare cpu / RAM
def display_usage():

    print(f"CPU: {psutil.cpu_percent(interval=1)} / RAM: {psutil.virtual_memory().percent}")

# 2.Atentionare la trecerea pragului
def check_resource_usage(cpu_limit = 50,memory_limit = 50):

    # Obținem informații despre consumul de resurse
    cpu_usage = psutil.cpu_percent(interval=0.1)
    memory_usage = psutil.virtual_memory().percent

    # Verificăm dacă limitele sunt atinse și afișăm mesaje de avertizare corespunzătoare
    if cpu_usage >= cpu_limit:
        print("Avertisment: Consumul de CPU a depășit limita de", cpu_limit, "%")

    if memory_usage >= memory_limit:
        print("Avertisment: Consumul de memorie a depășit limita de", memory_limit, "%")

# Configurare
logging.basicConfig(filename='app.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


#def check_temperature():
 #   psutil.sensors_temperatures()
  #  if psutil.sensors_temperatures()>=100:
   #     logging.ERROR('Depasire de temperatura')

while True:
    display_usage()
    check_resource_usage(10, 50)
    #check_temperature()

