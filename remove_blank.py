# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 16:48:56 2018

@author: elikr
"""

files = ['nodes.csv','ways.csv', 'ways_tags.csv', 'nodes_tags.csv', 'ways_nodes.csv']
    
for filename in files:
    with open('{}_{}'.format('new',filename), 'w') as f_out:
        for line in open(filename):
            line = line.rstrip()
            if line != '':
                line = line + '\n'
                f_out.write(line)