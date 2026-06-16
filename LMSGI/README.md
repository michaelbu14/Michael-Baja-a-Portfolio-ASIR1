# Módulo: Lenguajes de Marcas y Sistemas de Gestión de Información (LMSGI)

## Proyecto Destacado: Portal Web de Fórmula 1
Este repositorio incluye un proyecto web completo, estructurado en múltiples páginas HTML y dedicado íntegramente al mundo de la Fórmula 1. El sitio demuestra la aplicación práctica de los lenguajes de marcas y hojas de estilo mediante las siguientes secciones:
* **Historia y Evolución:** uso de etiquetas semánticas y multimedia integrada, combinando textos estructurados con audios de motores y vídeos históricos.
* **Reglamento y Normativa:** estructuración de datos complejos mediante la anidación de listas ordenadas y desordenadas para clasificar normativas técnicas y deportivas.
* **Pilotos y Circuitos:** implementación de mapas de imágenes interactivos (`<map>` y `<area>`) para enlazar coordenadas específicas de los trazados españoles con contenido multimedia, además de integrar elementos externos mediante `iframe`.
* **Merchandising:** maquetación avanzada de catálogos de productos y listas de precios utilizando tablas estructuradas con combinación de celdas y filas (`rowspan` y `colspan`).
* **Fan Zone:** creación de formularios interactivos y accesibles con validaciones en HTML5 (uso de patrones, rangos, y tipos de entrada específicos como `email`, `tel` o `color`).

---

## Resumen General del Aprendizaje (HTML5 y CSS3)
A lo largo de este módulo, se ha consolidado una base técnica sólida en el desarrollo web Front-end, dominando la separación entre el contenido (HTML) y la capa de presentación (CSS). Los conocimientos adquiridos abarcan:

### 1. Integración y Especificidad CSS
* Aplicación de estilos en línea (`style`), estilos embebidos (`<style>`) y vinculación de hojas externas mediante la etiqueta `<link>` y la regla `@import`.
* Comprensión de la cascada CSS, la herencia de propiedades entre elementos padre e hijo, y el control absoluto de la prioridad utilizando selectores de ID (`#`), clases (`.`) y la directiva `!important`.
* Implementación de hojas de estilo alternativas e interactivas para mejorar la accesibilidad del sitio.

### 2. Modelo de Cajas y Estructuración
* Control detallado del modelo de cajas gestionando márgenes (`margin`), rellenos (`padding`), bordes perimetrales y dimensiones exactas de los elementos.
* Diseño y estilización de tablas de datos, controlando la visibilidad de celdas vacías (`empty-cells`) y el espaciado interno.

### 3. Unidades de Medida y Formatos de Color
* Diferenciación práctica entre unidades absolutas (`px`, `pt`, `cm`) y relativas (`em`, `%`) para garantizar el correcto escalado tipográfico y la accesibilidad.
* Implementación de unidades de Viewport (`vh`, `vw`) para adaptar de forma dinámica el contenido al tamaño exacto de la ventana del navegador del usuario.
* Gestión avanzada del color utilizando formatos RGB, RGBA, HSL y HSLA, controlando el canal alfa para generar superposiciones y transparencias.

### 4. Diseño Web Adaptativo (Responsive Web Design)
* Uso de reglas `@media` para cargar diferentes arquitecturas visuales dependiendo del dispositivo de salida (pantalla, impresora, dispositivos portátiles).
* Creación de *Media Queries* basadas en la resolución de pantalla (ej. `max-width: 500px`) para reorganizar el contenido y adaptarlo a dispositivos móviles.

### 5. Estilización Avanzada y Fondos
* Personalización tipográfica definiendo familias de fuentes principales y de respaldo, alineación, interlineado (`line-height`), indentación y transformaciones de texto.
* Manipulación compleja de fondos, incluyendo la inserción de imágenes adaptables (`background-size: cover`), y la fijación de elementos visuales (`background-attachment: fixed`) para crear efectos de profundidad al hacer scroll.
