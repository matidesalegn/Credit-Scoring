# src/logger.py
# import logging

# def setup_logger(name='credit_scoring_logger', log_file='credit_scoring.log', level=logging.INFO):
#     handler = logging.FileHandler(log_file)        
#     handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s %(message)s'))

#     logger = logging.getLogger(name)
#     logger.setLevel(level)
#     logger.addHandler(handler)

#     return logger

import logging

def setup_logger():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger
