# Mini Gestor de Tareas
Esta es una aplicación web simple para gestionar tareas, construida con un backend en FastAPI y un frontend en Angular.
## Estructura del Proyecto

├── back

    ├── main.py            # Archivo principal para lanzar el servidor FastAPI
    └── requirements.txt   # Dependencias del backend


└── front

    ├── src                # Código fuente del proyecto Angular
    ├── angular.json       # Configuración de Angular
    └── package.json       # Dependencias del frontend



## Backend (FastAPI)
### Requisitos
- Python 3.6 o superior
- pip (gestor de paquetes de Python)
### Instalación
1. Navega a la carpeta del backend:
```
    cd back
```


2. Crea un entorno virtual (opcional pero recomendado):
```
    python -m venv venv
    source venv/bin/activate  # En Windows usa venv\Scripts\activate
```


3. Instala las dependencias:
```
    pip install -r requirements.txt
```


### Ejecutar el Servidor
Para lanzar el servidor de FastAPI, ejecuta el siguiente comando:
```
python main.py
```


El servidor estará disponible en `http://127.0.0.1:8000`.
### Endpoints Disponibles
- **GET /tasks**: Obtiene la lista de todas las tareas.
- **POST /tasks**: Crea una nueva tarea.
- **PUT /tasks/{task_id}**: Actualiza el estado de completado de una tarea.
- **DELETE /tasks/{task_id}**: Elimina una tarea específica.
## Frontend (Angular)
### Requisitos
- Node.js (versión 12 o superior)
- npm (gestor de paquetes de Node)
### Instalación
1. Navega a la carpeta del frontend:
```
    cd front
```


2. Instala las dependencias:
```
    npm install
```


### Ejecutar la Aplicación
Para lanzar la aplicación Angular, ejecuta el siguiente comando:
```
ng serve
```


La aplicación estará disponible en `http://localhost:4200`.
## Notas Adicionales
- Asegúrate de que el servidor de FastAPI esté funcionando antes de iniciar la aplicación Angular, ya que el frontend hace llamadas a la API del backend.

¡Gracias por usar Mini Gestor de Tareas!