# Proyecto N1 Desarrollo de Backend

API REST para gestión de reservas de salas.

## Entidades
| Entidad | Descripción |
|---------|-------------|
| **Sala** | Espacio disponible para ser reservado |
| **Usuario** | Persona que realiza reservas |
| **Reserva** | Asocia un usuario con una sala. Al crearla se valida que la sala y el usuario existan |
| **Equipamiento** | Recursos disponibles, con un estado que puede actualizarse |

## Requisitos
- Python 3.10 o superior
- Git

## Instalación
1. Clonar el repositorio #usando "git clone ("AQUI VA LA URL O LINK DEL REPOSITORIO")" o poder desplazarte y clonar en un archivo especifico usando cd
2. Crear y activar entorno virtual # python: -m venv venv # Windows: venv\Scripts\activate # Linux / Mac: source venv/bin/activate
3. `pip install -r requirements.txt` #con esto se instalan las dependencias, que en el requirements como dice, estan lo necesario para esto.

## Ejecución
ya con un entorno virtual 
`uvicorn app.main:app --reload`
el servidor quedara disponible en http://127.0.0.1:8000 

Documentación Swagger: http://127.0.0.1:8000/docs

## Endpoints principales
### Salas

| Método | Ruta | Descripción |
|--------|------|-------------|
| POST | `/salas` | Crear una sala |
| GET | `/salas` | Listar todas las salas |
| GET | `/salas/{sala_id}` | Obtener una sala por ID |
| PUT | `/salas/{sala_id}` | Actualizar una sala |
| DELETE | `/salas/{sala_id}` | Eliminar una sala |

### Usuarios

| Método | Ruta | Descripción |
|--------|------|-------------|
| POST | `/usuarios` | Crear un usuario |
| GET | `/usuarios` | Listar todos los usuarios |
| GET | `/usuarios/{usuario_id}` | Obtener un usuario por ID |

### Reservas

| Método | Ruta | Descripción |
|--------|------|-------------|
| POST | `/reservas` | Crear una reserva (valida que existan la sala y el usuario) |
| GET | `/reservas` | Listar todas las reservas |
| GET | `/reservas/{reserva_id}` | Obtener una reserva por ID |
| PUT | `/reservas/{reserva_id}` | Actualizar una reserva |
| DELETE | `/reservas/{reserva_id}` | Eliminar una reserva |
| PATCH | `/reservas/{reserva_id}/confirmar` | Confirmar una reserva |

### Equipamientos

| Método | Ruta | Descripción |
|--------|------|-------------|
| POST | `/equipamientos` | Crear un equipamiento |
| GET | `/equipamientos` | Listar todos los equipamientos |
| GET | `/equipamientos/{equipamiento_id}` | Obtener un equipamiento por ID |
| PATCH | `/equipamientos/{equipamiento_id}/estado` | Actualizar el estado de un equipamiento |

## Estructura del proyecto

```
Proyecto-N-1-Backend/
├── app/
│   ├── main.py                    # Punto de entrada de la aplicación FastAPI
│   ├── domain/                    
│   │   ├── entities.py            # Entidades: Sala, Usuario, Reserva, Equipamiento
│   │   └── reglas_negocio.py      # Reglas de negocio del dominio
│   ├── repositories/              # Acceso a datos (una clase por entidad)
│   │   ├── sala_repository.py
│   │   ├── usuario_repository.py
│   │   ├── reserva_repository.py
│   │   └── equipamiento_repository.py
│   ├── services/                  # Lógica de negocio (una por entidad)
│   │   ├── sala_service.py
│   │   ├── usuario_service.py
│   │   ├── reserva_service.py     # Valida que existan Sala y Usuario
│   │   └── equipamiento_service.py
│   ├── routers/                   # Endpoints de la API
│   │   ├── sala_router.py
│   │   ├── usuario_router.py
│   │   ├── reserva_router.py
│   │   └── equipamiento_router.py
│   ├── schemas/
│   │   └── dtos.py                # Modelos Pydantic de entrada y salida
│   ├── shared/
│   │   └── in_memory_store.py     # Almacenamiento en memoria
│   └── tests_manual/              # Pruebas manuales de los endpoints (.http)
│       ├── pruebas_sala.http
│       ├── pruebas_usuario.http
│       ├── pruebas_reserva.http
│       └── pruebas_equipamiento.http
├── requirements.txt               # Dependencias del proyecto
└── README.md
```
**Nota:** los datos se guardan en memoria; cada vez que se reinicia el servidor estos se pierden.

## Equipo
-Tomás Mardones: Lider de grupo y documentacion e integracion.
-Jesus huencumil: API e Logica de negocio y Calidad e Pruebas.
-Alonso Lantaño: Dominio y Datos.
-Diego Vasquez: Calidad y Pruebas.
