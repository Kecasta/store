# Proyecto Django - Gestión de Clientes y Productos

Este proyecto Django está diseñado para gestionar dos funcionalidades principales: el manejo de **Clientes** y el manejo de **Productos**. Ambas funcionalidades son implementadas como dos aplicaciones separadas dentro del mismo proyecto Django, cada una con sus propios CRUD (Crear, Leer, Actualizar, Eliminar).

## Estructura del Proyecto

El proyecto tiene la siguiente estructura:
Secompone de dos aplicaciones independientes cada una con un formulario basado en modelacion de datos y renderizados por plantillas HTML y CSS




## Funcionalidades

### Aplicación de Clientes

La aplicación `cliente` proporciona un sistema para crear, visualizar, actualizar y eliminar clientes. Cada cliente tiene los siguientes campos:

- **Nombre**: Nombre completo del cliente.
- **Correo electrónico**: Correo electrónico del cliente.
- **Teléfono**: Número telefónico del cliente.
- **Email**: Dirección del cliente.
- **Empresa**: Epresa a la cual pertenece.

### Aplicación de Productos

La aplicación `producto` permite gestionar los productos disponibles. Cada producto tiene los siguientes campos:

- **Codigo**: Codigo del producto.
- **Nombre**: Nombre del producto.
- **Precio costo**: Precio de costo del producto.
- **Precio venta**: Precio de evnta del producto.
- **Stock inicial**: Cantidad disponible en inventario.
