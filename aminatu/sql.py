from sqlalchemy import create_engine, CursorResult,Connection,Engine,text,Sequence,Row,Column,Index,String,BINARY,Select,select,insert,Table
from io import BytesIO
class Query:

    def __init__(self,connection: Connection, table: Table ) -> None:
        # TODO check if connection is already established
        self.table = table
        self.connection = connection

    def insertImage(self,data: bytes,id: int,name: int):
        query = self.table.insert().values(id=id, name=name,data=data)
        self.connection.execute(query)
        self.connection.commit()

        

    def findAll(self):
        query = self.table.select()
        result = self.connection.execute(query).fetchall()
        return result   

    def queryFindText(self,param: str) -> CursorResult:
        query = text("select * from word where text = :param")
        result = self.connection.execute(query,{'param':param})
        return result       

        
    def queryFindText(self,param: str) -> CursorResult:
        query = text("select * from word where text = :param")
        result = self.connection.execute(query,{'param':param})
        return result
    
    def getRows(self,cursor: CursorResult) -> Sequence[Row]:
        return cursor.fetchall()
    
    def queryByRootId(self,text:str)  -> CursorResult:
        query = "select * from word where rootId == @text".format(text, text)
        result = self.connection.exec_driver_sql(query)
        return result
    
    def queryFindTextLike(self,text:str):
        query = "select * from words where text like  '%@text%'".format(text, text)
        result = self.connection.exec_driver_sql(query)
        return result
      
    
    def queryFindTextEndingWith(self,text: str):
        query = "select * from words where text like '@text%'".format(text, text)
        result = self.connection.exec_driver_sql(query)
        return result
    
 
    def queryFindTextStartingWith(self,text: str):
        query = "select * from words where text like '$@text'".format(text, text)
        result = self.connection.exec_driver_sql(query)
        return result
