#!/bin/bash

docker run --name container-topology -it --rm --privileged -e DISPLAY \
    -v /tmp/.X11-unix:/tmp/.X11-unix \
    -v /lib/modules:/lib/modules \
    mininet-topology
