
# python3 -m venv venv 
# source venv/bin/activate

from sqlalchemy import create_engine, Engine , Connection
from pandas import DataFrame,ExcelFile
import logging as log
from typing import Dict

class Sqlite:
    def __init__(self,folder: str, subfolder:str) -> None:
        url = 'sqlite:///{folder}_{subfolder}_ana.db'.format(folder= folder,subfolder= subfolder)
        database = create_engine(url)
        self.__connection = database.connect()

    def connection(self) -> Connection:
        return self.__connection
    
        
    def initAll(self,book: ExcelFile, sheet: str)-> int:
        df = book.parse(sheet_name= sheet)
        db = self.populate(tableName= sheet,dataframe=df)
        return db        
 
                    
    def initFromFrame(self, frame : DataFrame , table: str,dataType: Dict, indexLable: str)-> int:
        
        rowCount = frame.to_sql(name=table,con=self.__connection, if_exists= 'append',dtype=dataType,index_label=indexLable)
        log.info(f'number of affecred rows: {rowCount}')          
        return rowCount

        