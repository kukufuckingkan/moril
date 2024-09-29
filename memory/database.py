
# python3 -m venv venv 
# source venv/bin/activate

from sqlalchemy import create_engine, Engine , Connection
from pandas import DataFrame,ExcelFile
import logging as log

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
 
                    
    def initFromFrame(self, frame : DataFrame , table: str)-> int:
        db = self.populate(tableName= table,dataframe= frame)
        return db
    
    def initFromExcel(self, file : ExcelFile , table: str)-> int:
        
        return 
        

                    

    def populate(self,dataframe: DataFrame,tableName: str) -> int:
        # todo add indexes
        rowCount = dataframe.to_sql(name=tableName,con=self.__connection, if_exists= 'replace')
        log.info(f'number of affecred rows: {rowCount}')        
        
        return rowCount,tableName                    