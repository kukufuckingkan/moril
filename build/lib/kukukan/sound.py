#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 17:47:16 2024

@author: kukukan
"""


from IPython.core.display import HTML
from IPython.display import HTML

BASE_PATH = "https://github.com/kukufuckingkan/mandenkan_media/raw/refs/heads/main/sound/"
EXTENSION = ".mp3"



def player(numero: int, alt: str,folder: str) -> str:
    path = BASE_PATH + folder + "/" + str(numero) + EXTENSION

    return  '''<audio controls style="width:150px">
                    <source src="{}" type="audio/mpeg">
                </audio>'''.format(path) 
    



    
    
