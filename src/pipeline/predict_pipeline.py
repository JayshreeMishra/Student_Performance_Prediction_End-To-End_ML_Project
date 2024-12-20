import sys
import pandas as pd
from src.exception import CustomException
from src.utils import load_object

class PredictPipeline:
    def __init(self):
        pass

    def predict(self, features):
        try:
            model_path=r'artifacts\model.pkl'
            preprocessor_path= r'artifacts\preprocessor.pkl'
            model= load_object(file_path= model_path)
            preprocessor= load_object(file_path= preprocessor_path)

            #transform features using preprocessor
            data_scaler= preprocessor.transform(features)
            preds= model.predict(data_scaler)
            
            #To ensure that the predicted math score does not exceed 100
            capped_preds= [min(pred, 100) for pred in preds]

            return capped_preds
        except Exception as e:
            raise CustomException(e, sys)


class CustomData:
    def __init__(self,
                 gender: str,
                 race_ethnicity: str,
                 parental_level_of_education: str,
                 lunch: str,
                 test_preparation_course: str,
                 reading_score: int,
                 writing_score: int):
        
        #Validate that input scores do not exceed 100
        if reading_score>100 or writing_score>100:
            raise ValueError("Reading and Writing scores must be 100 or below.")
        
        self.gender= gender
        self.race_ethnicity= race_ethnicity
        self.parental_level_of_education= parental_level_of_education
        self.lunch= lunch
        self.test_preparation_course= test_preparation_course
        self.reading_score= reading_score
        self.writing_score= writing_score

    
    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict = {
                "gender": [self.gender],
                "race_ethnicity": [self.race_ethnicity],
                "parental_level_of_education": [self.parental_level_of_education],
                "lunch": [self.lunch],
                "test_preparation_course": [self.test_preparation_course],
                "reading_score": [self.reading_score],
                "writing_score": [self.writing_score]
            }

            return pd.DataFrame(custom_data_input_dict)
        
        except Exception as e:
            raise CustomException(e, sys)