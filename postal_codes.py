import xml.etree.cElementTree as ET
from collections import defaultdict
import re
import pprint

OSMFILE = "sample.osm"
#street_type_re = re.compile(r'\b\S+\.?$', re.IGNORECASE)
postal_code_re = re.compile(r'^\d{5}$')
#http://regexlib.com/

def audit_postal_code(postal_types,postal_code):
    if not re.match(postal_code_re, postal_code):
        postal_types[postal_type].add(postal_code)


def is_postal_code(elem):
    return (elem.attrib['k'] == "addr:postcode")


def audit(osmfile):
    osm_file = open(osmfile, "r")
    postal_types = defaultdict(set)
    for event, elem in ET.iterparse(osm_file, events=("start",)):

        if elem.tag == "node" or elem.tag == "way":
            for tag in elem.iter("tag"):
                if is_postal_code(tag):
                    audit_postal_code(postal_types, tag.attrib['v'])
    osm_file.close()
    return postal_types




def test():
    pc_types = audit(OSMFILE)

    pprint.pprint(dict(pc_types))



if __name__ == '__main__':
    test()