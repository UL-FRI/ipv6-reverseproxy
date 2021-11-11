#!/bin/sh

HNAMES=""
for IP in $(ip -4 addr | grep -oP '(?<=inet\s)\d+(\.\d+){3}');
do
    for HNAME in $(dig +short -x ${IP} | sed -e 's/\.$//' | sort | uniq); 
    do
        HNAMES="$HNAMES\n$HNAME"
    done
done
for HNAME in $(echo $HNAMES | sort | uniq);
do
    # ENDIP=$(dig +short -t AAAA ${HNAME} | head -n 1) # this does not work for cnames
    ENDIP=$(dig +nocmd ${HNAME} AAAA +noall +answer | grep -P 'IN[[:space:]]AAAA[[:space:]][a-f0-9:]*$' | sed -e 's/.*AAAA[\t ]//' | head -n 1)
    if [ -n "$ENDIP" ];
    then
        echo "$HNAME [${ENDIP}];";
    fi
done
