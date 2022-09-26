#!/usr/bin/env bash

service openvswitch-switch start
ovs-vsctl set-manager ptcp:6640

cd /root/ryu/ryu/app && ryu-manager simple_switch_13.py ofctl_rest.py &

sleep 5
python topology.py
# mn 
# ovs-vsctl add-port br0 gre0 -- set interface gre0 type=gre options:remote_ip=172.17.0.4

service openvswitch-switch stop
