# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 18:43:42 2018

@author: Kris
"""

import xml.etree.cElementTree as ET
import pprint

"""
Your task is to explore the data a bit more.
The first task is a fun one - find out how many unique users
have contributed to the map in this particular area!

The function process_map should return a set of unique user IDs ("uid")
"""

def get_keys(element):
    return 


def process_map(filename):
    keys = set()
    for _, element in ET.iterparse(filename):
        if 'k' in element.attrib:
            keys.add(element.get('k'))
   

    return keys

def test():
    keys = process_map("sample.osm")
    pprint.pprint(keys)
    
if __name__ == "__main__":
    test()
    