#Installation method for  docker-compose

sudo curl -L https://github.com/docker/compose/releases/download/1.29.2/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose

sudo chmod +x /usr/local/bin/docker-compose

docker-compose –version

Should get an output similar to below:

[docker]$ docker-compose --version
docker-compose version 1.29.2, build 5becea4c
[docker]$


