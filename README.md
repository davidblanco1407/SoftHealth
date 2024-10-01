# Manual de Usuario
## Índice
1. Introducción
2. Requisitos del Sistema
3. Ingreso al Sistema
4. Navegación por el Sistema
5. Funciones Principales  
5.1 Información personal médico  
5.2 Agendar citas  
5.3 Tu historia clínica  
6. Preguntas Frecuentes
7. Contacto y Soporte Técnico
## 1. Introducción
**SoftHealth** es un proyecto formativo de **Análisis y desarrollo de Software** para el sector salud, dirigido por el **SENA**. Este manual está diseñado para ayudar a los usuarios a familiarizarse con nuesto sistema. Aquí encontrarás instrucciones sobre cómo utilizar las principales funciones y resolver problemas comunes.
## 2. Requisitos del Sistema
★ **Sistema Operativo:** Windows 10 o superior, macOS Mojave o superior.  
★ **Conexión a Internet:** Requerido para acceder a funcionalidades en línea.  
★ **MongoDBCompass**: Gestor de base de datos requerido para su correcto funcionamiento, [descargar](https://www.mongodb.com/try/download/compass).  
★ **Editor de Código:** Requerido para ejecutar el código, recomendamos ***Visual Studio Code***, [descargar](https://code.visualstudio.com/download).  
★ **Navegador:** Google Chrome, Mozilla Firefox o Safari (últimas versiones).
## 3. Ingreso al Sistema
Antes de ejecutar el código debe instalar una librería externa que no viene por defecto en **python**, consulte en la sección 6 **Preguntas frecuentes** para mayor información.
1. En el ***Buscador de Windows***, buscar y ejecutar ***Simbolo del Sistema***
2. Ingresa el comando ***pip install simple-colors***, si no funciona intenta con el comando ***py -m pip install simple-colors***
3. Abrir el enlace del repositorio ***SoftHealth***
4. En la rama **main**, descargar el archivo zip
5. Extraer la carpeta ***SoftHealth-main***
6. Buscar el file ***db***
7. Dar click derecho y seleccionar la opción ***Copiar como ruta de acceso***
8. Por defecto la ruta de acceso está separada por ***slash ( / )***. Verificar y reemplazar cada uno con ***backslash ( \\ )***, para dígitarlo presionar ***Alt+92***
9. Abrir ***Mongo DB Compass***
10. Nuevamente en el ***Buscador de Windows***, buscar y ejecutar ***Simbolo del Sistema***
11. Ingresa el comando ***mongorestore --db softhealth (ruta de acceso copiada)***
12. Verificar si se importó la base de datos ***softhealth***
13. Abrir ***Visual Studio Code*** o su editor de código favorito
14. Abrir la carpeta ***SoftHealth-main***
15. Buscar el file ***main***
16. Ejecutar
## 4. Navegación por el Sistema
En pantalla siempre se va a mostrar un menú con diferentes opciones enumeradas, con el fin de que si desea seleccionar una de ellas debe ingresar el número que corresponda a la función que desea usar.
## 5. Funciones Principales
## 5.1 Info. personal médico
Para acceder a esta funcion en el menú principal seleccione la opción 1 y llene los campos con los datos de la persona que hace parte del personal médico, es importante aclarar que los datos mostrados son datos son de carácter **público**.
## 5.2 Gestión de citas(beta)
Para acceder a esta funcion en el menú principal seleccione la opción 2 e ingrese la especialidad y la fecha que desee.
## 5.3 Historia clínica
Para acceder a esta funcion en el menú principal seleccione la opción 3, a continuación veremos un submenú donde podras 'Ver tu historia clínica' o 'Solicitar una edición' en caso de notar algun error.
## 6. Preguntas Frecuentes
• **No puedo iniciar sesión:** Verifica que tu nombre de usuario y contraseña sean correctos. Si el problema persiste, contacta al soporte técnico.

• **¿Qué es la librería *simple_colors*?:** Es una librería externa que muestra ciertos enunciados con diferentes colores, esto con el fin de que la interfaz sea más llamativa e intuitiva, la instalación es completamente gratuita y segura.

• **Error al instalar la librería *simple_colors*:** Revisa la conexión a internet.

• **Error al guardar datos:** Asegúrese de que todos los campos obligatorios estén completados. Revisa la conexión a internet.
## 7. Contacto y Soporte Técnico
Para cualquier consulta o problema técnico, por favor contacta al equipo de soporte:  
★ **Teléfono:** +57 320 4064112  
★ **Email:** soporte@softhealth.com  
★ **Horario de atención:** Lunes a Viernes, 9:00 AM - 5:00 PM  
