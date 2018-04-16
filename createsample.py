# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 14:55:49 2018

@author: Kris
"""
from xml.etree.ElementTree import ElementTree, Element, tostring
import xml.etree.ElementTree as ET

#define the destination file.
def d_file_out(filename, f_type):
    file_var_out = open(filename, f_type)
    return file_var_out
#define the source file.
def d_file_in(filename, f_type):
    file_var_in = open(filename, f_type)
    return file_var_in


def get_element(d_in, tags=('node', 'way', 'relation')):
   #Yield element if it is the right type of tag
    context = ET.iterparse(d_in, events=('start', 'end'))
    _, root = next(context)
    for event, elem in context:
        if event == 'end' and elem.tag in tags:
            yield elem
            root.clear()
          
#create the sample file.
def sample_data(inputfile, outputfile):
    outputfile.write('<?xml version="1.0" encoding="UTF-8"?>\n')
    outputfile.write('<osm>\n  ')
    #capture every 100th entry, starting at entry 100.
    for num, row in enumerate(get_element(inputfile), 100):
        if num % 100 == 0:
            outputfile.write(ET.tostring(row, encoding='utf-8', method='xml'))
    outputfile.write('</osm>')
"""  Reference:
    http://stackoverflow.com/questions/3095434/inserting-newlines-in-xml-file-generated-via-xml-etree-elementtree-in-python
    """
    
    
d_in = d_file_in("dallas.osm", 'r')
d_out = d_file_out("sample.osm", 'w')
sample_data(d_in, d_out)

d_in.close()
d_out.close()
