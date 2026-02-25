import logging #module standard Python pour gérer les logs
import os #pour manipuler les chemins de fichiers et dossiers
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(logs_path,exist_ok=True) #os.makedirs() pour créer le dossier logs s'il n'existe pas déjà, et exist_ok=True pour éviter une erreur si le dossier existe déjà.

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,


)

#if __name__=="__main__":
 #   logging.info("Logging has started")