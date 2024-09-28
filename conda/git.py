"""
@author Ana
"""

import logging as log
import pathlib
import urllib
#pathlib.Path or py._path.local.LocalPath
from typing import Dict,Optional,overload

from ana import http



class Git:
    
    def __init__(self,str,folder: str, subFolder: str) -> None:
        basePath = 'https://github.com/kukufuckingkan/mandenkanMedia/raw/refs/heads/main/'
        self.folder = folder
        self.subfolder = subFolder
        self.path += basePath + folder + '/' + subFolder
 

    # retrive all assets in the subfolder
    @overload
    def retrive(self):
        pass
    
    @overload
    def retrive(self,assetName:None| str, extension) -> bytes:
        path = self.path + assetName + '.' + extension

        if self.folder == 'dictionary':
            match self.subfolder:
                case 'english':
                    url += assetName + '.' + extension
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
                    if assetName and extension:
                        url += assetName + '.' + extension
                        data = http.request(url=url)
                        return data
                    


