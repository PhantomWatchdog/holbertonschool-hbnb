from Persistence.IPersistenceManager import IPersistenceManager
from Model.User import User
from Model.Place import Place
from Model.Review import Review
from Model.Amenity import Amenity
from Model.Country import Country
from Model.City import City

class DataManager(IPersistenceManager):
    def __init__(self):
        self.storage = {
            User: {},
            Place: {},
            Review: {},
            Amenity: {},
            Country: {},
            City: {}
        }

    def save(self, entity):
        entity_class = type(entity)
        if entity_class not in self.storage:
            raise ValueError(f"Unsupported entity type: {entity_class}")
        
        entity_id = self._get_entity_id(entity)
        self.storage[entity_class][entity_id] = entity

    def get(self, entity_id, entity_type):
        if entity_type not in self.storage:
            raise ValueError(f"Unsupported entity type: {entity_type}")
        return self.storage[entity_type].get(entity_id, None)

    def update(self, entity):
        entity_class = type(entity)
        if entity_class not in self.storage:
            raise ValueError(f"Unsupported entity type: {entity_class}")
        
        entity_id = self._get_entity_id(entity)
        if entity_id in self.storage[entity_class]:
            self.storage[entity_class][entity_id] = entity
        else:
            raise ValueError(f"Entity not found: {entity_id}")

    def delete(self, entity_id, entity_type):
        if entity_type not in self.storage:
            raise ValueError(f"Unsupported entity type: {entity_type}")
        if entity_id in self.storage[entity_type]:
            del self.storage[entity_type][entity_id]
        else:
            raise ValueError(f"Entity not found: {entity_id}")

    def _get_entity_id(self, entity):
        if isinstance(entity, User):
            return entity.user_id
        elif isinstance(entity, Place):
            return entity.place_id
        elif isinstance(entity, Review):
            return entity.review_id
        elif isinstance(entity, Amenity):
            return entity.amenity_id
        elif isinstance(entity, Country):
            return entity.country_id
        elif isinstance(entity, City):
            return entity.city_id
        else:
            raise ValueError(f"Unsupported entity type: {type(entity)}")
