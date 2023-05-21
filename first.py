# Importing the library
import psutil
import os

# Calling psutil.cpu_precent() for 4 seconds
print('The CPU usage is: ', psutil.cpu_percent(4))

# Getting loadover15 minutes
load1, load5, load15 = psutil.getloadavg()
cpu_usage = (load15 / os.cpu_count()) * 100


# Getting % usage of virtual_memory ( 3rd field)
print('RAM memory % used:', psutil.virtual_memory()[2])
# Getting usage of virtual_memory in GB ( 4th field)
print('RAM Used (GB):', psutil.virtual_memory()[3]/1000000000)
