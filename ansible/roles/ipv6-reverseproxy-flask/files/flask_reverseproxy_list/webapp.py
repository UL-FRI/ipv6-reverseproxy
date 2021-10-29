#!/usr/bin/env python3

from flask import Flask
from flask import flash
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for

import crypt
import dns.resolver
import subprocess
import pwd
import random
import shutil
import string

import config

def check_entry(domain):
    print("adding: %s" % (domain))
    try:
        resolver = dns.resolver.Resolver()
        resolver.nameservers = config.NAMESERVERS
    except Exception as e:
        print('    error connecting to DNS: %s' % (e))
    try:
        ipv4 = resolver.query(domain, 'a')[0].address
    except Exception as e:
        print('    error resolving IPv4: %s' % (e))
    try:
        ipv6 = resolver.query(domain, 'aaaa')[0].address
    except Exception as e:
        print('    error resolving IPv6: %s' % (e))
    try:
        assert ipv4 == config.IPV4_ADDR
        return ipv6
    except Exception as e:
        print('    Wrong IPv4 entry (%s != %s)' % (ipv4, config.IPV4_ADDR))
    return None


def add_entry(domain, ipv6):
    shutil.copyfile('domain_lists/domain_list', 'domain_lists/domain_list.new')
    pos = None
    domainstr = '    ' + domain + ' '
    ipv6str = "[{}];".format(ipv6)
    with open('domain_lists/domain_list.new', 'r+') as f:
        while True:
            fpos = f.tell()
            s = f.readline()
            if len(s) == 0:
            # end of file reached
                print("Add new: " + domainstr + ipv6str)
                f.write(domainstr + ipv6str + "\n")
                break
            domainlen = len(s) - len(ipv6str) - 1
            if s[:domainlen] == domainstr:
                f.seek(fpos + domainlen)
                f.write(ipv6str)
                print("Fix: " + domainstr)
                break
    return True


def forb(domain):
    for allowed in config.ALLOWED:
        if domain.endswith(allowed):
            return False
    return True

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/added', methods = ['GET', 'POST'])
def added():
    return render_template('added.html')

@app.route('/failed')
def failed():
    return render_template('failed.html')

@app.route('/empty')
def empty():
    return render_template('empty.html')

@app.route('/forbidden')
def forbidden():
    return render_template('forbidden.html')

@app.route('/form', methods = ['POST'])
def test_dns_entry():
    domain = request.form['domain']
    if not domain:
        return redirect(url_for('empty'))
    if forb(domain):
        return redirect(url_for('forbidden'))
    ipv6 = check_entry(domain)
    if ipv6 is not None:
        if add_entry(domain, ipv6):
            return redirect(url_for('added'))
    return redirect(url_for('failed'))

if __name__ == '__main__':
    app.run(debug = True, host = config.IP, port = config.PORT)
