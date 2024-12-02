# sdn-load-balancer
Performs load balancing on any fat tree topology using SDN Controller and OpenDaylight.

# Running OpenDaylight
./bin/karaf

feature:install odl-l2switch-switch

feature:install odl-restconf odl-mdsal-apidocs odl-dlux-all

# Creating and Running Custom Topoloy on Mininet
sudo mn --custom topology.py --topo mytopo --controller=remote,10.0.2.15,port=6633 --switch ovs,protocols=OpenFlow13


**Ensure network Connectivity**
pingall

# Topology

![Topology drawio (1)](https://github.com/user-attachments/assets/2c592085-0e40-4270-a3ab-14f8d1d0f661)

**Use Opendaylight UI to visualize the topology**

![ODL](https://github.com/user-attachments/assets/99149ded-b7b2-4c60-93df-cb53a77f93d0)

# Running ODL Load_balancer
python load_balancer_odl.py

Input Source and Destination hosts. The load_balancer will make rest call for obtaining topology information (Device ip & map, switch connection and port and link port mapping). Based on the toplogy information,
it will identify the shortest path with smallest link cost and push the flow of the shortest path. 

# Use Postman to visualize the flow rules and port mapping
GET http://10.0.2.15:8181/restconf/config/opendaylight-inventory:nodes/node/openflow:21

# Use mininet and wireshark to perform/validate the loadbalancing
Installation Tip:

sudo usermod -aG wireshark username

sudo chmod +x /usr/bin/dumpcap









