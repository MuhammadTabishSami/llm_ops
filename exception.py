import sys

from logger import logger

def error_message_detail(error,error_detail:sys):
    _, _, esc_tb=error_detail.exc_info()
    file_name=esc_tb.tb_frame.f_code.co_filename
    error_message='Error Occurred in Python Script name [{0}] line number [{1}] error message [{2}]'.format(
        file_name,esc_tb.tb_lineno,str(error)
    )
    return error_message

#OOP(inheritance)
class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_detail)

    def __str__(self):
        return self.error_message  