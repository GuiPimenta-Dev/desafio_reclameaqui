from ...db.conn import ConnectToDatabase
from flask_restful import Resource, request
from flask_restful_swagger import swagger


class Complain(Resource, ConnectToDatabase):
    @swagger.model
    @swagger.operation(
        notes='Create a complain',
        parameters=[
            {
                "name": "title",
                "description": "Complain title",
                "required": True,
                "allowMultiple": False,
                "dataType": "string",
                "paramType": "form"
            },
            {
                "name": "description",
                "description": "Complain description",
                "required": True,
                "allowMultiple": False,
                "dataType": "string",
                "paramType": "form"
            },
            {
                "name": "locale",
                "description": "Company locale",
                "required": True,
                "allowMultiple": False,
                "dataType": "string",
                "paramType": "form"
            },
            {
                "name": "company",
                "description": "Company whose complain belongs to",
                "required": True,
                "allowMultiple": False,
                "dataType": "string",
                "paramType": "form"
            },

        ]
    )
    def post(self):

        args = request.form

        if not 'title' in args:
            return {'message': 'Complain title is required'}, 400

        elif not args['title']:
            return {'message': 'Complain title can`t be null'}, 400

        if not 'description' in args:
            return {'message': 'Complain description is required'}, 400

        elif not args['description']:
            return {'message': 'Complain description can`t be null'}, 400

        if not 'locale' in args:
            return {'message': 'Company locale is required'}, 400

        elif not args['locale']:
            return {'message': 'Company locale can`t be null'}, 400

        if not 'company' in args:
            return {'message': 'Company is required'}, 400

        elif not args['company']:
            return {'message': 'Company can`t be null'}, 400

        complain = {
            "title": args['title'],
            "description": args['description'],
            "locale": args['locale'],
            "company": args['company'],
        }

        self.collection_complains.insert(complain)

        del complain['_id']

        return {
                   'message': f'Complain {args["title"]} created successfully',
                   'data': complain
               }, 201
