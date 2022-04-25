from peewee import * 
db = PostgresqlDatabase('book', user='kdoubleu', password='', host='localhost', port=4321 )
db.connect()

class BaseModel(Model): 
    class Meta: 
        database = db 


class Book(BaseModel): 
    first_name = CharField()
    last_name = CharField()
    birthday = CharField()
    phone_number= IntegerField() 
    email= CharField()
    

db.create_tables('Contact')

#contact book 