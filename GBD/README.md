# Módulo: Gestión de Bases de Datos (GBD)

## Resumen Teórico
Durante este módulo he estudiado el ciclo de vida de la información, desde su gestión básica hasta el diseño avanzado de sistemas de almacenamiento. Los conceptos fundamentales adquiridos incluyen:

* **Sistemas de Información:** comprensión de la información como recurso estratégico, sus cualidades (precisión, oportunidad, compleción, coherencia y seguridad) y su clasificación en niveles operacionales, tácticos y estratégicos.
* **Evolución y Modelos:** análisis de la transición desde sistemas de gestión de ficheros hasta los modelos modernos. He dominado las arquitecturas centralizadas y distribuidas (replicación, fragmentación y particionamiento) y el cumplimiento de las propiedades ACID (Atomicidad, Consistencia, Aislamiento, Durabilidad) para garantizar la integridad de los datos.
* **Arquitectura ANSI/SPARC:** implementación de la arquitectura de tres niveles (interno/físico, conceptual y externo) para asegurar la independencia lógica y física entre los datos y las aplicaciones.
* **SGBD (DBMS):** Funciones clave como la gestión de transacciones, seguridad, concurrencia, uso de metadatos (diccionario de datos) y herramientas de salvaguarda y recuperación.

---

## Prácticas y Modelado
He completado un ciclo de prácticas enfocado en el diseño profesional de bases de datos relacionales, utilizando herramientas de diagramación y software de gestión.

### 1. Modelado Conceptual y Lógico (Diagramas E/R)
* **Qué se hizo:** diseño de diagramas Entidad-Relación (E/R) usando Microsoft Visio.
* **Enfoque técnico:** he definido entidades, atributos (claves primarias y foráneas), relaciones (1:N, M:N) y especializaciones/herencias. He realizado la transición lógica al Modelo Relacional, determinando las claves ajenas necesarias para garantizar la integridad referencial.

### 2. Implementación en Microsoft Access
* **Qué se hizo:** materialización de los modelos lógicos mediante Microsoft Access, creando tablas, estableciendo tipos de datos y configurando relaciones con Integridad Referencial basándose en el modelo Entidad-Relación.
* **Logro técnico:** he definido el orden correcto de llenado de datos, asegurando que las tablas independientes y aquellas que actúan como "padres" se poblen antes que las tablas dependientes, evitando errores de integridad.

### 3. Normalización
* **Qué se hizo:** ejercicios prácticos de normalización, aplicando reglas de la 1FN a la 5FN para eliminar dependencias transitivas y multivaloradas, evitando así anomalías en la inserción, actualización y borrado.
