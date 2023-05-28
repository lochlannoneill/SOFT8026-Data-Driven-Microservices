#!/bin/bash

# Run start-docker.sh in a new terminal window
gnome-terminal --tab --title="Docker" --command="bash -c './start-docker.sh; $SHELL'"

sleep 10
# Run start-grafana.sh in a new terminal window
gnome-terminal --tab --title="Grafana" --command="bash -c './start-grafana.sh; $SHELL'"

