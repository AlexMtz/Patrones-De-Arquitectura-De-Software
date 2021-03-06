# Sistema de Monitoreo de Adultos Mayores (SMAM)

Repositorio del capítulo 3

Antes de ejecutar el código asegurate de instalar los prerrequisitos del sistema ejecutando:
> sudo pip install -r requirements.txt

El paquete que se instalará es el siguiente:

Paquete | Versión | Descripción
--------|---------|------------
pika    |0.10.0   | Libreria para python que permite conectar y utilizar RabbitMQ

*__Nota__: También puedes instalar éste prerrequisito manualmente ejecutando el siguiente comando*
> sudo pip install pika==0.10.0

### Estructura del repositorio

Dentro del repositorio encontraremos los siguientes directorios:

Directorio | Descripción
-----------|------------
Publicadores | Se encuentran todos los archivos que representan el rol de un publicador dentro del sistema SMAM.
Suscriptores | Se encuentran todos los archivos que representan el rol de un suscriptor dentro del sistema SMAM.

Así mismo en la raíz del capítulo 3 encontraremos los siguientes archivos:

Archivo | Descripción
--------|-------------
README.md | Contiene una breve descripción del repositorio.
monitor.py | Representa al componente que muestra datos, alertas y advertencias sobre los signos vitales dentro del SMAM.
requirements.py | Contiene el nombre y versión de las librerias necesarias para que el SMAM funcione correctamente.
simulador.py | Representa el set-up del sistema, es decir, inicializa la simulación del SMAM.

### Ejecutar Simulador

*__Nota__: La implementación de la versión del SMAM actual es distribuida, es decir, se puede ejecutar cada componente del sistema en ubicaciones geográficas distintas.*

Para ejecutar el simulador es necesario seguir los sigiuentes pasos:  
1. Abrir terminal en Ubuntu / Fedora.  
2. Clonar el repositorio:   `git clone https://github.com/AlexMtz/Patrones-De-Arquitectura-De-Software.git`  
3. Ingresar a la carpeta que descargamos:   `cd Patrones-De-Arquitectura-De-Software/`  
4. Acceder al capítulo 3:  `cd capitulo_3/`  
5. Instalar los prerrequisitos: `sudo pip install -r requirements.py`
6. Ejecutar el simulador: `python simulador.py`  

*__Nota__: El simulador unicamente inicializa a los publicadores del SMAM para inicalizar un suscriptor se deberá hacer lo siguiente.*

1. Abrir terminal en Ubuntu / Fedora.  
2. Clonar el repositorio:   `git clone https://github.com/AlexMtz/Patrones-De-Arquitectura-De-Software.git`  
3. Ingresar a la carpeta que descargamos:   `cd Patrones-De-Arquitectura-De-Software/`  
4. Acceder al capítulo 3:  `cd capitulo_3/`  
5. Instalar los prerrequisitos: `sudo pip install -r requirements.py`
6. Acceder al directorio de los suscriptores:  `cd Suscriptores/`  
7. Ejecutar cualquier suscriptor: `python procesador_de_temperatura.py` o `python procesador_de_ritmo_cardiaco.py` o `python procesador_de_presion.py`  
