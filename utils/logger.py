"""Simple logging module"""
import logging
import sys

def log(system_handeler:sys,file_handler:str)->logging.Logger:
    """
    ## Args: system_handler = Describe system where you want to print message like (```sys.stdout```)
    ## Args2: file_handler = Describe file as string value where you want to print message like (```example.log```)
    """
    # create the logger varribale 
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    # creat hadelers 
    system_handler_var = logging.StreamHandler(system_handeler)
    file_handler_var = logging.FileHandler(file_handler)
    # create formate type
    formatte = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    # use the formate in the handelers
    system_handler_var.setFormatter(formatte)
    file_handler_var.setFormatter(formatte)
    logger.addHandler(system_handler_var)
    logger.addHandler(file_handler_var)
    # retrun logger
    return logger









