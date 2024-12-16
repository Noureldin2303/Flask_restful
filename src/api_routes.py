from src import api
from src.controller import getRecords, getSingleRecord

# Routes
api.add_resource(getRecords, "/api/")
api.add_resource(getSingleRecord, "/api/<int:id>")
