# -*- coding: utf-8 -*-
"""
Created on Sun Apr 22 17:11:19 2018

@author: Kris
"""

import re

street_type_re = re.compile(r'\b\S+\.?$', re.IGNORECASE)

#https://en.wikipedia.org/wiki/Street_suffix
#https://pe.usps.com/text/pub28/28apc_002.htm
#https://en.wikipedia.org/wiki/Texas_State_Highway_Spur_408
expected = ['Alley', 'Annex', 'Arcade', 'Avenue', 'Bayou', 'Beach', 'Bend', 'Bluff', 'Bottom', 'Boulevard', 'Branch', 'Bridge',\
            'Brook', 'Burg', 'Bypass', 'Camp', 'Canyon', 'Cape', 'Causeway', 'Center', 'Circle', 'Cliff', 'Club', 'Common',\
            'Corner', 'Course', 'Court', 'Cove', 'Creek', 'Crescent', 'Crest', 'Crossing', 'Crossroad', 'Curve', 'Dale', \
            'Dam', 'Divide', 'Drive', 'Estate', 'Expressway', 'Extension', 'Fall', 'Ferry', 'Field', 'Flat', 'Ford', \
            'Forest', 'Forge', 'Fork', 'Fort', 'Freeway', 'Garden', 'Gateway', 'Glen', 'Green', 'Grove', 'Harbor', \
            'Haven', 'Heights', 'Highway', 'Hill', 'Hollow', 'Inlet', 'Island', 'Isle', 'Junction', 'Key', 'Knoll', \
            'Lake', 'Land', 'Landing', 'Lane', 'Light', 'Loaf', 'Lock', 'Lodge', 'Loop', 'Mall', 'Manor', 'Meadow', \
            'Mews', 'Mill', 'Mission', 'Motorway', 'Mount', 'Mountain', 'Neck', 'Orchard', 'Oval', 'Overpass', 'Park', \
            'Parkway', 'Pass', 'Passage', 'Path', 'Pike', 'Pine', 'Place', 'Plain', 'Plaza', 'Point', 'Port', 'Prairie', \
            'Radial', 'Ramp', 'Ranch', 'Rapid', 'Rest', 'Ridge', 'River', 'Road', 'Route', 'Row', 'Rue', 'Run', 'Shoal', \
            'Shore', 'Skyway', 'Spring', 'Spur', 'Square', 'Station', 'Stravenue', 'Stream', 'Street', 'Summit', 'Terrace', \
            'Throughway', 'Trace', 'Track', 'Trafficway', 'Trail', 'Trailer', 'Tunnel', 'Turnpike', 'Underpass', 'Union', 'Valley', \
            'Viaduct', 'View', 'Village', 'Ville', 'Vista', 'Walk', 'Wall', 'Way', 'Well', 'Wells', 'Via', 'Spur 408'] 


mapping = { "St": "Street",
            "St.": "Street",
            "Ave": "Avenue",
            "Av": "Avenue",
            "Rd": "Road",
            "Rd.": "Road",
            "road": "Road",
            "Blvd": "Boulevard",
            "blvd": "Boulevard",
            "Dr": "Drive",
            "Dr.": "Drive",
            "Expy": "Expressway",
            "LN": "Lane",
            "Ln": "Lane",
            "Pkwy": "Parkway",
            "Webb Chapel Rd 200": "Webb Chapel Road",
            "I-30": "Interstate 30",
            "I 30": "Interstate 30",
            "Blvd E": "Boulevard E",
            "West Main Street #B": "West Main Street",
            "7815 McCallum Blvd 14203 Dallas TX 75252 Kjo": "McCallum Boulevard",
            "I-20": "Interstate 20",
            "Forest Central Drive, Suite 300": "Forest Central Drive",
            "W Illinois Ave #306": "West Illinois Avenue",
            "North Market Street #102": "North Market Street",
            "75062": "",
            "North Saint Paul Street, Suite 2010": "North Saint Paul Street",
            "Canton Street, Suite 202": "Canton Street",
            "Las Colinas Blvd E": "Las Colinas Boulevard East",
            "Reunion Blvd E": "Reunion Boulevard East",
            "North Pearl Street, Suite 1150": "North Pearl Street"

            }

def update_name(name):
     m = street_type_re.search(name)
     street_type = m.group()

     if (street_type not in expected) & (street_type in mapping):
         
#https://lzone.de/examples/Python%20re.sub
         name = re.sub(street_type, mapping[street_type], name)
         

     return name