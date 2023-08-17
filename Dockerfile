# Gebruik een basisimage met Java 8
FROM openjdk:8-jre-slim AS builder

# Gebruik Tomcat 9.0.76 als basisimage
FROM tomcat:9.0.76-jdk8-openjdk-slim

# Kopieer d WAR bestand naar de container
COPY ./warfiles/petclinic.war /usr/local/tomcat/webapps/

# De standaard commando van de Tomcat image start Tomcat al, dus je hoeft geen ENTRYPOINT te specificeren.
