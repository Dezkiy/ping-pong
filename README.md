Simple client-server application Ping Pong.

Server respond "pong" on request "ping" from client.
Server based on falcon.

to start just run:
ansible-playbook -i hosts main.yml

to show dockers logs:
docker logs -f [server' or client' docker id]

to stop containers:
docker stop [server' docker id] [client' docker id]

tested on Ubuntu 20.04.1 LTS

https://falcon.readthedocs.io/
https://rapidapi.com/blog/best-python-api-frameworks/
