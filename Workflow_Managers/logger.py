# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 20:19:58 2023

@author: David López
"""

from datetime import datetime

LOG_FILE_PATH = "logs.txt"

def logger(message):
    with open(LOG_FILE_PATH, 'a') as file:
        file.write("{date} - {message}\n".format(date = datetime.now(), message = message))
    return