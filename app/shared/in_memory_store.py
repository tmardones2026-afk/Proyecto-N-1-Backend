"""
Almacén genérico en memoria para las 4 entidades del dominio.
"""
from typing import Generic, TypeVar, Optional
from itertools import count

T = TypeVar("T")


class InMemoryStore(Generic[T]):
    def __init__(self):
        self._data: dict[int, T] = {}
        self._id_counter = count(start=1)

    def add(self, build_entity) -> T:
        new_id = next(self._id_counter)
        entity = build_entity(new_id)
        self._data[new_id] = entity
        return entity

    def get(self, entity_id: int) -> Optional[T]:
        return self._data.get(entity_id)

    def list_all(self) -> list[T]:
        return list(self._data.values())

    def update(self, entity_id: int, entity: T) -> Optional[T]:
        if entity_id not in self._data:
            return None
        self._data[entity_id] = entity
        return entity

    def delete(self, entity_id: int) -> bool:
        if entity_id not in self._data:
            return False
        del self._data[entity_id]
        return True 