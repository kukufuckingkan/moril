#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 17:47:16 2024

@author: kukukan
"""


from IPython.core.display import HTML
from IPython.display import HTML


def play(filePath: str, env: str) -> str:
    path = getPath(filePath, env)

    # HTML for the audio player without newlines
    audio_html = '''<audio controls style="width:150px">
                      <source src="{}" type="audio/mpeg">
                      Your browser does not support the audio element.
                    </audio>'''.format(path)
    
    return audio_html


def getPath(path:str,env: str) -> str:
    PATH_RESOURCE = 'resource/'
    
    if PATH_RESOURCE in path:
        if 'DEV' == env:
            return path.replace(PATH_RESOURCE,'')
        return path
    return ''

    