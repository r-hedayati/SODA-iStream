FROM ubuntu:20.04

LABEL Author="Reza Hedayati <ireza.hedayati@gmail.com>"
LABEL Version="1"
LABEL Description="This is custom Docker Image for running dash servers as mininet host"

USER root
WORKDIR /root

ENV TZ=US/Mountain
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

COPY ENTRYPOINT.sh /

RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    dnsutils \
    ifupdown \
    iproute2 \
    iptables \
    iputils-ping \
    mininet \
    net-tools \
    openvswitch-switch \
    openvswitch-testcontroller \
    tcpdump \
    vim \
    x11-xserver-utils \
    xterm \
    gcc \
    python-dev \
    libffi-dev \
    libssl-dev \
    libxml2-dev \
    libxslt1-dev \
    zlib1g-dev \
    git \
    nano \
    python3-pip \
    nginx \
 && rm -rf /var/lib/apt/lists/* \
 && touch /etc/network/interfaces \
 && chmod +x /ENTRYPOINT.sh

 RUN pip install ryu 
 RUN pip uninstall eventlet gunicorn -y
 RUN pip install eventlet==0.25.2 gunicorn==20.0.04 
 RUN git clone https://github.com/faucetsdn/ryu.git
 RUN git clone -b v0.1  https://github.com/Yang-Jace-Liu/dash-emulator.git && \
    cd dash-emulator && \
    pip3 install .

ADD server.py /root/
ADD /ServerFiles/* /var/www/html/

EXPOSE 6633 6653 6640 80 1935

ENTRYPOINT ["/ENTRYPOINT.sh"]

