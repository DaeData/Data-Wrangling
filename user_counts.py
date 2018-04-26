#!/usr/bin/env python
# -*- coding: utf-8 -*-
import xml.etree.cElementTree as ET



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
