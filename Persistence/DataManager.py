import os
from flask_sqlalchemy import SQLAlchemy
from Persistence.IPersistenceManager import DataManager
from Model.User import User
from Model.Place import Place
from Model.Review import Review
from Model.Amenity import Amenity
from Model.Country import Country
from Model.City import City

db = SQLAlchemy()

class ConcreteDataManager(DataManager):
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
    
    def delete(self, entity):
        if self.use_database:
            db.session.delete(entity)
            db.session.commit()
        else:
            entity_class = type(entity)
            entity_id = self._get_entity_id(entity)
            if entity_id in self.storage[entity_class]:
                del self.storage[entity_class][entity_id]

    def get(self, entity_class, entity_id):
        if self.use_database:
            return entity_class.query.get(entity_id)
        else:
            if entity_id in self.storage[entity_class]:
                return self.storage[entity_class][entity_id]
            return None
    
    def get_all(self, entity_class):
        if self.use_database:
            # Retourne tous les enregistrements de la base de données pour l'entité spécifiée
            return entity_class.query.all()
        else:
            # Vérifie si l'entité est présente dans le stockage en mémoire
            if entity_class in self.storage:
                # Retourne toutes les instances de l'entité stockées en mémoire
                return list(self.storage[entity_class].values())
            else:
                # Retourne une liste vide si l'entité n'est pas trouvée
                return []

    def update(self, entity):
        if self.use_database:
            db.session.commit()
        else:
            entity_class = type(entity)
            entity_id = self._get_entity_id(entity)
            if entity_id in self.storage[entity_class]:
                self.storage[entity_class][entity_id] = entity