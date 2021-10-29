#!/bin/sh
NGINX=/usr/sbin/nginx
cd /home/polz/Webapp_v2/domain_lists
if [ -e domain_list.new ]
then
    cp domain_list domain_list.bak
    mv domain_list.new domain_list
    if $NGINX -t
    then
        echo "reloading config"
        $NGINX -s reload
    else
	cp domain_list.bak domain_list
    fi
fi
