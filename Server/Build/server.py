#!/usr/bin/python

"""Custom topology example
"""
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSController
from mininet.node import CPULimitedHost, Host, Node
from mininet.node import OVSKernelSwitch, UserSwitch
from mininet.node import IVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import TCLink, Intf
from subprocess import call
from time import sleep
from mininet.term import makeTerms, makeTerm, runX11
import os



class SingleSwitchTopo(Topo):
    "Single switch connected to n hosts."
    def build(self):
        #s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')
        #s3 = self.addSwitch('s3')
        #s4 = self.addSwitch('s4')
        #h1 = self.addHost('h1', mac="00:00:00:00:00:01")
        #h2 = self.addHost('h2', mac="00:00:00:00:00:02")
        #h1 = self.addHost('h1', mac="00:00:00:00:00:01", ip="10.0.0.1")
        #h2 = self.addHost('h2', mac="00:00:00:00:00:02", ip="10.0.0.2")
        #h3 = self.addHost('h3', mac="00:00:00:00:00:03", ip="10.0.0.3")
        h4 = self.addHost('h4', mac="00:00:00:00:00:04", ip="10.0.0.4")
        h5 = self.addHost('h5', mac="00:00:00:00:00:05", ip="10.0.0.5")
# if bw=... added the queue won't work.
        self.addLink(h4, s2)
        self.addLink(h5, s2)

if __name__ == '__main__':
    setLogLevel('info')
    topo = SingleSwitchTopo()
    c1 = RemoteController('c1', ip='172.17.0.2')
    net = Mininet(topo=topo, controller=c1, link=TCLink)
    net.start()
    #sleep(5)
    #net.pingAll()

    #sleep(10)

    hosts=net.hosts
    print(hosts)

    os.system('ovs-vsctl add-port s2 gres -- set interface gres type=gre options:remote_ip=172.17.0.4')
    #hosts[0].cmdPrint('ifconfig h1-eth0 mtu 1400 up')
    #sleep(5)

    hostNumber=5
    for host in hosts:
        for i in range(1, hostNumber+1):
            if i < 10:
                host.cmdPrint('arp -s 10.0.0.{} 00:00:00:00:00:0{}'.format(i,i))
            if i >=10:
                host.cmdPrint('arp -s 10.0.0.{} 00:00:00:00:00:{}'.format(i,i))

    #print("sleep....")
    #sleep(30)
    #hosts[0].cmdPrint('python3 -m dash_emulator.main http://10.0.0.3/live.mpd --output /root/result -y')
    hosts[0].cmdPrint('nginx')
    hosts[1].cmdPrint('nginx')
    CLI(net)
    net.stop()
