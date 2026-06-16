# Módulo: Planificación y Administración de Redes (PAR)

## Resumen General del Aprendizaje
Durante este curso, he adquirido una visión técnica e integral de las redes de telecomunicaciones, abarcando desde el diseño físico hasta la capa de aplicación. He asimilado los fundamentos de transmisión y atenuación, el cálculo avanzado de subredes (Subnetting/VLSM), y los estándares de cableado estructurado ANSI/TIA-568 e ISO/IEC 11801. Además, he estudiado a fondo las tecnologías inalámbricas, analizando los estándares Wi-Fi 6, configuraciones en malla (Mesh), Bluetooth y protocolos IoT como Zigbee.

A nivel práctico, he configurado arquitecturas de red complejas implementando VLANs (802.1Q), puentes de red (Bridges) y asignación IP mediante `Netplan` e `ifupdown` en sistemas Linux y Windows. He llevado a cabo auditorías capturando tráfico con Sniffers a bajo nivel, analizado vulnerabilidades en la capa de enlace como con ARP, e implementado seguridad mediante firewalls y servicios como OpenDNS. 

El núcleo de mi capacitación se ha centrado en el diseño de topologías de enrutamiento avanzado, configurando infraestructuras en anillo y comunicando redes heterogéneas mediante enrutamiento estático y protocolos dinámicos (RIPv2), tanto en plataformas Microsoft (RRAS) como en código abierto (FRRouting).

---

## Prácticas y Proyectos Seleccionados

He seleccionado aquellos proyectos y laboratorios que evidencian de forma real mi capacidad para planificar, desplegar y administrar infraestructuras de red a nivel empresarial:

### 1. Proyecto Integral de Cableado Estructurado (M-VISION SECURITY SYSTEM)
**El Reto y Ejecución:** diseño, planificación y documentación de un Sistema de Cableado Estructurado (SCE) en un edificio de dos plantas para 68 trabajadores. Se diseñaron los subsistemas de área de trabajo, cableado horizontal y backbone vertical, centralizando 160 puntos de red en switches y patch panels dentro de dos armarios Rack (42U y 24U). Se especificó el uso de cable UTP Categoría 6 LSZH y enlaces de Fibra Óptica Multimodo OM3 con conectores LC para garantizar transferencias de 10 Gbps entre plantas.
**Impacto Profesional:** evidencia el dominio absoluto de la capa física, la elaboración de presupuestos técnicos, la interpretación de planos, y el conocimiento de los estándares necesarios para superar una auditoría de certificación (TIA/EIA 568B).

### 2. Enrutamiento Avanzado en Windows Server: NAT, RIPv2 y VPN (Práctica PARP603)
**El Reto y Ejecución:** se habilitó el rol de Acceso Remoto (RRAS) en Windows Server 2022 para actuar como enrutador de borde. Se configuró NAT para proporcionar salida a Internet a los clientes de las redes privadas, se implementó enrutamiento dinámico mediante RIPv2 y se desplegó un servidor VPN (PPTP/MS-CHAP v2), ajustando las directivas NPS para conceder acceso seguro.
**Impacto Profesional:** configurar un Windows Server como router y servidor VPN demuestra un control sólido sobre los servicios corporativos de Microsoft, garantizando el acceso remoto seguro para los empleados.

### 3. Enrutamiento Dinámico en Anillo con GNU/Linux (Práctica PARP604)
**El Reto y Ejecución:** se modificó el kernel (`sysctl`, habilitando `net.ipv4.ip_forward=1`) en múltiples servidores Ubuntu para permitir el reenvío de paquetes IP. Posteriormente, se instaló la suite FRRouting (FRR) y se utilizó la consola interactiva `vtysh` para configurar el protocolo dinámico RIPv2 dentro de una topología de tres routers en anillo.
**Impacto Profesional:** Desplegar protocolos dinámicos en Linux exige conocimientos profundos de arquitectura de red, evidenciando la capacidad para crear infraestructuras tolerantes a fallos que convergen automáticamente ante caídas de enlace.

### 4. Enrutamiento Estático Mixto: Windows y Linux (Práctica PARP605)
**El Reto y Ejecución:** diseño de una red en anillo interconectando routers de distintos fabricantes (Windows Server y Ubuntu Server). Tras aislar los segmentos LAN mediante virtualización, se configuraron tablas de enrutamiento estático cruzadas, verificando la conectividad de extremo a extremo mediante comandos de diagnóstico (`ping`, `tracepath`, `tracert`).
**Impacto Profesional:** enseña la habilidad crítica de interconectar y hacer que sistemas Microsoft y distribuciones Linux "hablen el mismo idioma" a nivel de Capa 3, replicando entornos empresariales heterogéneos reales.

### 5. Segmentación Lógica: VLANs (802.1Q) y Sockets (Práctica PARP601)
**El Reto y Ejecución:** se cargó el módulo `8021q` en el kernel de Linux para operar con el estándar IEEE 802.1Q, aislando el tráfico mediante la creación de subinterfaces lógicas etiquetadas con distintos VLAN IDs (ens33.2 y ens33.3). Además, se auditaron las conexiones y puertos del sistema usando la utilidad `ss`.
**Impacto Profesional:**l as VLANs son el pilar del diseño de red moderno para reducir dominios de broadcast. Saber aislar tráfico lógicamente desde la línea de comandos es esencial en cualquier arquitectura.

### 6. Análisis de Tráfico de Red y Sniffers (Práctica PARP401)
**El Reto y Ejecución:** captura y filtrado de tráfico en tiempo real (ICMP, HTTP, DNS, Telnet) mediante analizadores de protocolos (Wireshark, NetworkMiner, `tcpdump` y `windump`). Se logró interceptar tráfico no cifrado extrayendo archivos de texto plano y se instaló `ntopng` para monitorizar flujos gráficamente vía web.
**Impacto Profesional:** la lectura de paquetes a bajo nivel es la habilidad definitiva para diagnosticar averías complejas, detectar cuellos de botella e identificar posibles intrusiones o fugas de datos.

### 7. Seguridad en Capa de Enlace: ARP Poisoning (Práctica PARP503)
**El Reto y Ejecución:** análisis del proceso de resolución de direcciones (ARP). Se manipularon las tablas de caché introduciendo entradas físicas estáticas falsificadas para simular un ataque de "ARP", interceptando y bloqueando exitosamente la comunicación entre clientes de la misma subred.
**Impacto Profesional:** Entender la relación IP-MAC y cómo vulnerarla permite al administrador aplicar medidas de seguridad directas en los switches corporativos.

### 8. Configuración Avanzada de Interfaces: Netplan y Bridges (Práctica PARP405)
**El Reto y Ejecución:** gestión de la red en Ubuntu Server alternando entre herramientas modernas como `Netplan` (archivos YAML) y métodos clásicos como `ifupdown`. Se asignaron IPs estáticas y se crearon puentes de red virtuales (Bridges - `br0`), unificando varios adaptadores físicos en una misma interfaz lógica.
**Impacto Profesional:** administrar la red desde la terminal es obligatorio en servidores sin entorno gráfico. La creación de Bridges es un paso previo imprescindible para dominar los entornos de virtualización y contenedores.
