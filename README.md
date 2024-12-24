# **Sistema de Gestión de Concesionaria de Vehículos Usados**

### Desarrollado en Python | Proyecto Final de Programación I  
**Universidad Nacional de Entre Ríos**  
**Tecnicatura Universitaria en Desarrollo Web** 

---

## **Descripción del Proyecto**  
Este sistema está diseñado para gestionar de manera eficiente las operaciones de compra, venta y mantenimiento de vehículos usados en una concesionaria. Incluye funcionalidades para el registro de vehículos, clientes y transacciones, utilizando una interfaz interactiva y almacenamiento en archivos JSON.  

---

## **Videos de Presentación**

- **Ejecución del Sistema:**  
  [![Mira el video en YouTube](https://img.youtube.com/vi/CwvD74Q7fsQ/maxresdefault.jpg)](https://www.youtube.com/watch?v=CwvD74Q7fsQ)

- **Código del Proyecto:**  
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

## **Tecnologías Utilizadas**
- **Lenguaje:** Python  
- **Almacenamiento:** Archivos JSON  
- **IDE:** Visual Studio Code
