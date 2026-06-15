 **CHATBOT DE GESTIÓN DE VACACIONES**

---

 **Descripción del Proyecto**

Este proyecto consiste en el desarrollo de un chatbot que automatiza el proceso de solicitud de vacaciones dentro de una organización.

El sistema fue diseñado a partir de un modelo de procesos **BPMN 2.0**, asegurando coherencia entre el análisis de negocio y la implementación técnica.

---

  **Objetivo**

Automatizar el proceso de solicitud de vacaciones, permitiendo:

*  Validar días disponibles
*  Gestionar aprobaciones
*  Reducir intervención manual
*   Mejorar tiempos de respuesta

---

**Modelo de Negocio (BPMN)**

El proceso fue modelado utilizando BPMN 2.0, incluyendo:

*  Carril **Usuario**
*  Carril **Sistema / Bot**
*  Eventos de inicio y fin
*  Gateways (decisiones)
*  Flujo completo del proceso

---

  **Tecnologías Utilizadas**

*  Lenguaje: **Python**
*  Entorno: **Consola (simulación)**
*  Base de datos: **Estructura en memoria (diccionario simulando Excel)**

---

##  **Estructura del Proyecto**

(editar al concluir codigo) /*/

---

##  **Cómo ejecutar**

1. Tener Python instalado
(editar al concluir el codigo) /*/



---

##  **Flujo del Bot**

1.  Usuario ingresa su nombre
2.  El sistema solicita cantidad de días
3.  Se valida disponibilidad
4.  Se determina si requiere aprobación
5.  Se aprueba o  rechaza la solicitud

---

##  **Gestión de Estados**

El sistema implementa una máquina de estados:

* INICIO
* PEDIR_DIAS
* VALIDAR
* APROBACION
* APROBADO
* RECHAZADO

---

##  **Decisiones (Gateways)**

El chatbot toma decisiones en base a:

*  ¿Tiene días suficientes?
*  ¿Requiere aprobación del jefe?
*  ¿El jefe aprueba?

---

##  **Manejo de Errores (Camino Infeliz)**

El sistema contempla distintos escenarios:

*  Usuario inexistente
*  Entrada no numérica
*  Valores inválidos (negativos o cero)
*  Rechazo por falta de días

---

##  **Casos de Prueba**

| Caso             | Resultado           |
| ---------------- | ------------------- |
| Solicitud válida |  Aprobado          |
| Exceso de días   |  Rechazado         |
| Error de entrada |  Mensaje de error |

---

##  **Posibles Mejoras**

*  Integración con base de datos real (MySQL / SQLite)
*  Implementación en Telegram o WhatsApp
*  Interfaz gráfica
*  Persistencia de solicitudes

---

##  **Autor**

Trabajo Práctico Integrador
**Tecnicatura Universitaria en Programación**

---
