from ...db.conn import ConnectToDatabase
from flask_restful import Resource
from flask_restful_swagger import swagger


class ListComplains(Resource,ConnectToDatabase):
    @swagger.model
    @swagger.operation(notes='list all complains')
    def get(self):
            objects = []
            for object in self.collection_complains.find({},{"_id":0}):
                objects.append(object)

            return {'data': objects }, 200