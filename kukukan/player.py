#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 17:47:16 2024

@author: kukukan
"""


from IPython.core.display import HTML
from IPython.display import HTML

BASE_PATH = "https://github.com/kukufuckingkan/mandenkan_media/raw/refs/heads/main/"
FOLDER_PATH = "consonant/"
FOLDER_VOWEL = "vowel/"


def showHtml(path: str) -> str:
    return  '''<audio controls style="width:150px">
                    <source src="{}" type="audio/mpeg">
                    Your browser does not support the audio element.
                </audio>'''.format(path)

def play(filePath: str, env: str) -> str:
    path = getPath(filePath, env)

    return showHtml(path)
    



def getPath(path:str,env: str) -> str:
    PATH_RESOURCE = 'resource/'
    
    if PATH_RESOURCE in path:
        if 'DEV' == env:
            return path.replace(PATH_RESOURCE,'')
        return path
    return ''


def playFromGitt(folder: str,numero: int) -> str:
    path = BASE_PATH
    
    if folder == 'VOWEL':
        path += FOLDER_VOWEL
    
    if folder == 'CONSONANT':
        path += FOLDER_PATH
    
    path += str(numero) + ".mp3"
  
    return showHtml(path)

# if __name__=="__main__":
#     playFromGitt('VOWEL',2)
    
    
