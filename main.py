#!/usr/bin/env python

import urllib2
from xml.dom import minidom
import sys

def boolean_to_status(boolean):
    if boolean:
        return 'online'
    return 'offline'

def get_xml_from_url(url):
    site = urllib2.urlopen(url)
    status = site.read()
    xmldoc = minidom.parseString(status)
    return xmldoc

def print_server_stats(url):
    xmldoc = get_xml_from_url(url)
    itemlist = xmldoc.getElementsByTagName('shard')
    for s in itemlist:
        print s.attributes['name'].value, ' : ', boolean_to_status(s.attributes['online'].value)

if __name__ == '__main__':
    EU_URL = 'http://status.riftgame.com/eu-status.xml'
    NA_URL = 'http://status.riftgame.com/na-status.xml'
    print '___EU_SERVER___'
    print_server_stats(EU_URL)

    print '___NA_SERVER___'
    print_server_stats(NA_URL)
