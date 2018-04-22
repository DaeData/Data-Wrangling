# -*- coding: utf-8 -*-
"""
Created on Thu Apr  5 00:46:25 2018

@author: Kris
"""
import xml.etree.cElementTree as ET
import pprint

def get_user(element):
    return 


def process_map(filename):
    users = set()
    for _, element in ET.iterparse(filename):
        if 'uid' in element.attrib:
            users.add(element.get('uid'))
   

    return users


def test():

    users = process_map('sample.osm')
    pprint.pprint(users)




if __name__ == "__main__":
    test()