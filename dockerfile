# Imagen base de Ubuntu
FROM ubuntu:latest

# Actualizar el sistema e instalar dependencias necesarias
RUN apt-get update && apt-get install -y \
    apache2 \
    python3 \
    python3-pip \
    python3-venv \
    libapache2-mod-wsgi-py3 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Crear un entorno virtual para Python
RUN python3 -m venv /opt/venv

# Activar el entorno virtual y asegurar que sea utilizado
ENV PATH="/opt/venv/bin:$PATH"

# Instalar dependencias de Python en el entorno virtual
RUN pip install Flask pymongo

# Configuración de Apache
RUN echo "ServerName localhost" >> /etc/apache2/apache2.conf

RUN a2enmod wsgi

# Copiar la aplicación al contenedor
COPY ./app /var/www/app

# Copiar el archivo de configuración de Apache
COPY ./app/apache-flask.conf /etc/apache2/sites-available/000-default.conf

# Copiar el archivo WSGI
COPY ./app/app.wsgi /var/www/app/app.wsgi

# Establecer el directorio de trabajo
WORKDIR /var/www/app

# Exponer el puerto 80
EXPOSE 80

# Iniciar Apache en primer plano
CMD ["apache2ctl", "-D", "FOREGROUND"]
