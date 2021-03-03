import pymongo

client = pymongo.MongoClient("mongodb+srv://test:<test>@are-you-feeling-lucky-d.0pydi.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.test