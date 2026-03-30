FROM apache/nifi:latest

USER root

# JDBC PostgreSQL
ADD https://jdbc.postgresql.org/download/postgresql-42.7.8.jar /opt/nifi/nifi-current/lib/postgresql-42.7.8.jar

# HDFS / Hadoop NARs
ADD https://repo1.maven.org/maven2/org/apache/nifi/nifi-hadoop-libraries-nar/2.8.0/nifi-hadoop-libraries-nar-2.8.0.nar /opt/nifi/nifi-current/lib/nifi-hadoop-libraries-nar-2.8.0.nar
ADD https://repo1.maven.org/maven2/org/apache/nifi/nifi-hadoop-nar/2.8.0/nifi-hadoop-nar-2.8.0.nar /opt/nifi/nifi-current/lib/nifi-hadoop-nar-2.8.0.nar

RUN chown nifi:nifi /opt/nifi/nifi-current/lib/postgresql-42.7.8.jar && \
    chown nifi:nifi /opt/nifi/nifi-current/lib/nifi-hadoop-libraries-nar-2.8.0.nar && \
    chown nifi:nifi /opt/nifi/nifi-current/lib/nifi-hadoop-nar-2.8.0.nar

USER nifi