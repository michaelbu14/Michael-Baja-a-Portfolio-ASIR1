# 🖥️ Módulo: Implantación de Sistemas Operativos (ISO)

## 🧠 Resumen General del Aprendizaje
A lo largo de este primer curso en el módulo de ISO, he adquirido una base técnica sólida que abarca desde la virtualización hasta la administración avanzada y recuperación de desastres. He aprendido a desplegar entornos heterogéneos instalando sistemas clientes y servidores (Windows Server 2022/2025, Ubuntu, Fedora, AlmaLinux), y a realizar actualizaciones complejas, como forzar el paso a Windows 11 emulando hardware TPM 2.0. 

A nivel de infraestructura, he dominado el particionado de discos con utilidades como `fdisk` y `GParted`, y el escalado empresarial utilizando volúmenes lógicos (LVM) y RAID. En cuanto a la administración diaria, he configurado redes, enrutamientos (ICS) y firewalls (UFW y Windows Defender), además de gestionar cuentas de usuario, grupos y permisos de acceso tanto en la consola de Linux como mediante las directivas NTFS en Windows. Finalmente, he aprendido a enfrentarme a sistemas rotos o bloqueados, auditando bases de datos SAM de contraseñas de forma offline y reparando sectores de arranque sobreescritos. 

Como complemento indispensable, he integrado Git y GitHub en mi flujo de trabajo para asegurar el control de versiones de mis configuraciones y proyectos.

---

## 🚀 Prácticas Seleccionadas y su Importancia

Para este portfolio, he seleccionado las siete que mejor demuestran mi capacidad para resolver problemas complejos en entornos reales:

### 1. Hacking y Reset de Contraseñas de Windows (Práctica ISOP406)
* **Qué se hizo:** Utilizando un LiveCD de Ubuntu, forcé el montaje de una partición de Windows bloqueada por la hibernación ("Inicio Rápido"), localicé la base de datos SAM y eliminé la contraseña del administrador local usando la utilidad `chntpw` identificando al usuario por su RID (`03e9`).
* **Por qué es importante:** Demuestra habilidades críticas de auditoría de seguridad y resolución de incidentes (troubleshooting). Saber acceder a un sistema cuando se han perdido las credenciales administrativas es vital para el rescate de servidores en un entorno empresarial.

### 2. Entornos Multiboot: Windows y Linux (Práctica ISOP304)
* **Qué se hizo:** Se desplegó un entorno Dual-Boot en un mismo disco duro virtual, gestionando el particionado para hacer convivir Windows 11 y Ubuntu. Para lograr la instalación de Ubuntu, fue necesario acceder a Windows y desactivar temporalmente el cifrado de unidad BitLocker.
* **Por qué es importante:** Demuestra la capacidad para preparar hardware compartido, entendiendo cómo interactúan diferentes sistemas de archivos y S.O. de forma nativa en un mismo equipo físico.

### 3. Recuperación y Reparación de Arranque (Práctica ISOP305)
* **Qué se hizo:** Se simuló la pérdida del gestor de arranque (GRUB) por sobreescritura y se reparó manualmente. Utilizando un LiveCD de Ubuntu y la técnica de enjaulamiento (`chroot`), se montaron las particiones EFI necesarias para reinstalar y actualizar GRUB (`grub-install`, `update-grub`) en los discos NVMe.
* **Por qué es importante:** Garantiza que sé recuperar un sistema inoperativo. Entender la arquitectura de arranque (EFI/GRUB vs Windows Boot Manager) es fundamental para solucionar desastres sin tener que recurrir al formateo.

### 4. Almacenamiento Avanzado: RAID en Windows (Práctica ISOP504)
* **Qué se hizo:** Se configuraron múltiples discos en Windows Server 2025 y Windows 11 para crear arreglos de almacenamiento tolerantes a fallos. Se desplegaron volúmenes distribuidos (JBOD), RAID 1 (reflejo) y RAID 5 (paridad) utilizando la Administración de Discos y los Espacios de Almacenamiento.
* **Por qué es importante:** Configurar RAID es el estándar de la industria para asegurar la alta disponibilidad. Evidencia que sé cómo evitar que una empresa pierda sus datos ante el fallo de hardware de un disco.

### 5. Gestión de Volúmenes Lógicos LVM en Linux (Práctica ISOP509)
* **Qué se hizo:** Se simularon discos físicos utilizando ficheros llenos de ceros (`dd`) y dispositivos `loop`. Sobre ellos, se implementó la tecnología LVM creando Volúmenes Físicos (PV), Grupos de Volúmenes (VG) y Volúmenes Lógicos (LV), aplicando además instantáneas (snapshots) y configuraciones en espejo.
* **Por qué es importante:** LVM aporta una flexibilidad de gestión que las particiones tradicionales no tienen. Saber redimensionar discos en caliente o hacer snapshots es vital para los respaldos (backups) en servidores Linux corporativos.

### 6. Montaje de Particiones y Seguridad NTFS/ext4 (Práctica ISOP503)
* **Qué se hizo:** Se automatizó el montaje de discos secundarios en GNU/Linux editando el archivo `/etc/fstab` mediante identificadores únicos (UUID). Además, se aplicaron políticas de permisos exclusivas usando `chown/chmod` (valor octal 700) en Linux y Listas de Control de Acceso (ACLs) en particiones NTFS en Windows.
* **Por qué es importante:** La persistencia de datos tras un reinicio y la segregación de permisos son la barrera fundamental de la seguridad. Demuestra que sé proteger la confidencialidad frente a accesos no autorizados en entornos multiusuario.

### 7. Control de Versiones: Integración con Git y GitHub (Práctica ISOP411)
* **Qué se hizo:** Creación de repositorios locales (`git init`), registro del historial de cambios (`git commit`) y sincronización con repositorios remotos en GitHub. Creación de ramas paralelas y realización de un "Pull Request" para fusionar el código de forma segura.
* **Por qué es importante:** Git es una herramienta indispensable en el sector IT. Demuestra que conozco las metodologías ágiles y que estoy preparado para versionar mis propios scripts, auditar cambios y trabajar en equipo.
