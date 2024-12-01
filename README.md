# sdn-load-balancer
Performs load balancing on any fat tree topology using SDN Controller and OpenDaylight.

# Running OpenDaylight
./bin/karaf

feature:install odl-l2switch-switch
feature:install odl-restconf odl-mdsal-apidocs odl-dlux-all

# Creating and Running Custom Topoloy on Mininet
sudo mn --custom topology.py --topo mytopo --controller=remote,10.0.2.15,port=6633 --switch ovs,protocols=OpenFlow13
-- Ensure network Connectivity
pingall
--- Use Opendaylight UI to visualize the topology

