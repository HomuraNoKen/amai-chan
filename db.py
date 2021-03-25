import pymongo

client = pymongo.MongoClient("mongodb+srv://rwuser:rwuser@are-you-feeling-lucky-c.ar5dn.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client["db01"]

def add_channel_id(channel_id:str, channel_name:str):
    collection = db.channel_id
    if collection.count() < 1:
        inp_file = {
            "id":1,
            "channel_id":channel_id,
            "channel_name":channel_name
        }

        collection.insert_one(inp_file)

    else:
        temp = collection.find_one({"id":1})
        if temp["channel_id"] == channel_id:
            return False
        replaced_file = {
            "id":1,
            "channel_id":channel_id,
            "channel_name":channel_name
        }
        collection.update({"id":1},replaced_file)

    return True