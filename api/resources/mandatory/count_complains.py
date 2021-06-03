from ...db.conn import ConnectToDatabase
from flask_restful import Resource, request
# from ...constants.status import StatusEnum
from flask_restful_swagger import swagger


class CountComplains(Resource, ConnectToDatabase):
    @swagger.model
    @swagger.operation(
        notes='Count how many complains a specific company has in specific city',
        parameters=[
            {
                "name": "company",
                "description": "Company whose complain belongs to",
                "required": True,
                "allowMultiple": False,
                "dataType": "string",
                "paramType": "query"
            },
            {
                "name": "locale",
                "description": "City where company is located",
                "required": True,
                "allowMultiple": False,
                "dataType": "string",
                "paramType": "query"
            },
        ]
    )
    def get(self):

        if not request.args:
            return {"message": 'Query params missing'}, 400

        if 'company' not in request.args:
            return {'message': 'Company is required'}, 400

        if 'locale' not in request.args:
            return {'message': 'Company locale is required'}, 400

        complains_count = self.collection_complains.count_documents(
            {'company': request.args['company'], 'locale': request.args['locale']})

        return {

                   'company': request.args['company'],
                   'locale': request.args['locale'],
                   'complains_count': complains_count

               }, 200
