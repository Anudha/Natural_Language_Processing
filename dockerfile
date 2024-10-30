# Use an official OpenJDK runtime as a parent image
FROM openjdk:11-jre-slim

# Set environment variables for Spark
ENV SPARK_VERSION=3.4.0
ENV HADOOP_VERSION=3
ENV SPARK_HOME=/opt/spark
ENV PATH=$PATH:$SPARK_HOME/bin:$SPARK_HOME/sbin

# Install required packages: wget, tar, PostgreSQL client, and other dependencies
RUN apt-get update && \
    apt-get install -y wget curl postgresql-client && \
    apt-get clean

# Download and install Apache Spark
#RUN wget https://dlcdn.apache.org/spark/spark-$SPARK_VERSION/spark-$SPARK_VERSION-bin-hadoop$HADOOP_VERSION.tgz && \
#    tar -xvzf spark-$SPARK_VERSION-bin-hadoop$HADOOP_VERSION.tgz && \
#    mv spark-$SPARK_VERSION-bin-hadoop$HADOOP_VERSION /opt/spark && \
#    rm spark-$SPARK_VERSION-bin-hadoop$HADOOP_VERSION.tgz


RUN wget https://archive.apache.org/dist/spark/spark-3.5.3/spark-3.5.3-bin-hadoop3.tgz && \
    tar -xvzf spark-3.5.3-bin-hadoop3.tgz && \
    mv spark-3.5.3-bin-hadoop3.tgz /opt/spark
#    rm spark-3.5.3-bin-hadoop3.tgz



# Expose ports for Spark UI and Web UI
EXPOSE 4040 8080 7077

# Default command to run Spark Shell
CMD ["/bin/bash"]

~                      
