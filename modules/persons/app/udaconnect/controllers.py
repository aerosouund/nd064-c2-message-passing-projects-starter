from datetime import datetime

from app.udaconnect.models import Person
from app.udaconnect.schemas import (
    PersonSchema,
)
from app.udaconnect.services import PersonService
from flask import request, g
from flask_accepts import accepts, responds
from flask_restx import Namespace, Resource
from typing import Optional, List
import logging

DATE_FORMAT = "%Y-%m-%d"

api = Namespace("UdaConnect", description="Connections via geolocation.")  # noqa


# TODO: This needs better exception handling


@api.route("/persons")
class PersonsResource(Resource):
    @accepts(schema=PersonSchema)
    @responds(schema=PersonSchema)
    def post(self) -> Person:
        payload = request.json
        kafka_producer = g.kafka_producer
        kafka_producer.send("persons", payload)
        return payload

    @responds(schema=PersonSchema, many=True)
    def get(self) -> List[Person]:
        persons: List[Person] = PersonService.retrieve_all()
        return persons


@api.route("/persons/<person_id>")
@api.param("person_id", "Unique ID for a given Person", _in="query")
class PersonResource(Resource):
    @responds(schema=PersonSchema)
    def get(self, person_id) -> Person:
        person: Person = PersonService.retrieve(person_id)
        return person

