import os
from flask_sqlalchemy import SQLAlchemy
from Persistence.IPersistenceManager import IPersistenceManager
from Model.User import User
from Model.Place import Place
from Model.Review import Review
from Model.Amenity import Amenity
from Model.Country import Country
from Model.City import City

db = SQLAlchemy()

class DataManager(IPersistenceManager):
    def __init__(self):
        self.use_database = os.getenv('USE_DATABASE', 'False') == 'True'
        if not self.use_database:
            self.storage = {
                User: {},
                Place: {},
                Review: {},
                Amenity: {},
                Country: {},
                City: {}
            }

    def save(self, entity):
        if self.use_database:
            db.session.add(entity)
            db.session.commit()
        else:
            entity_class = type(entity)
            if entity_class not in self.storage:
                raise ValueError(f"Unsupported entity type: {entity_class}")
            
            entity_id = self._get_entity_id(entity)
            self.storage[entity_class][entity_id] = entity

    def _get_entity_id(self, entity):
        # Assuming each entity has an 'id' attribute
        return getattr(entity, 'id', None)