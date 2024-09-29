import pandas as pd
from pandas import DataFrame

from pandas import ExcelFile
import io

def getFile(data: bytes) -> ExcelFile:
    try:
        file = pd.ExcelFile(data)
        return file
    except Exception as e:
        return None    


def getFrame(data: bytes) -> DataFrame:
    try:
        buffer = io.BytesIO(data)
        file = pd.read_excel(buffer)
        return file
    except Exception as e:
        return None

def getSheet(name: str, book: ExcelFile) -> DataFrame:
    df = book.parse(sheet_name= name)
    return df


def getFrameFromFile(file: ExcelFile) -> DataFrame:
    file = pd.read_excel(file)
    return file        
