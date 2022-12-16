from flask import Flask,Response,request
import pymongo
import json
from bson.objectid import ObjectId
from dbmoudules.database import *
app=Flask(__name__)

mycol=createConnection('Quotes','quoteInfo')# this will pass thename of db and collection to database.py which has function for creating db


# CRUD METHODS TO CREATE AN API THROUGH POSTMAN

#***************** CREATE(POST)**************
@app.route("/quotes",methods=['POST'])
def create_quote():
    quote_data={'id':request.form['id'],"quote":request.form['quote'],"authorName":request.form['authorName'],"imgUrl":request.form['imgUrl']}
    data=mycol.insert_one(quote_data)
    print("^^^^^^^^^^^^^^^^^^^^",data)
    return "quotes has been created Successfully!"



#***************** READ(GET)**************
@app.route("/quotes",methods=['GET'])
def get_quote():
    data=list(mycol.find())
    response=[]
    for dt in data:
        dt["_id"]=str(dt["_id"])
        print(dt)
        response.append(dt)
    print("#############",response)
    return {"data":response}







#***************** UPDATE(PUT)**************

@app.route("/quotes/<id>",methods=['PUT'])
def update_quote(id):
    updated_data={"$set":{'id':request.form['id'],"quote":request.form['quote'],"authorName":request.form['authorName'],"imgUrl":request.form['imgUrl']}}
    data=mycol.update_one({"_id":ObjectId(id)},updated_data)
    return "quoet has been updated!"


#***************** DELETE(DELETE)**************

@app.route("/quotes/<id>",methods=['DELETE'])
def delete_quote(id):
    data=mycol.delete_one({"_id":ObjectId(id)})
    return "quoet has been deleted!"
if __name__=="__main__":
    app.run(port=80,debug=True)