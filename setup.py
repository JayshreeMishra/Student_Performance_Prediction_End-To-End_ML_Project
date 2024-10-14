from setuptools import find_packages, setup    #will find all the packages in our ml app
from typing import List


HYPHEN_E_DOT= '-e .'
def get_requirements(file_path:str)->List[str]:
    """
    This function will return list of requirements
    """
    requirements=[]     # initialize an empty list to store the requirements
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()   #this will read lines in requirenments.txt
        
        # Using a list comprehension to remove the newline character (\n) from each requirement 
        # and replace it with a space to remove the newline character at the end of each line
        requirements= [req.replace("\n", "") for req in requirements]

        # Remove '-e .' and any empty strings from the list
        requirements = [req for req in requirements if req and req != HYPHEN_E_DOT]
    
    return requirements

#this setup can be considered as the meta data info about the entire project 
setup(
    name= 'Student_Performance_Prediction_End-To-End_ML_Project',
    version='0.0.1',
    author='Jayshree Mishra',
    author_email= 'jayshreemishra197@gmail.com',
    packages= find_packages(),
    install_requires= get_requirements('requirements.txt') #this will download all the packages in requirements file
)