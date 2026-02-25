import os
import sys
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

try:
    # when executed as part of the package (recommended)
    from ..exception import CustomException
    from ..logger import logging
except Exception:
    # fallback when running the file directly (no parent package)
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
    if project_root not in sys.path:
        sys.path.insert(0, project_root)
    from src.exception import CustomException
    from src.logger import logging
@dataclass #dataclass est un décorateur qui permet de créer des classes de données (data classes) de manière plus concise et lisible au lieu de devoir écrire manuellement les méthodes d'initialisation, de représentation, etc. pour chaque classe.
            #we use dataclass when we define juse variables in a class but we have other function inside the clas we better go with normal class (__init__ method)
class DataIngestionConfig: #DataIngestionConfig est une classe de configuration pour lingestion de données.
                            #elle dit au script ou trouver les données d'entrée et ou les stocker après le traitement.
    train_data_path: str=os.path.join('artifacts',"train.csv")#construction du path pour un artifact folder qui est ici train.csv
    test_data_path: str=os.path.join('artifacts',"test.csv")
    raw_data_path: str=os.path.join('artifacts',"data.csv")
    #these are the inputs of dataingestion componen and now it knows very well ou stocker l'input et l'output de train

class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()#

    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component")
        try:
            csv_path = os.path.join('notebook', 'data', 'stud.csv')
            df = pd.read_csv(csv_path)
            logging.info('Read the dataset as dataframe')

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)

            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)#.to_csv() pour enregistrer le DataFrame df dans un fichier CSV à l'emplacement spécifié par self.ingestion_config.raw_data_path. index=False pour ne pas inclure les index du DataFrame dans le fichier CSV, et header=True pour inclure les noms des colonnes comme en-tête dans le fichier CSV.

            logging.info("Train test split initiated")
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)

            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            logging.info("Inmgestion of the data iss completed")

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path

            )
        except Exception as e:
            raise CustomException(e,sys)
        
if __name__=="__main__":
    obj=DataIngestion()
    train_data,test_data=obj.initiate_data_ingestion()

    #data_transformation=DataTransformation()
    #train_arr,test_arr,_=data_transformation.initiate_data_transformation(train_data,test_data)

    #modeltrainer=ModelTrainer()
    #print(modeltrainer.initiate_model_trainer(train_arr,test_arr))