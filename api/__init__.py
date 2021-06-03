from flask import Flask
from flask_restful import Api
from flask_restful_swagger import swagger
from flask_cors import CORS

from .resources.mandatory.complain import Complain
from .resources.mandatory.count_complains import CountComplains
from .resources.extra.list_complains import ListComplains


app = Flask(__name__)
api = swagger.docs(
                   Api(app),
                   apiVersion='1.0',
                   api_spec_url='/docs',
                   description='Reclame Aqui Hard skills test assignment - created by Guilherme Alves Pimenta'
                   )
CORS(app)

# Mandatory endpoints
api.add_resource(Complain, '/complain')
api.add_resource(CountComplains, '/countcomplains')

# Extra endpoints
api.add_resource(ListComplains, '/listcomplains')


