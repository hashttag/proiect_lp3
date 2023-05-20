import psutil

# Definim limitele de consum pentru CPU și memorie (exprimate în procente)
cpu_limit = 30
memory_limit = 90


# Funcție pentru verificarea consumului de resurse
def check_resource_usage():
    # Obținem informații despre consumul de resurse
    cpu_usage = psutil.cpu_percent()
    memory_usage = psutil.virtual_memory().percent

    # Verificăm dacă limitele sunt atinse și afișăm mesaje de avertizare corespunzătoare
    if cpu_usage >= cpu_limit:
        print("Avertisment: Consumul de CPU a depășit limita de", cpu_limit, "%")

    if memory_usage >= memory_limit:
        print("Avertisment: Consumul de memorie a depășit limita de", memory_limit, "%")


# Executăm funcția de verificare a consumului de resurse la intervale regulate
while True:
    check_resource_usage()

