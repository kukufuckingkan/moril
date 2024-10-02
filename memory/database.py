
# python3 -m venv venv 
# source venv/bin/activate

from sqlalchemy import create_engine, Engine ,Table, Column, Integer, String, MetaData, Index,Text,BINARY
from pandas import DataFrame,ExcelFile
import logging as log


class Sqlite:
    def __init__(self,database_name: str) -> None:
        url = 'sqlite:///{}'.format(database_name)   
        database = create_engine(url)
        self.database = database


    def getTable(self,name: str) -> Table:
        metadata = MetaData()
        if 'word'.__eq__(name):
            table = Table(
                name, metadata,
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
            return table
        elif 'animal'.__eq__(name):
            table = Table(
                name, metadata,
                 Column('index', Integer, primary_key=True),               
                Column('id', Integer),
                Column('data', BINARY),
                Column('name', Integer),

                Index('ix_image_id', 'id'),
                Index('ix_image_name_id', 'name'),                                              
            )
            return table
        



    def createTable(self,name: str):
        table = self.getTable(name)
        table.metadata.create_all(self.database)
                         
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