import logging
import os
from datetime import datetime
from logging.handlers import RotatingFileHandler

# Directory for log files to be saved
log_dir=os.path.join(os.getcwd(),'logs')
os.makedirs(log_dir,exist_ok=True)

# files to be added in above directory
log_file=f'{datetime.now().strftime('%m_%d_%Y_%H_%M_S')}.log'
log_file_path=os.path.join(log_dir,log_file)

#creating logger
logger=logging.getLogger()
logger.setLevel(logging.INFO)

# Creating a rotating file handler
## reduce the size of logging file
file_handler = RotatingFileHandler(log_file_path,maxBytes=10*1024*1024,backupCount=5)
file_handler.setLevel(logging.INFO)

console_handler=logging.StreamHandler()
console_handler.setLevel(logging.INFO)

formatter=logging.Formatter('%(asctime)s-%(levelname)s-%(message)s')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(console_handler)

if __name__=="__main__":
    logger.info('Log file testing')