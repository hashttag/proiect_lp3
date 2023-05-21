import logging

#Configurare
logging.basicConfig(filename='app.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

#Exemple
logging.info('Depasire de temperatura')
logging.warning(' Dispozitivul a depasit limita')
logging.error('Eroare')