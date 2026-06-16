# Módulo: Fundamentos de Hardware (FH)

## Resumen General del Aprendizaje
Este módulo proporciona una comprensión profunda de los componentes físicos y lógicos que constituyen las infraestructuras informáticas, abarcando desde la electrónica básica de un ordenador doméstico hasta arquitecturas complejas de servidores empresariales y entornos de computación en la nube. 

A lo largo del curso, se han consolidado competencias clave en:
* **Arquitectura y Microarquitectura de CPUs:** análisis detallado del procesador como cerebro del sistema. Estudio de buses de comunicación, chipsets, jerarquías de memoria caché (L1, L2, L3) y tecnologías de procesamiento paralelo como Multithreading Simultáneo (SMT/HyperThreading) y frecuencias dinámicas (Precision Boost / Turbo Boost).
* **Sistemas de Almacenamiento y Memorias:** diferenciación física y lógica entre tecnologías volátiles (DRAM principal) y no volátiles (ROM/BIOS). Análisis de la anatomía y mecánica de discos duros tradicionales (HDD con tecnologías avanzadas como HAMR y carcasas herméticas de Helio) frente a unidades sólidas (SSD). Gestión de tecnologías de memoria de servidor con corrección de errores (ECC, RDIMM, LRDIMM) frente a las domésticas (UDIMM) en estándares DDR4 y DDR5.
* **Sistemas de Alimentación y Protección Eléctrica:** estudio del Box Model energético, analizando la conversión de corriente alterna (CA) a continua (CC) mediante fuentes conmutadas (eficiencia, voltajes de 3.3V, 5V y 12V, estándar ATX 3.1) y mitigación de anomalías de suministro mediante tecnologías SAI/UPS (Off-line, interactiva y On-line de doble conversión) y su evolución hacia baterías de litio (LiFePO4).
* **Periféricos y visualización:** estudio de la arquitectura de adaptadores gráficos (procesamiento especializado en GPU y gestión del Frame Buffer) y tecnologías avanzadas de visualización (paneles IPS, OLED, Mini LED).

---

## Proyectos Destacados y Evidencias Técnicas

Se han seleccionado cuatro laboratorios prácticos y auditorías esenciales que demuestran la capacidad de diagnosticar, implementar y administrar soluciones de hardware tanto a nivel local como en la nube:

### 1. Instalación y Administración de un Hipervisor de Tipo 1 (VMware ESXi)
* **Descripción:** despliegue y parametrización de un hipervisor nativo (*Bare-Metal*) para la consolidación de servidores virtuales independientes del sistema operativo anfitrión.
* **Hitos técnicos:** instalación y configuración inicial del núcleo ESXi de VMware.
    * Acceso y dominio de la interfaz web de administración para la monitorización de recursos físicos (CPU, RAM, Almacenamiento).
    * Creación y aprovisionamiento de *Datastores* (Almacenes de datos) dedicados de forma exclusiva para el aislamiento de imágenes ISO y discos de máquinas virtuales.
    * Planificación del despliegue de servidores virtuales multi-plataforma (estructuras Linux y MS Windows).
    * Habilitación y auditoría de la gestión remota segura mediante consola de comandos a través del protocolo SSH (uso de clientes como PuTTY).

### 2. Creación de Instancias Virtuales e Infraestructura Cloud en MS Azure
* **Descripción:** despliegue de infraestructura como servicio (IaaS) utilizando el cloud público de Microsoft Azure para entornos de producción de alta disponibilidad.
* **Hitos técnicos:**
    * Elección y dimensionamiento de recursos de cómputos optimizados (aprovisionamiento de vCPUs, memoria RAM y almacenamiento virtualizado).
    * Configuración de arquitecturas base bajo sistemas operativos Linux de nivel corporativo (Ubuntu Server 24.04 LTS).
    * Diseño y gestión de redes virtuales y asignación dinámica/estática de direccionamiento IP público.
    * Securización del entorno mediante la implementación de *Network Security Groups* (NSG) que actúan como un cortafuegos perimetral, aplicando reglas estrictas por prioridad (restricción total de tráfico entrante, permitiendo únicamente el acceso cifrado mediante el puerto 22 para SSH).
    * Autenticación robusta sin contraseña mediante el uso de pares de claves criptográficas asimétricas (claves privadas `.pem`).

### 3. Estrategias Avanzadas de Copias de Seguridad y Redundancia de Datos
* **Descripción:** diseño e implementación de políticas de respaldo empresarial tolerantes a fallos de hardware y desastres lógicos.
* **Hitos técnicos:**
    * Preparación y aprovisionamiento de múltiples unidades de almacenamiento secundario en el sistema.
    * Implementación de esquemas de tolerancia a fallos mediante la configuración de un arreglo de discos RAID 1 por software, garantizando el espejo de datos idéntico frente a averías de un disco físico.
    * Instalación y configuración del software de respaldo corporativo *Uranium Backup*.
    * Automatización y ejecución de un ciclo completo de copias de seguridad: Full Backup (respaldo completo de base), Backup Diferencial (acumulación de cambios desde el último completo) y Backup Incremental (copia exclusiva de modificaciones diarias).
    * Pruebas de restauración y recuperación de datos borrados para verificar la integridad de las copias.

### 4. Caracterización, Auditoría y Diagnóstico de Servidores Empresariales
* **Descripción:** análisis físico, lógico y arquitectónico exhaustivo de un servidor en rack de alto rendimiento diseñado para entornos de producción corporativos (ej. HP ProLiant DL360 G7).
* **Hitos técnicos:**
    * Auditoría de bajo nivel mediante el acceso y configuración de la utilidad de configuración basada en ROM (BIOS/UEFI) del servidor.
    * Análisis del chasis y los flujos térmicos, documentando la distribución de los ventiladores redundantes de extracción activa (FANS).
    * Diagnóstico preventivo mediante la monitorización del Systems Insight Display (SID), interpretando los indicadores de salud LED de los subsistemas críticos (procesadores, fuentes de alimentación PS1/PS2 y bancos de memoria RAM DIMM).
    * Estudio de las tecnologías de administración fuera de banda (OOB) independientes del sistema operativo principal para tareas de mantenimiento remoto.
