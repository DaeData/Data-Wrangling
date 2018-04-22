# -*- coding: utf-8 -*-
"""
Created on Sun Apr 22 17:11:19 2018

@author: Kris
"""

import re

street_type_re = re.compile(r'\b\S+\.?$', re.IGNORECASE)

#https://en.wikipedia.org/wiki/Street_suffix
#https://pe.usps.com/text/pub28/28apc_002.htm

expected = "Alley", "Annex", "Arcade", "Avenue", "Bayou", "Beach", "Bend", "Bluff", "Bottom", "Boulevard", "Branch", "Bridge", "Brook", "Burg", "Bypass", "Camp", "Canyon", "Cape", "Causeway", "Center", "Circle", "Cliff", "Club", "Common", "Corner", "Course", "Court", "Cove", "Creek", "Crescent", "Crest", "Crossing", "Crossroad", "Curve", "Dale", "Dam", "Divide", "Drive", "Estate", "Expressway", "Extension", "Fall", "Ferry", "Field", "Flat", "Ford", "Forest", "Forge", "Fork", "Fort", "Freeway", "Garden", "Gateway", "Glen", "Green", "Grove", "Harbor", "Haven", "Heights", "Highway", "Hill", "Hollow", "Inlet", "Island", "Isle", "Junction", "Key", "Knoll", "Lake", "Land", "Landing", "Lane", "Light", "Loaf", "Lock", "Lodge", "Loop", "Mall", "Manor", "Meadow", "Mews", "Mill", "Mission", "Motorway", "Mount", "Mountain", "Neck", "Orchard", "Oval", "Overpass", "Park", "Parkway", "Pass", "Passage", "Path", "Pike", "Pine", "Place", "Plain", "Plaza", "Point", "Port", "Prairie", "Radial", "Ramp", "Ranch", "Rapid", "Rest", "Ridge", "River", "Road", "Route", "Row", "Rue", "Run", "Shoal", "Shore", "Skyway", "Spring", "Spur", "Square", "Station", "Stravenue", "Stream", "Street", "Summit", "Terrace", "Throughway", "Trace", "Track", "Trafficway", "Trail", "Trailer", "Tunnel", "Turnpike", "Underpass", "Union", "Valley", "Viaduct", "View", "Village", "Ville", "Vista", "Walk", "Wall", "Way", "Well", "Wells" 


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
             "7815 McCallum Blvd 14203 Dallas TX 75252 Kjo": "McCallum Boulevard"
            }

def update_name(name):
     m = street_type_re.search(name)
     street_type = m.group()
     #print street_type
     if (street_type not in expected) & (street_type in mapping):
         print street_type
#https://lzone.de/examples/Python%20re.sub
         name = re.sub(street_type, mapping[street_type], name)
         print name

     return name