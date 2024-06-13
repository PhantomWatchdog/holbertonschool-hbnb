
from abc import ABC, abstractmethod

class IPersistenceManager(ABC):
    @abstractmethod
    def save(self, entity):
        """Save an entity to the storage."""
        pass

    @abstractmethod
    def get(self, entity_id, entity_type):
        """Retrieve an entity from the storage by its ID."""
        pass

    @abstractmethod
    def update(self, entity):
        """Update an existing entity in the storage."""
        pass

    @abstractmethod
    def delete(self, entity_id, entity_type):
        """Delete an entity from the storage by its ID."""
        pass
