"""
@author Ana
"""

import logging as log
import pathlib
import urllib
from typing import Dict,Optional
from io import BytesIO
from ana import http



class Git:
    
    def __init__(self,folder: str, subFolder: str) -> None:
        self.path = 'https://github.com/kukufuckingkan/mandenkanMedia/raw/refs/heads/main/'
    
        if folder:
            self.path += folder + '/'
        if subFolder:
            self.path += subFolder + '/'    
 

    # retrive all assets in the subfolder
    def retriveDirFiles(self):
        pass
    
    def retriveFile(self,asset:str, extension:str) -> BytesIO:
        url = self.path + asset + '.' + extension
        data = http.request(url=url)
        return data
                    


