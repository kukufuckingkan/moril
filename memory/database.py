
# python3 -m venv venv 
# source venv/bin/activate

from sqlalchemy import create_engine, Engine , Connection
from pandas import DataFrame,ExcelFile
from typing import Dict
import logging as log

class Sqlite:
    def __init__(self,folder: str, subfolder:str) -> None:
        url = 'sqlite:///{folder}_{subfolder}_ana.db'.format(folder= folder,subfolder= subfolder)
        database = create_engine(url)
        self.__connection = database.connect()

    def connection(self) -> Connection:
        return self.__connection
    
        
    def initAll(self,book: ExcelFile, sheet: str)-> int | None:
        sheetNames = book.sheet_names
        
        log.info(f'Sheet names: {sheetNames}')
        for sheetName in book.sheet_names:
            capSheetName = sheetName.upper()
            if 'english'.__eq__(sheet.casefold()):
                match capSheetName:
                    case 'WORD':
                        df = book.parse(sheet_name= sheetName)
                        db = self.populate(tableName= sheetName,dataframe=df)
                        return db
                    case _:
                        return
            elif 'ߒߞߏ'.__eq__(sheet.casefold()):
                match capSheetName:
                    case 'WORD':
                        df = book.parse(sheet_name= sheetName)
                        return self.populate(tableName= sheetName,dataframe=df)
                    case _:
                        return  
                    
    def initFromFrame(self, frame : DataFrame , table: str)-> int | None:
        db = self.populate(tableName= table,dataframe= frame)
        return db
    
    def initFromExcel(self, file : ExcelFile , table: str)-> int | None:
        
        return 
        

                    

    def populate(self,dataframe: DataFrame,tableName: str) -> (int | None):
        # todo add indexes
        rowCount = dataframe.to_sql(name=tableName,con=self.__connection, if_exists= 'replace')
        log.info(f'number of affecred rows: {rowCount}')        
        
        return rowCount,tableName                    