#!/usr/bin/env python
# -*- coding: utf-8 -*-
import xml.etree.cElementTree as ET
import pprint
import re
"""
Your task is to explore the data a bit more.
The first task is a fun one - find out how many unique users
have contributed to the map in this particular area!

The function process_map should return a set of unique user IDs ("uid")
"""
import xml.etree.cElementTree as ET
import pprint

def get_user(element):
    return 


def process_map(filename):
    users = set()
    dup_att = {}
   
    for _, element in ET.iterparse(filename):
        if 'uid' in element.attrib:
            dup_attrib = element.get('uid')
            if dup_attrib in users:
                dup_att[dup_attrib] +=1
            else:
                users.add(element.get('uid'))
                dup_att[dup_attrib] = 1
        element.clear()
    for k,v in dup_att.items():
        print (k, v)
       
                
   

    return users




if __name__ == "__main__":
    process_map('dallas.osm')
