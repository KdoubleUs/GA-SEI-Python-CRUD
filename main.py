from flask import Flask, jsonify, request
from peewee import * 
import datetime
from playhouse.shortcuts import model_to_dict,dict_to_model
db = PostgresqlDatabase('contact', user='kdoubleu', password='', host='localhost', port=5432, autorollback=True )
db.connect()


class BaseModel(Model): 
    class Meta: 
        database = db 


class Contact(BaseModel): 
    first_name = CharField()
    last_name = CharField()
    birthday = DateField()
    phone_number= CharField() 
    email= CharField()
    
db.drop_tables([Contact])
db.create_tables([Contact])

eric = Contact(first_name='eric', last_name='lee', birthday=datetime.date(2000,4,12), phone_number="1233124", email='ericlee192@gmail.com' )
eric.save()
kevin = Contact(first_name='kevin', last_name='wu', birthday=datetime.date(1993,10,9), phone_number="3949123", email='kdoubleus123@gmail.com' )
kevin.save()

list_of_contact = Contact.select()
print([list_of_contact.first_name for list_of_contact in list_of_contact])



app = Flask(__name__)
@app.route('/')
def index(): 
    return "hello world"

@app.route('/contact/<id>', methods=['GET'])
def getContact(id=None):
    if(request.method == "GET"): 
        if(id): 
            return jsonify(model_to_dict(Contact.get(Contact.id == id )))
        else: 
            return "cannot find any contact"
    
@app.route('/contact/create', methods=['POST'])
def createContact(): 
    newContact = dict_to_model(Contact, request.get_json())
    newContact.save()
    return jsonify({"success":True})



@app.route('/contact/<id>', methods=['DELETE'])
def deleteContact(id=None): 
    if(Contact.id == id):
        Contact.delete().where(Contact.id == id)
        return f"delete contact with {id}"


    
if __name__ == '__main__':    
    app.run(host='localhost', port=9000, debug=True, )
#contact book 