
# python3 -m venv venv 
# source venv/bin/activate

from sqlalchemy import create_engine, Engine ,Table, Column, Integer, String, MetaData, Index,Text,BINARY
from pandas import DataFrame,ExcelFile
import logging as log

class Sqlite:
    def __init__(self,folder: str, subfolder:str) -> None:
        url = 'sqlite:///ayinatu'
        if folder:
            url += '_'+ folder
        if subfolder:
            url += '_' + subfolder 
        url += '.db'       
        database = create_engine(url)
        self.database = database


    def createTable(self,sheetName: str):
        metadata = MetaData()
        if 'word'.__eq__(sheetName):
            Table(
                sheetName, metadata,
                Column('index', Integer, primary_key=True),
                Column('id', Integer),  
                Column('text', String),
                Column('meaning', Text),
                Column('voice', BINARY),
                Column('root', Integer),
                Column('type', Integer),
                Column('version', Integer),

                Index('ix_users_id', 'id'),
                Index('ix_users_text', 'text'),
                Index('ix_users_root', 'root')                                                
            )

            metadata.create_all(self.database)

        elif 'animal'.__eq__(sheetName):
            Table(
                sheetName, metadata,
                 Column('index', Integer, primary_key=True),               
                Column('id', Integer, primary_key=True),
                Column('data', BINARY),
                Column('name', Integer),

                Index('ix_image_name_id', 'name_id'),                                              
            )

            metadata.create_all(self.database)   
        else:
            pass               

            
    def initFromExcell(self,book: ExcelFile, sheet: str)-> int:
        connection = self.database.connect()
        df = book.parse(sheet_name= sheet)
        rowCount = df.to_sql(name=sheet,con= connection, if_exists= 'append') 

        log.info(f'number of affecred rows: {rowCount}')                  
        return rowCount        
 
                    
    def initFromFrame(self, frame : DataFrame , table: str)-> int:
        connection = self.database.connect()
        rowCount = frame.to_sql(name=table,con= connection, if_exists= 'append',index=False)
        log.info(f'number of affecred rows: {rowCount}')          
        return rowCount