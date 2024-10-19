import sys
from logger import logging

def error_message_detail(error, error_detail:sys):
    # Unpacking the exception information
    # We're only interested in the traceback object (exc_tb)
    _, _, exc_tb = error_detail.exc_info()        #the variable exc_tb will provide in which and line the exception has occured

    # Get the filename where the exception occurred
    file_name = exc_tb.tb_frame.f_code.co_filename
    
    # Format the error message with filename, line number, and error description
    error_message = "Error occurred in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )

    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_detail:sys):
        # Call the parent class (Exception) constructor
        super().__init__(error_message)
        
        # Create a detailed error message using the error_message_detail function
        self.error_message = error_message_detail(error_message, error_detail=error_detail)

    def __str__(self):
        # Return the formatted error message when the exception is converted to a string
        return self.error_message
    

#this is to test if exceptions are working or not
#if __name__=="__main__":

    #try:
        #a=1/0

    #except Exception as e:
        #logging.error("An error occurred: {}".format(str(e)))
        #raise CustomException(e, sys)