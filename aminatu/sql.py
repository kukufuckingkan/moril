from sqlalchemy import create_engine, CursorResult,Connection,Engine,text,Sequence,Row,Column,Index,String,BINARY,Select,select,insert
from io import BytesIO
class Query:

    def __init__(self,connection: Connection, table: str) -> None:
        # TODO check if connection is already established
        self.table = table
        self.connection = connection

    def insertImage(self,data: BytesIO,id: int,name: int):
        query = insert(table=self.table).values(id=id, name=name,data=data)
        self.connection.execute(query)

    def findAll(self):
        query = select('*').select_from(text(self.table))
        #query = select(text(self.table))
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
