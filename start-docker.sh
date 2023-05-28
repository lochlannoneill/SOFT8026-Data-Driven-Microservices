#!/bin/bash

# stop all running containers
sudo sudo docker stop $(sudo docker ps -aq)
sleep 1

# remove all stopped containers
sudo sudo docker container prune -f
sleep 1

sudo sudo docker compose up --build

