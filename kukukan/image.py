from IPython.core.display import HTML
from IPython.display import HTML

BASE_PATH = "https://github.com/kukufuckingkan/mandenkan_media/raw/refs/heads/main/image/"
EXTENSION = ".jpg"



def player(numero: int, alt: str,folder: str) -> str:
    path = BASE_PATH + folder + "/" + str(numero) + EXTENSION
    
    return  '''<img src="{}" alt="{}" width="150" height="150">'''.format(path,alt)