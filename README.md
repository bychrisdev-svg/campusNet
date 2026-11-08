# CampusNet - Red Social Académica

CampusNet es una red social académica desarrollada en Python mediante la implementación de un **grafo dirigido**. El proyecto permite representar las relaciones entre estudiantes, profesores y egresados de una comunidad universitaria.

La aplicación utiliza el patrón arquitectónico **Modelo-Vista-Controlador (MVC)** para organizar el código y separar las responsabilidades de cada componente.

## Funcionalidades

### 1. Gestión del grafo (CRUD)

El sistema permite realizar las siguientes operaciones:

- Crear usuarios (vértices).
- Actualizar la información de los usuarios.
- Eliminar usuarios.
- Crear relaciones dirigidas entre usuarios (aristas).
- Eliminar relaciones existentes.
- Evitar usuarios y relaciones duplicadas.
- Validar los roles de los usuarios y las relaciones.

### 2. Representación del grafo

La red social utiliza una **lista de adyacencia** para representar las conexiones entre usuarios.

Cada vértice representa un usuario y cada arista dirigida representa una relación de seguimiento.

### 3. Algoritmos de grafos

El proyecto implementa los siguientes algoritmos:

- **Búsqueda en Anchura (BFS):** Recorre el grafo por niveles a partir de un vértice inicial.
- **Búsqueda en Profundidad (DFS):** Explora los vértices siguiendo cada camino hasta donde sea posible.
- **Alcanzabilidad:** Determina si un usuario puede llegar a otro mediante las relaciones dirigidas.
- **Detección de ciclos:** Identifica la existencia de ciclos en el grafo dirigido.

### 4. Análisis de la red social

El sistema permite realizar consultas para analizar las relaciones entre los usuarios:

- **Grado de entrada (In-Degree):** Cantidad de usuarios que siguen a un usuario determinado.
- **Grado de salida (Out-Degree):** Cantidad de usuarios que sigue un usuario determinado.
- **Usuarios sin seguidores:** Identifica usuarios cuyo grado de entrada es cero.
- **Usuarios más influyentes:** Identifica los usuarios con mayor grado de entrada.
- **Usuarios más activos:** Identifica los usuarios con mayor grado de salida.

## Estructura del proyecto

```text
campusNet/
│
├── controllers/
│   └── graph_controller.py
│
├── models/
│   ├── edge.py
│   ├── graph.py
│   └── vertex.py
│
├── views/
│   └── graph_view.py
│
├── main.py
└── README.md
```

## Tecnologías utilizadas

- **Python 3:** Lenguaje de programación principal.
- **Collections:** Utilizado para implementar la cola del algoritmo BFS mediante `deque`.
- **Estructuras de datos:** Diccionarios, listas y conjuntos.
- **Programación Orientada a Objetos (POO).**
- **Arquitectura MVC:** Separación de responsabilidades entre modelos, vistas y controladores.

No se requieren bibliotecas externas para ejecutar el proyecto.

## Instalación y ejecución

### 1. Clonar el repositorio

```bash
git clone https://github.com/bychrisdev-svg/campusNet.git
```

### 2. Ingresar al directorio del proyecto

```bash
cd campusNet
```

### 3. Ejecutar la aplicación

```bash
python main.py
```

## Datos iniciales

La aplicación carga una red social académica de ejemplo compuesta por:

- **12 usuarios (vértices).**
- **19 relaciones dirigidas (aristas).**

### Tipos de usuarios

El sistema contempla tres roles:

| Rol | Descripción |
|---|---|
| Student | Estudiante universitario

### Autor

Christopher Osorio P

GitHub: @bychrisdev-svg