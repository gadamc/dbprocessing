#!/usr/bin/env python

from TierProcess import *
from couchdbkit import Server, Database

s = Server('http://127.0.0.1:5984')
db = s['testdb']
doc = db.get('tsupertestid111')
tier = {}
tier['newfile'] = 'newfile.txt'
tier['hostname'] = '12.12.12.12'
mcp = RemoteCopyProcess('http://127.0.0.1:5984', 'testdb', 'sccopy0')
mcp.doprocess(doc, tier, 'testfile.txt','adam@134.158.176.27','newfile.txt')

