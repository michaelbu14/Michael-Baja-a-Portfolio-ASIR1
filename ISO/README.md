# 🖥️ Módulo: Implantación de Sistemas Operativos (ISO)

## 🧠 Resumen General del Aprendizaje
A lo largo de este primer curso en el módulo de ISO, he adquirido una base técnica sólida que abarca desde la virtualización hasta la administración avanzada y recuperación de desastres. He aprendido a desplegar entornos heterogéneos instalando sistemas clientes y servidores (Windows Server 2022/2025, Ubuntu, Fedora, AlmaLinux)[cite: 1, 3], y a realizar actualizaciones complejas, como forzar el paso a Windows 11 emulando hardware TPM 2.0[cite: 6]. 

A nivel de infraestructura, he dominado el particionado de discos con utilidades como `fdisk` y `GParted`[cite: 8], y el escalado empresarial utilizando volúmenes lógicos (LVM) y RAID[cite: 19, 20]. En cuanto a la administración diaria, he configurado redes, enrutamientos (ICS) y firewalls (UFW y Windows Defender)[cite: 14, 15], además de gestionar de forma granular cuentas de usuario, grupos y permisos de acceso tanto en la consola de Linux como mediante las directivas NTFS en Windows[cite: 13, 18]. Finalmente, he aprendido a enfrentarme a sistemas rotos o bloqueados, auditando bases de datos SAM de contraseñas de forma offline[cite: 16] y reparando sectores de arranque sobreescritos[cite: 10]. 

Como complemento indispensable, he integrado Git y GitHub en mi flujo de trabajo para asegurar el control de versiones de mis configuraciones y proyectos[cite: 17].

---

## 🚀 Prácticas Seleccionadas y su Importancia

Para este portfolio, he filtrado las prácticas rutinarias y he seleccionado las cinco que mejor demuestran mi capacidad para resolver problemas complejos en entornos reales:

### 1. Hacking y Reset de Contraseñas de Windows (Práctica ISOP406)
* **Qué se hizo:** Utilizando un LiveCD de Ubuntu, forcé el montaje de una partición de Windows bloqueada por la hibernación ("Inicio Rápido"), localicé la base de datos SAM y eliminé la contraseña del administrador local usando la utilidad `chntpw` identificando al usuario por su RID (`03e9`)[cite: 16].
* **Por qué es importante:** Demuestra habilidades críticas de auditoría de seguridad y resolución de incidentes (troubleshooting). Saber acceder a un sistema cuando se han perdido las credenciales administrativas es vital para el rescate de servidores y equipos en un entorno empresarial.

### 2. Entornos Multiboot y Recuperación de Arranque (Prácticas ISOP304 e ISOP305)
* **Qué se hizo:** Se desplegó un entorno Dual-Boot (Windows 11 y Ubuntu 24.04) en el mismo disco, requiriendo desactivar BitLocker para la convivencia de particiones[cite: 9]. Posteriormente, se simuló la ruptura del arranque y se reparó manualmente usando la técnica de enjaulamiento (`chroot`) desde un LiveCD para reinstalar GRUB en la partición EFI del disco NVMe[cite: 10].
* **Por qué es importante:** Instalar un S.O. es fácil; entender y reparar la arquitectura de arranque (EFI/GRUB vs Windows Boot Manager) requiere un conocimiento profundo de la estructura interna de los discos. Garantiza que sé recuperar un sistema inoperativo.

### 3. Almacenamiento Avanzado: RAID y LVM (Prácticas ISOP504 e ISOP509)
* **Qué se hizo:** Por un lado, se simularon discos físicos en Linux con dispositivos `loop` para implementar LVM, creando volúmenes lógicos, espejos y snapshots[cite: 20]. Por otro lado, se montaron arreglos RAID 1 (reflejo) y RAID 5 (paridad) en Windows Server 2025 y Windows 11[cite: 19].
* **Por qué es importante:** Demuestra que sé cómo evitar que una empresa pierda sus datos ante el fallo físico de un disco. LVM y RAID son el estándar de la industria para asegurar la alta disponibilidad y la tolerancia a fallos en servidores de almacenamiento.

### 4. Montaje de Particiones y Seguridad NTFS/ext4 (Práctica ISOP503)
* **Qué se hizo:** Se automatizó el montaje de discos secundarios en GNU/Linux editando el archivo `/etc/fstab` mediante identificadores únicos (UUID)[cite: 18]. Además, se crearon grupos de usuarios para aplicar políticas de permisos exclusivas (lectura, escritura, ejecución) usando `chown/chmod` (valor octal 700) en Linux y Listas de Control de Acceso (ACLs) en particiones NTFS en Windows[cite: 18].
* **Por qué es importante:** La persistencia de datos tras un reinicio y la segregación de permisos son la barrera fundamental de seguridad. Esta práctica evidencia que sé proteger la confidencialidad de los datos frente a accesos no autorizados dentro de un entorno multiusuario.

### 5. Control de Versiones: Integración con Git y GitHub (Práctica ISOP411)
* **Qué se hizo:** Creación de repositorios locales (`git init`), registro del historial de cambios (`git commit`) y sincronización con repositorios remotos en GitHub. Creación de ramas paralelas y realización de un "Pull Request" para fusionar el código de forma segura[cite: 17].
* **Por qué es importante:** Git es una herramienta indispensable en el sector IT. Demuestra que conozco las metodologías ágiles y que estoy preparado para trabajar en equipo, versionar mis propios scripts y auditar el historial de cambios en cualquier infraestructura.
