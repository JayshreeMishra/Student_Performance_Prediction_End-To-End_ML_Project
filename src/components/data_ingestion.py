import os
import sys
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

from src.exception import CustomException
from src.logger import logging

@dataclass
class DataIngestionConfig:      #This is a placeholder for setting up where to bring in data later
    train_data_path: str= os.path.join('artifacts', "train.csv")
    test_data_path: str= os.path.join('artifacts', "test.csv")
    raw_data_path: str= os.path.join('artifacts', "raw.csv")


class DataIngestion:
    def __init__(self):
        self.ingestion_config= DataIngestionConfig()

    def initiate_data_ingestion(self):      #code to read data from a database or location will be here
        logging.info("Entered the data ingestion method or component")
        try:
            df= pd.read_csv(r'notebook\data\stud.csv')
            logging.info("Read the data as 'df'")

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)

            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)

            logging.info("train test split initiated")
            train_set, test_set=train_test_split(df, test_size=0.3, random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)

            logging.info("Data Ingestion is completed")

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        except Exception as e:
            raise CustomException(e, sys)
        
#this is to test the data ingestion
'''
if __name__=="__main__":
    #obj= DataIngestion()
    #obj.initiate_data_ingestion()
'''

#this is to test data ingestion

from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransformationConfig

if __name__=="__main__":
    obj= DataIngestion()
    train_data, test_data= obj.initiate_data_ingestion()

    data_transformation= DataTransformation()
    data_transformation.initiate_data_transformation(train_data, test_data)