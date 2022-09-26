#!/bin/bash

# docker run --name server_container -p 7070:80 -d mininet_server_image -it --privileged -e DISPLAY \
#             -v /tmp/.X11-unix:/tmp/.X11-unix \
#             -v /lib/modules:/lib/modules

docker run --name server-container -p 7070:80 -it --rm --privileged -e DISPLAY \
    -v /tmp/.X11-unix:/tmp/.X11-unix \
    -v /lib/modules:/lib/modules \
    mininet-server


# docker run --name server_container -p 7070:80 -d mininet_server_image
