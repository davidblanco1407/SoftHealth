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
★ **Editor de Código:** Requerido para ejecutar el código recomendamos ***Visual Studio Code***, [descargar](https://code.visualstudio.com/download).  
★ **Navegador:** Google Chrome, Mozilla Firefox o Safari (últimas versiones).
## 3. Ingreso al Sistema
Antes de ejecutar el código debe instalar dos librerías externas que no viene por defecto ni en **Python** ni en **MongoDBCompass**, consulte en la sección 6 **Preguntas frecuentes** para mayor información.
1. En el ***Buscador de Windows***, buscar y ejecutar ***Simbolo del Sistema***
2. Ingresa el comando ***pip install simple-colors***, si no funciona intenta con el comando ***py -m pip install simple-colors***
3. Descargar [***MongoDB Database Tools***](https://www.mongodb.com/try/download/database-tools)
4. Descomprimir el zip descargado y dirigirse a la carpeta ***bin***
5. Copiar todos los archivos
6. Dirigirse a la ruta ***C:\Program Files\MongoDB\Server\7.0\bin\bin***
7. Pegar todos los archivos
9. En el navegador de su preferencia dirigirse a el enlace del repositorio [***SoftHealth***](https://github.com/davidblanco1407/SoftHealth.git)
11. Dentro de la rama **main**, descargar el archivo zip
12. Descomprimir y dentro de la carpeta ***SoftHealth-main*** buscar el file ***db***
13. Dar click derecho y seleccionar la opción ***Copiar como ruta de acceso***
14. Por defecto la ruta de acceso está separada por ***slash ( / )***. Verificar y reemplazar cada uno con ***backslash ( \\ )***, para dígitarlo presionar ***Alt+92***
15. Abrir ***Mongo DB Compass***
16. Nuevamente en el ***Buscador de Windows***, buscar y ejecutar ***Simbolo del Sistema***
17. Ingresar el comando ***cd C:\Program Files\MongoDB\Server\7.0\bin***
18. Ingresar el comando ***mongorestore --db softhealth (ruta de acceso copiada)***
19. Verificar si se importó la base de datos ***softhealth***
20. Abrir ***Visual Studio Code*** o su editor de código favorito
21. Abrir la carpeta ***SoftHealth-main***
22. Buscar el file ***main***
23. Ejecutar
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

• **¿Qué es la librería *simple_colors*?:** Es una librería externa de ***Python*** que muestra ciertos enunciados con diferentes colores, esto con el fin de que la interfaz sea más llamativa e intuitiva, la instalación es completamente gratuita y segura.

• **Error al instalar la librería *simple_colors*:** Verifique si esta librería ya se encuentra instalado en su ordenador. Revisa la conexión a internet.

• **¿Qué es la librería *MongoDB Database Tools*?:** Es una librería externa de MongoDB que ofrece varias herramientas, una de ellas es ***mongorestore*** la cual se requiere para la importación de la base de datos.

• **Error al guardar datos:** Asegúrese de que todos los campos obligatorios estén completados. Revisa la conexión a internet.
## 7. Contacto y Soporte Técnico
Para cualquier consulta o problema técnico, por favor contacta al equipo de soporte:  
★ **Teléfono:** +57 320 4064112  
★ **Email:** soporte@softhealth.com  
★ **Horario de atención:** Lunes a Viernes, 9:00 AM - 5:00 PM  
