import pymongo
#step1 connection to client:URL

local_url="mongodb://localhost:27017/"
remote_url="mongodb+srv://Rafaljawad:rootroot@cluster0.4li9lly.mongodb.net/?retryWrites=true&w=majority"
# my_client=pymongo.MongoClient(remote_url)
# print(client.list_database_names())
mycol=None
def createConnection(name,colName):
    myclient=pymongo.MongoClient(remote_url)
    mydb=myclient[name]
    try:
        if name in myclient.list_database_names():
            try:
                if colName in mydb.list_collection_names():
                    global mycol
                    mycol=mydb[colName]
                else:
                    raise Exception("collection not found")
            except Exception as e:
                print(e)
        else:
            raise Exception("given Db name not found")
    except Exception as e:
        print(e)
    return mycol 