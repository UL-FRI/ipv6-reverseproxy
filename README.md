# ipv6-reverseproxy

nginx config for an IPv4 -> IPv6 reverse proxy with SNA; scripts for adding hosts, ansible roles to install the config, etc.

The repo contains an optional web app for editing the list of server name entries.

# Using the reverse proxy

1. Set up an ipv6-accessible web server.
2. Add the AAAA record to your DNS.
3. Set up a reverse proxy from this repo.
4. Add the A record pointing to this reverse proxy to your DNS.
5. Create the host list
  5.1. When you have control over the reverse DNS for your reverse proxy's IP:
    5.1.1 Set your reverse lookup (PTR) entries - add the reverse entry for your new server.
    5.1.2 Run list\_from\_dns.sh to create the host list.
  5.2. When you rarely add hostnames, edit your hosts list manually.
  5.3. When you have multiple users and want to reduce your workload, use the flask webapp.

# Nginx config

The nginx config is split into multiple files.

The main config is in two files under `nginx/modules/fri\_reverseproxy.conf` and ˇnginx/sites/http\_forwardsˇ. These files use an include directive on a file (`domain\_list`) which contains a list of the form:

  firsthost.somedomain.net [2001:0DB8::1];
  secondhost.somedomain.net [2001:0DB8::2];
  otherhost.seconddomain.com [2001:0DB8::3];

That is all.

# Using the reverse DNS script

The list of hosts can be built by querying the reverse DNS pointer entries for the reverseproxy server's IP. If this script is run periodically, the proxy is configured pretty much as soon as the proper DNS entries are created.

# Using the web app

Install flask, configure uwsgi, use the flask app, Rejoice!

The flask app is under flask\_reverseproxy\_list.

To configure the app, change the values in config\_sample.py and rename it to config.py.

The web application presents the user with a simple entry field. The user enters the name of the server to be added to the domain\_list file. The web app checks whether the DNS entries for the server is correct and whether the domain is in the list of allowed domains.

# Installation instructions

## Using ansible



## Manually

See install.sh; use the files as inspiration.

# Further development

The flask app is simple, however, some may not wish to install the whole flask runtime just to run a reverse proxy.
Versions of the app using different technologies, would be gladly accepted. The same goes for various packaging efforts.

# Users

The main reason for this section is to provide something to update. Since various rankings are based on how "lively" a repo is, this list will be periodically updated. 

For now, the system is used at least by the following servers:

    doc.fri.uni-lj.si [2001:1470:fffd:ff91:a8c7:55ff:feda:4eea];
    zahteve.fri.uni-lj.si [2001:1470:fffd:ff91:9087:efff:fef7:1835];
    reverseproxy.fri1.uni-lj.si [2001:1470:fffd:ff91:144e:dfff:fe61:f56a];
    urnik-unitime.fri1.uni-lj.si [2001:1470:fffd:2073:fcf6:9bff:fe29:8a36];
    summerschool.fri.uni-lj.si [2001:1470:fffd:2073:6804:77ff:febd:91e7];
    apis-rilec.fri1.uni-lj.si [2001:1470:fffd:ff91:b45a:3ff:fe80:e81a];
    apis-rilec-js.fri1.uni-lj.si [2001:1470:fffd:ff91:b45a:3ff:fe80:e81a];
    apis-rilec-python.fri1.uni-lj.si [2001:1470:fffd:ff91:b45a:3ff:fe80:e81a];
    apis-rilec-php.fri1.uni-lj.si [2001:1470:fffd:ff91:b45a:3ff:fe80:e81a];
    vpn.fri1.uni-lj.si [2001:1470:fffd:ff91:382d:25ff:feac:3d5f];
    registrator.fri.uni-lj.si [2001:1470:fffd:ff91:b45a:3ff:fe80:e81a];
    reg.fri.uni-lj.si [2001:1470:fffd:ff91:b45a:3ff:fe80:e81a];
    helios-voting.fri1.uni-lj.si [2001:1470:fffd:ff91:b812:a8ff:fe1c:136b];
    apis-rilec-test.fri1.uni-lj.si [2001:1470:fffd:ff91:b45a:3ff:fe80:e81a];
    pracomul.si [2001:1470:fffd:202e:c1b7:56ff:fe93:6152];
    www.pracomul.si [2001:1470:fffd:202e:c1b7:56ff:fe93:6152];
    agora2021.fri1.uni-lj.si [2001:1470:fffd:ff91:f407:a1ff:fe8e:bc50];

