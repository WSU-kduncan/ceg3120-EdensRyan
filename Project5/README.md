Load balancing documentation
1, I logged into my proxy and both of my servers and added the private ip and name for my resources. The document now appears as below.
127.0.0.1 localhost
10.0.0.25 proxy
10.0.0.26  leroy
10.0.0.20 jenkins


# The following lines are desirable for IPv6 capable hosts
::1 ip6-localhost ip6-loopback
fe00::0 ip6-localnet
ff00::0 ip6-mcastprefix
ff02::1 ip6-allnodes
ff02::2 ip6-allrouters
ff02::3 ip6-allhosts
~

2, Each of the systems now has the private IP's of the others saved as their system name. With the private key correctly established in .ssh/id_rsa then going from 
from one system to another only takes the command ssh "systemName". For example ssh proxy or ssh jenkins.

3, The haproxy application was installed in the .yml file with the command "apt-get update && \ apt-get install -y git python3 python3-pip haproxy". It could also be installed after the fact with "sudo apt-get update" followed by "apt-get install haproxy".

The command built a folder in etc called haproxy and /etc/haproxy contains an errors folder and a haproxy.cfg file. I have renamed the .cfg file haproxy.cfg.old and  created a new blank haproxy.cfg file.

The new .cfg file has the following configuration
global
        maxconn 49999
        log /dev/log local0
        user haproxy
        group haproxy
        stats socket /run/haproxy/admin.sock user haproxy group haproxy mode 660 level admin
defaults
        timeout connect 10s
        timeout client 30s
        timeout server 30s
        log global
        mode tcp
        option tcplog
        macxonn 3000
frontend http_front
        bind *:80
        bind 10.0.0.25:80
        default_backend web_servers
backend web_servers
        balance roundrobin
        server leroy 10.0.0.26:80
        server jenkins 10.0.0.20:80
 
The commands to refresh the application without shutting down the system are "sudo systemctl stop haproxy.service" and sudo systemctl start haproxy.service"

The resources I used are https://linuxhint.com/how-to-install-and-configure-haproxy-load-balancer-in-linux/ and the lecture recordings

4, The nginx service was installed in the .yml file with the command apt-get update && \ apt-get install -y git nginx" 

The command built a folder in etc called nginx and populated a file in var/www/html with a default web page.

After several failed attempts at configurations as directed by various websites I realized that instead of bothering with sites-available and sites-enabled I could   accomplish this assignment by reconfiguring the default page with the pages provided.

sudo service nginx restart 

https://ubuntu.com/tutorials/install-and-configure-nginx#1-overview

My site http://52.44.15.101/

![image of server1](Images/S1.png)
![image of server2](Images/S2.png)

   
 
