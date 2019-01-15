##From https://medium.com/@rohitkhatana/deploying-django-app-on-aws-ecs-using-docker-gunicorn-nginx-c90834f76e21

############################################################
# Dockerfile to run a Django-based web application
# Based on an AMI
############################################################

# Set the base image to use to Ubuntu
FROM ubuntu:16.04 
#switched from 14.04

# Set the file maintainer (your name - the file's author)
MAINTAINER Lucas Brunner

# Set env variables used in this Dockerfile (add a unique prefix, such as DOCKYARD)
# Local directory with project source
ENV DOCKYARD_SRC=code/django_app
# Directory in container for all project files
ENV DOCKYARD_SRVHOME=/srv
# Directory in container for project source files
ENV DOCKYARD_SRVPROJ=$DOCKYARD_SRVHOME/$DOCKYARD_SRC

# Update the default application repository sources list
RUN apt-get update && apt-get -y upgrade
RUN apt-get install -y python python-pip
RUN apt-get install -y python-dev
RUN apt-get install -y libmysqlclient-dev
RUN apt-get install -y git
RUN apt-get install -y vim
RUN apt-get install -y mysql-server
RUN apt-get install -y nginx

# Create application subdirectories
WORKDIR $DOCKYARD_SRVHOME
RUN mkdir media static logs
#read
VOLUME ["$DOCKYARD_SRVHOME/media/", "$DOCKYARD_SRVHOME/logs/"]

# Copy application source code to SRCDIR
COPY $DOCKYARD_SRC $DOCKYARD_SRVPROJ

# Install Python dependencies
RUN pip install -r $DOCKYARD_SRVPROJ/requirement.txt

# Port to expose
EXPOSE 8000

# Copy entrypoint script into the image
WORKDIR $DOCKYARD_SRVPROJ
COPY ./docker-entrypoint.sh /
COPY ./django_nginx.conf /etc/nginx/sites-available/
RUN ln -s /etc/nginx/sites-available/django_nginx.conf /etc/nginx/sites-enabled
RUN echo "daemon off;" >> /etc/nginx/nginx.conf
ENTRYPOINT ["/docker-entrypoint.sh"]