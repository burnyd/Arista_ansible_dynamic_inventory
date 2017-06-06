This is a exmaple of how to use the CVP API to pull back a python list to a ansible dynamic inventory.  Some examples...

root@Ubuntu16-04:/opt/projects/dynamic_ansible# ansible all -i cvpdynamic_api.py -m ping
l1.arista.test | SUCCESS => {
    "changed": false, 
    "ping": "pong"
}
spine1.arista.test | SUCCESS => {
    "changed": false, 
    "ping": "pong"
}
leaf2.arista.test | SUCCESS => {
    "changed": false, 
    "ping": "pong"
}
leaf3.arista.test | SUCCESS => {
    "changed": false, 
    "ping": "pong"
}
leaf4.arista.test | SUCCESS => {
    "changed": false, 
    "ping": "pong"
}
spine2.arista.test | SUCCESS => {
    "changed": false, 
    "ping": "pong"
}

Running as a ansible-playbook with the lldp_neighbors.yaml to find lldp neighbors based off of cvp.

root@Ubuntu16-04:/opt/projects/dynamic_ansible# ansible-playbook -i cvpdynamic_api.py lldp_neighbors.yaml -v | sed 's/\\n/\n/g'
Using /etc/ansible/ansible.cfg as config file

PLAY [arista] ******************************************************************

TASK [find all lldp neighbors] *************************************************
ok: [leaf2.arista.test] => {"changed": false, "stdout": ["Last table change time   : 0:32:36 ago
Number of table inserts  : 9
Number of table deletes  : 0
Number of table drops    : 0
Number of table age-outs : 0

Port       Neighbor Device ID               Neighbor Port ID           TTL
Et1        leaf1.********.test                Ethernet1                  120
Et2        spine1.********.test               Ethernet3                  120
Et3        spine2.********.test               Ethernet3                  120
Et5        leaf1.********.test                Ethernet5                  120
Ma1        leaf1.********.test                Management1                120
Ma1        leaf4.********.test                Management1                120
Ma1        leaf3.********.test                Management1                120
Ma1        spine1.********.test               Management1                120
