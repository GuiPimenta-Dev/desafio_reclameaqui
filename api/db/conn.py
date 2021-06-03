import pymongo
from env_heroku import HEROKU

class ConnectToDatabase():
    if HEROKU:
        import os

        conn = pymongo.MongoClient(
                f"mongodb+srv://{os.environ['USER']}:{os.environ['PASS']}@backend.lwkqa.mongodb.net/{os.environ['DB']}?retryWrites={os.environ['RETRY']}&w=majority")

        db = conn.desafio_reclameaqui

        collection_complains = db[os.environ['COMPLAINS']]

               
    else:     
        from env import USER,PASS,DB,RETRY,COMPLAINS

        conn = pymongo.MongoClient(
            f"mongodb+srv://{USER}:{PASS}@backend.lwkqa.mongodb.net/{DB}?retryWrites={RETRY}&w=majority")

        db = conn.desafio_reclameaqui

        collection_complains = db[COMPLAINS]
