Django Node Chat con Login Redes Sociales
=================

## Python y NodeJs
Python 3.4.1
NodeJs v0.10.24

## Como usar

Descargamos el repositorio y creamos nuestro entorno virtual, usare virtualenvwrapper:

    mkvirtualenv chat
    workon chat

Nos ubicamos en el repositorio y ejecutamos :

    pip install -r requirements.txt
    
Con esto ya tendremos listo los paquetes necesarios para arrancar el proyecto.
Ahora necesitamos agregar los valores de las key y secret de nuestras apps de Facebook y Twitter respectivamente.

    SOCIAL_AUTH_TWITTER_KEY = ''
    SOCIAL_AUTH_TWITTER_SECRET = ''
    SOCIAL_AUTH_FACEBOOK_KEY = ''
    SOCIAL_AUTH_FACEBOOK_SECRET = ''

Con esto listo procedemos a migrar nuestros modelos :

    manage.py migrate

Ahora nos ubicamos en la carpeta "nodechat" y ejecutamos :

    npm install

Esto nos instalara las dependencias que utilizaremos, en este caso socket.io.

Ahora solo que arrancar nuestro proyecto :

    manage.py runserver

Y paralelamente en otra terminal, nos ubicamos en la carpeta "nodechat" para arrancar el archivo server.js :

    node server

Accedemos a "localhost:8000" y ahora solo queda logearnos con nuestras redes sociales y probar el chat.

![alt tag](https://scontent-a-mia.xx.fbcdn.net/hphotos-xpf1/t31.0-8/10974524_959214330762868_4896919565687488950_o.png)

![alt tag](https://fbcdn-sphotos-c-a.akamaihd.net/hphotos-ak-xaf1/t31.0-8/10498394_959214324096202_3195883505100474688_o.png)
