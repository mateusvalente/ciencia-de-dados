FROM apache/nifi:latest

USER root

ADD https://jdbc.postgresql.org/download/postgresql-42.7.8.jar /opt/nifi/nifi-current/lib/postgresql-42.7.8.jar

RUN chown nifi:nifi /opt/nifi/nifi-current/lib/postgresql-42.7.8.jar

USER nifi