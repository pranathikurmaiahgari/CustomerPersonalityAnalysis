import sys
from src.logger import logging

def error_message_detail(error,error_detail:sys):
    _,_,exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename

    error_message = "Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )

    return error_message

class CustomException(Exception):
    
    def _init_(self, error_message, error_detail:sys):
        super()._init_(error_message)
        self.error_message = error_message_detail(error_message, error_detail=error_detail)

    def _str_(self):
        return self.error_message  
    

if __name__=="main_":
    logging.info("Logging has started")

    try:
        a=1/0
    except Exception as e:
        logging.info('Division by zero') 
        raise CustomException(e,sys)