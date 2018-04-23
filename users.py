import xml.etree.cElementTree as ET


def get_user(element):
    return 


def process_map(filename):
    users = set()
    for _, element in ET.iterparse(filename):
        if 'uid' in element.attrib:
            users.add(element.get('uid'))
   
    print(len(users))
    return users



if __name__ == "__main__":
    process_map('dallas.osm')
