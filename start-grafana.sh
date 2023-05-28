#!/bin/bash

sudo docker run -p 3000:3000 grafana/grafana

# Open a new terminal window and run the Grafana container in it
# gnome-terminal --tab -e "sudo docker run -p 3000:3000 grafana/grafana"

# open Grafana webpage
xdg-open http://localhost:3000
