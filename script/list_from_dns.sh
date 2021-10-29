#!/bin/sh

for IP in $(ip -4 addr | grep -oP '(?<=inet\s)\d+(\.\d+){3}');
do
    for HNAME in $(dig +short -x ${IP} | sed -e 's/\.$//'); 
    do
        IPV6S=$(dig +short -t AAAA ${HNAME})
	for ENDIPS in ${IPV6S};
        do
            echo "$HNAME [${ENDIPS}];";
	done
    done
done
