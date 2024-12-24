# **Sistema de Gestión de Concesionaria de Vehículos Usados**
**Desarrollado en Python**  
**Proyecto Final - Programación I**  
**Universidad Nacional de Entre Ríos**  
**Tecnicatura Universitaria en Desarrollo Web**  

**Tecnologías Utilizadas:**  
- Python  
- Archivos JSON  
- Visual Studio Code 

---

## **Descripción del Proyecto**  
Este sistema está diseñado para gestionar de manera eficiente las operaciones de compra, venta y mantenimiento de vehículos usados en una concesionaria. Incluye funcionalidades para el registro de vehículos, clientes y transacciones, utilizando una interfaz interactiva y almacenamiento en archivos JSON.  

---

## **Lo que Aprendí**

#### **Permanencia de Datos con JSON**
- **Comprensión del Concepto de Persistencia:** Aprendí a manejar datos persistentes utilizando archivos JSON, lo que me permitió guardar información entre ejecuciones del programa sin perder los datos. Esto fue crucial para mantener registros de manera permanente, como en la gestión de vehículos, clientes y transacciones.

#### **Estructuración y Manejo de los Datos**
- **Organización de Datos en JSON:** Aprendí a estructurar datos de manera eficiente utilizando JSON, lo que permitió representar de forma clara las entidades de mi sistema, como vehículos, clientes y transacciones. 
- **Normalización de la Información:** Me familiaricé con el concepto de normalización en la organización de datos, asegurando que las relaciones entre vehículos, clientes y transacciones estuvieran bien definidas para evitar redundancias y errores de integridad.
- **Acceso y Modificación de Datos:** A lo largo del proyecto, desarrollé habilidades para navegar y manipular estructuras de datos complejas, como listas y diccionarios, a fin de realizar consultas, inserciones y modificaciones de manera eficiente.

#### **Modularización con Funciones**
- **Desarrollo de Funciones Reutilizables:** Aprendí a modularizar el código creando funciones que abstraen tareas específicas, como agregar vehículos, registrar transacciones y buscar información. Esto no solo mejoró la legibilidad del código, sino también su mantenibilidad.
- **Descomposición de Problemas Complejos:** Implementar funciones me permitió descomponer el proyecto en pequeñas tareas manejables, lo cual facilita la resolución de problemas y mejora la organización general del código.
- **Facilitación de Pruebas:** Al dividir el código en funciones, aprendí a probar partes del sistema de manera más aislada, lo que facilitó la identificación de errores y la mejora de la calidad del software.

#### **Desarrollo Ágil**
- **Iteración Rápida y Mejora Continua:** A través de la implementación de características y pruebas constantes, aprendí a trabajar de manera ágil, mejorando y ajustando el sistema de forma continua según los requerimientos del proyecto.
- **Priorización de Funcionalidades:** Aprendí a identificar las funcionalidades esenciales para el funcionamiento del sistema, implementando las más importantes primero y ajustando características secundarias de acuerdo con el progreso del proyecto.

---

## **Video con explicacion en detalle de funcionamiento del codigo**
  
  [![Mira el video en YouTube](https://img.youtube.com/vi/-YvR8CUqmU4/maxresdefault.jpg)](https://www.youtube.com/watch?v=-YvR8CUqmU4)

---

## **Objetivo del Sistema**  
Desarrollar una solución de software que permita automatizar los procesos relacionados con la gestión de vehículos, clientes y transacciones, ofreciendo un control centralizado y eficiente para la concesionaria.

---

## **Requerimientos**

### **1. Registro de Vehículos:**  
   - **ID de vehículo:** Número único y autoincremental  
   - **Nº de Patente o Dominio**  
   - **Marca**  
   - **Modelo**  
   - **Tipo:** Sedán, Hatchback, SUV, Pick Up, etc.  
   - **Año**  
   - **Kilometraje**  
   - **Precio de Compra**  
   - **Precio de Venta**  
   - **Estado:** Disponible, Reservado, Vendido  

### **2. Gestión de Clientes:**  
   - **ID de Cliente:** Número único y autoincremental  
   - **Nombre**  
   - **Documento**  
   - **Apellido**  
   - **Dirección**  
   - **Teléfono**  
   - **Correo Electrónico**  

### **3. Registro de Transacciones:**  
   - **ID de Transacción:** Número único y autoincremental  
   - **ID de Vehículo**  
   - **ID de Cliente**  
   - **Tipo de Transacción:** Compra/Venta  
   - **Fecha**  
   - **Monto**  
   - **Observaciones**  

---

## **Características del Software**

1. **Almacenamiento de Información:**  
   Los datos se almacenan en archivos JSON, garantizando portabilidad y fácil manipulación.  

2. **Interfaces de Usuario Interactivas:**  
   - **Vehículos:**  
     - Crear, editar y eliminar vehículos.  
     - Realizar búsquedas por patente, marca, modelo y precios de compra/venta.  

   - **Clientes:**  
     - Crear, editar y eliminar clientes.  
     - Realizar búsquedas por documento, apellido y/o nombres.  

   - **Transacciones:**  
     - Registrar compras y ventas de vehículos.  
     - Generar reportes de compras y ventas por cliente, vehículo y rango de fechas, incluyendo totalizadores de montos.  

---

