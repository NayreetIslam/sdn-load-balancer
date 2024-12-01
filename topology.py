#!/usr/bin/python

from mininet.node import CPULimitedHost, Host, Node
from mininet.node import OVSKernelSwitch
from mininet.topo import Topo

class fatTreeTopo(Topo):

    "Fat Tree Topology"

    def __init__(self):
        "Create Fat tree Topology"

        Topo.__init__(self)

        #Add hosts
        h7 = self.addHost('h7', cls=Host, ip='10.0.0.7', defaultRoute=None)
        h8 = self.addHost('h8', cls=Host, ip='10.0.0.8', defaultRoute=None)
        h1 = self.addHost('h1', cls=Host, ip='10.0.0.1', defaultRoute=None)
        h2 = self.addHost('h2', cls=Host, ip='10.0.0.2', defaultRoute=None)
        h4 = self.addHost('h4', cls=Host, ip='10.0.0.4', defaultRoute=None)
        h3 = self.addHost('h3', cls=Host, ip='10.0.0.3', defaultRoute=None)
        h5 = self.addHost('h5', cls=Host, ip='10.0.0.5', defaultRoute=None)
        h6 = self.addHost('h6', cls=Host, ip='10.0.0.6', defaultRoute=None)

        #Add switches
        s6 = self.addSwitch('s6')
        s3 = self.addSwitch('s3')
        s9 = self.addSwitch('s9')
        s4 = self.addSwitch('s4')
        s10 = self.addSwitch('s10')
        s1 = self.addSwitch('s1')
        s7 = self.addSwitch('s7')
        s5 = self.addSwitch('s5')
        s8 = self.addSwitch('s8')
        s2 = self.addSwitch('s2')

        #Add links
        self.addLink(h1, s1)
        self.addLink(h2, s1)
        self.addLink(h3, s2)
        self.addLink(h4, s2)
        self.addLink(h5, s3)
        self.addLink(h6, s3)
        self.addLink(h7, s4)
        self.addLink(h8, s4)
        self.addLink(s1, s5)
        self.addLink(s5, s2)
        self.addLink(s1, s6)
        self.addLink(s2, s6)
        self.addLink(s3, s7)
        self.addLink(s4, s8)
        self.addLink(s7, s4)
        self.addLink(s3, s8)
        self.addLink(s5, s9)
        self.addLink(s7, s9)
        self.addLink(s6, s10)
        self.addLink(s8, s10)

topos = { 'mytopo': (lambda: fatTreeTopo() ) }
