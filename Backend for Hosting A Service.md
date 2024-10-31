Backend for Hosting A Service: cgroups /Docker / JRE / Spark / Hadoop / nginx / load testing

cgroups and namespaces are used to isolate software programs from seeing/accessing files, process ids, network connections. To get more information about cgroups on ubuntu OS: ls /sys/fs/cgroup/

Use a dockerfile to create a docker image. dockerfile is just a text file.
docker build .
31 sec to built the image
check the image exists 
run a container using the image and access the command line. use the -d flag instead of -it to run the container as a background process, not attaching it to the interactive shell or to stdout.
When a docker container is started, -p and -v flags can be used to map a host port to a container port, and a host file location mapped to a container location, i.e. mapping a docker volume to a docker container location. 
Ports and Volumes cannot be linked between hosts and containers when a container is already running. 
Container can be committed to an image, a way to save its current state, stopped, and a new container can be started with the latter image and a new config for ports, volume. 
For access to files inside a container, docker cp can be used while the container is running in which case files are copied from host to a location inside the container. There is no encryption or transfer over the internet in this copy. For example in scp, there is encryption and transfer over the internet. Docker cp ~  linux OS cp, except it executes via the daemon running as docker engine which has root privilege to access the file space in a container. Docker isolates run times by isolating namespaces and cgroups. 
another dockerfile
FROM openjdk:11-jre-slim
RUN apt-get update && \
apt-get install -y wget curl postgresql-client && \
apt-get clean
RUN wget https://archive.apache.org/dist/spark/spark-3.5.3/spark-3.5.3-bin-hadoop3.tgz && \
tar -xvzf spark-3.5.3-bin-hadoop3.tgz && \
mv spark-3.5.3-bin-hadoop3.tgz /opt/spark
# rm spark-3.5.3-bin-hadoop3.tgz
EXPOSE 4040 8080 7077
CMD ["/bin/bash"]
Finished building image in a vm in 57 sec
get the name of the image from docker images, run a container based on the image,and attach it to the terminal:
Questions about load testing nginx:
How to load test a web server. Send Xk requests in a short time, such as 5k requests in 10 seconds. There are tools to load test. A python script with requests lib should also work. Also leads to dos attack considerations. 
How to measure the results. Internally via access to the machine hosting the web server and externally from response time. Tools used to measure. 
Metrics that determine performance of the web server. Current config of cloud VM:

Data related - Total I/O per month 1 TB, Data in 40gb/sec, data out 1gb/sec
Memory - 1 Gb RAM, (Does HD matter?)
CPU - 1
file descriptors:
https://serverfault.com/questions/48717/practical-maximum-open-file-descriptors-ulimit-n-for-a-high-volume-system
