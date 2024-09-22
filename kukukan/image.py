from IPython.core.display import HTML
from IPython.display import HTML

BASE_PATH = "https://github.com/kukufuckingkan/mandenkan_media/raw/refs/heads/main/image/"
EXTENSION = ".jpg"


def showHtml(numero: int, name: str) -> str:

    def getPathFromGit(numero: int) -> str:
        return BASE_PATH + str(numero) + EXTENSION
    
    path = getPathFromGit(numero)
    return  '''<img src="{}" alt="{}" width="150" height="150">'''.format(path,name)
