Current status: in progress

# InfrastructureAsCode
Infrastructure as code program using Ansible. Includes a managing portal written in Python. This program was created as an assignment for the module Infrastructure As Code (IAC), part of the Cloud Architecture and Automation (CAA) semester of Windesheim HBO-ICT / Infrastructure Design and Security

The basic idea of this project is to create and manage customers' VM's using a Python console program. This program runs on a Ubuntu host that contains all the customers' data. 

The VM's consist of: web-servers, database-servers and load-balancers. They're not being ran directly on the Ubuntu host. Instead they're deployed on ESXI-hosts, using Vagrant.

Ansible is utilised to deploy the specific types of servers. PowerCLI will be applied in the future to enable up-scaling.
