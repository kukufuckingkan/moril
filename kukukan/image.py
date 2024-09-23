from IPython.core.display import HTML
from IPython.display import HTML

BASE_PATH = "https://github.com/kukufuckingkan/mandenkan_media/raw/refs/heads/main/image/"
EXTENSION = ".jpg"



def player(numero: int, alt: str,folder: str) -> str:
    path = getPath(numero,folder)
    return  '''<img src="{}" alt="{}" width="150" height="150">'''.format(path,alt)

def playerWithDimention(numero: int, alt: str,folder: str,width: int, height: int) -> str:
    path = getPath(numero,folder)
    return  '''<img src="{}" alt="{}" width="{}" height="{}">'''.format(path,alt,width,height)

def getPath(numero: int,folder: str) -> str:
    return BASE_PATH + folder + "/" + str(numero) + EXTENSION