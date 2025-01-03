# Trabajo Práctico Final: Docker & Docker Compose | AUS - Sistemas Operativos 2024
Este Trabajo Práctico implementa una aplicación web para gestionar información sobre juegos de mesa, desarrollada utilizando Docker y Docker Compose. La aplicación se compone de dos servicios principales:

● Aplicación Web
Desarrollada en Python utilizando el framework Flask.
Servida por Apache HTTP Server.
Permite realizar operaciones CRUD (Crear, Leer, Actualizar y Eliminar) sobre una base de datos de juegos de mesa.

● Base de Datos
Utiliza un contenedor con la imagen oficial de MongoDB.
Almacena de forma persistente los datos relacionados con los juegos de mesa.

# Requisitos para Ejecutar el Proyecto
Instalar:

● Docker

● Docker Compose

# Instrucciones para Despliegue
1. Clonar el Repositorio

```bash
git clone https://github.com/MatiasHaspert/TrabajoFinalSO.git
cd TrabajoFinalSO
```
2. Iniciar los Servicios
Construir y desplegar los contenedores:

```bash
docker compose up --build
```
3. Acceder a la Aplicación
Abre un navegador y visita:

● http://localhost:80 para interactuar con la aplicación web.

4. Finalizar los Servicios
Para detener y eliminar los contenedores:
```bash
docker compose down
```
