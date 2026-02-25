import sys, os #it enables Python program talk directly to the Python interpreter and the operating system environment, ici il permet d’accéder directement aux flux d’erreurs et aux infos sur l’exécution. 
try:
    from .logger import logging #
except Exception:
    # fallback when running the file directly (no parent package)
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) #obtenir le chemin du projet en remontant d'un niveau à partir du fichier actuel
    if project_root not in sys.path: #ajouter le chemin du projet à sys.path pour permettre l'importation de modules depuis ce chemin
        sys.path.insert(0, project_root)
    from src.logger import logging

def error_message_detail(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info() #exc_info() the exception type, the exception value, and the traceback object : whick file which line the error has occured 
    file_name=exc_tb.tb_frame.f_code.co_filename
    #le formatage du mssh d 'erreur
    error_message="Error occured in python script name [{0}] line number [{1}] error message[{2}]".format(
     file_name,exc_tb.tb_lineno,str(error))

    return error_message

    

class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_detail=error_detail)
    
    def __str__(self):
        return self.error_message
    
#if __name__=="__main__":
#    try:
#        a=1/0
#    except Exception as e:
#        logging.info("Divide by zero error")
#        raise CustomException(e,sys)
    

#ce code sert à centraliser la gestion des erreurs dans ton projet ML. il :

    #Capture l’erreur (type, message).

    #Ajoute le contexte (dans quel fichier et à quelle ligne).

    #Formate le message pour qu’il soit clair et lisible.

    #Retourne une exception personnalisée (CustomException) qu'on va  logguer ensuite grace à logger.py