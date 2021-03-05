import pymongo
import config
import discord

client = pymongo.MongoClient("mongodb+srv://test:<test>@are-you-feeling-lucky-d.0pydi.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.test

serverID = db.serverID

serverID_data = {
    "server_name": ,
    "server_id": 
}