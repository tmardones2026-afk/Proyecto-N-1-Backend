"""
Router de Sala: define las URIs y delega la lógica al service.
"""
from fastapi import APIRouter, status

from app.schemas.dtos import SalaCreate, SalaOut
from app.services import sala_service

router = APIRouter(prefix="/salas", tags=["Salas"])


@router.post("", response_model=SalaOut, status_code=status.HTTP_201_CREATED)
def crear_sala(data: SalaCreate):
    return sala_service.crear_sala(data)


@router.get("", response_model=list[SalaOut])
def listar_salas():
    return sala_service.listar_salas()


@router.get("/{sala_id}", response_model=SalaOut)
def obtener_sala(sala_id: int):
    return sala_service.obtener_sala(sala_id)


@router.put("/{sala_id}", response_model=SalaOut)
def actualizar_sala(sala_id: int, data: SalaCreate):
    return sala_service.actualizar_sala(sala_id, data)


@router.delete("/{sala_id}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_sala(sala_id: int):
    sala_service.eliminar_sala(sala_id)