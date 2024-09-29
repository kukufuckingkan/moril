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
    
    def retriveFile(self,asset:None| str, extension) -> bytes:
        url = self.path + asset + '.' + extension

        if self.folder == 'dictionary':
            match self.subfolder:
                case 'english':
                    data = http.request(url=url)
                    return data              
                case 'ߣߞߏ':
                    return None
                case _:
                    return None
                
        # subfolder is image
        else:
            match self.subfolder:
                case 'animal':
                    if asset and extension:
                        data = http.request(url=url)
                        return data
                    


