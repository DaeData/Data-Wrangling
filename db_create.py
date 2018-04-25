# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 17:11:15 2018

@author: elikr
"""
# this script creates the sqlite3 database, creates the tables in the db and imports the information from each of the csvs created in the xml to csv conversion process in data.py.
import csv, sqlite3
sql_file="dallas_metro.db"
  
con = sqlite3.connect(sql_file)
cur = con.cursor()

cur.execute('''DROP TABLE IF EXISTS nodes; ''')
con.commit()

cur.execute("CREATE TABLE nodes (id INTEGER PRIMARY KEY NOT NULL, lat REAL, lon REAL, user TEXT, uid INTEGER, version TEXT, changeset INTEGER, timestamp DATE);") # use your column names here
con.commit()

with open('nodes.csv','rb') as f: 
   
    data = csv.DictReader(f) 
    to_db = [(i['id'].decode("utf-8"),i['lat'].decode("utf-8"),i['lon'].decode("utf-8"),i['user'].decode("utf-8"),i['uid'].decode("utf-8"),i['version'].decode("utf-8"),i['changeset'].decode("utf-8"),i['timestamp'].decode("utf-8")) for i in data]
   

cur.executemany("INSERT INTO nodes (id, lat, lon, user, uid, version, changeset, timestamp) VALUES (?,?,?,?,?,?,?,?);", to_db,)
con.commit()

cur.execute('''DROP TABLE IF EXISTS ways; ''')
con.commit()

cur.execute("CREATE TABLE ways (id INTEGER PRIMARY KEY NOT NULL, user TEXT, uid INTEGER, version TEXT, changeset INTEGER, timestamp DATE);") # use your column names here
con.commit()

with open('ways.csv','rb') as f:
    
    data = csv.DictReader(f) 
    to_db = [(i['id'].decode("utf-8"),i['user'].decode("utf-8"),i['uid'].decode("utf-8"),i['version'].decode("utf-8"),i['changeset'].decode("utf-8"),i['timestamp'].decode("utf-8")) for i in data]
    

cur.executemany("INSERT INTO ways (id,user,uid,version,changeset,timestamp) VALUES (?,?,?,?,?,?);", to_db,)
con.commit()

cur.execute('''DROP TABLE IF EXISTS nodes_tags; ''')
con.commit()

cur.execute("CREATE TABLE nodes_tags (id INTEGER, key TEXT, value TEXT, type TEXT, FOREIGN KEY (id) REFERENCES nodes(id));") # use your column names here
con.commit()

with open('nodes_tags.csv','rb') as f: 

    data = csv.DictReader(f) 
    to_db = [(i['id'].decode("utf-8"),i['key'].decode("utf-8"),i['value'].decode("utf-8"),i['type'].decode("utf-8")) for i in data]
    

cur.executemany("INSERT INTO nodes_tags (id,key,value,type) VALUES (?,?,?,?);", to_db,)
con.commit()


cur.execute('''DROP TABLE IF EXISTS ways_tags; ''')
con.commit()

cur.execute("CREATE TABLE ways_tags (id INTEGER NOT NULL,key TEXT NOT NULL,value TEXT NOT NULL,type TEXT,FOREIGN KEY (id) REFERENCES ways(id));") # use your column names here
con.commit()

with open('ways_tags.csv','rb') as f: 
    data = csv.DictReader(f)
    to_db = [(i['id'].decode("utf-8"),i['key'].decode("utf-8"),i['value'].decode("utf-8"),i['type'].decode("utf-8")) for i in data]
    

cur.executemany("INSERT INTO ways_tags (id,key,value,type) VALUES (?,?,?,?);", to_db,)
con.commit()


cur.execute('''DROP TABLE IF EXISTS ways_nodes; ''')
con.commit()

cur.execute("CREATE TABLE ways_nodes (id INTEGER NOT NULL,node_id INTEGER NOT NULL, position INTEGER NOT NULL,FOREIGN KEY (id) REFERENCES ways(id),FOREIGN KEY (node_id) REFERENCES nodes(id));") 
con.commit()

with open('ways_nodes.csv','rb') as f: 
    data = csv.DictReader(f)
    to_db = [(i['id'].decode("utf-8"),i['node_id'].decode("utf-8"),i['position'].decode("utf-8")) for i in data]
    

cur.executemany("INSERT INTO ways_nodes (id,node_id, position) VALUES (?,?,?);", to_db,)
con.commit()
con.close()
