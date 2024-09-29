"""
@author Ana
"""

import logging as log
import pathlib
import urllib
#pathlib.Path or py._path.local.LocalPath
from typing import Dict,Optional

from ana import http



class Git:
    
    def __init__(self,folder: str, subFolder: str) -> None:
        basePath = 'https://github.com/kukufuckingkan/mandenkanMedia/raw/refs/heads/main/'
        self.folder = folder
        self.subfolder = subFolder
        self.path = basePath + folder + '/' + subFolder + '/'
 

    # retrive all assets in the subfolder
    def retriveDirFiles(self):
        pass
    
    def retriveFile(self,asset:str, extension:str) -> bytes:
        url = self.path + asset + '.' + extension
        data = http.request(url=url)
        return data
                    


