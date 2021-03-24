import pymongo

client = pymongo.MongoClient("mongodb+srv://rwuser:rwuser@are-you-feeling-lucky-d.0pydi.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.test