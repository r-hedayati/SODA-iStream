#!/usr/bin/env bash

service openvswitch-switch start
ovs-vsctl set-manager ptcp:6640

sleep 5
python server.py

service openvswitch-switch stop
