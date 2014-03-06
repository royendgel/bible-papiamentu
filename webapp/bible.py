
import pymongo
import re
# put URI here
conn = pymongo.MongoClient(uri)
db = conn.biblepap
collbible = db.bible

f = open('BEIBEL.txt', 'r')
l = f.read().split('\r')
c = 0
emptyline = 0 
for lines in l:
	if len(lines) == 0:
		emptyline = emptyline + 1 
		continue
	lines = lines.lstrip()
	book = lines[0:3]
	bookIdent = lines[4:]
	passage = re.search('^\d*:\d* ', bookIdent)
	if passage != None:
		x = bookIdent[passage.start() : passage.end()].split(":")
		chapter = x[0]
		versus = x[1]
		bookre = re.search('^\d{1-3}', bookIdent)
		text = bookIdent[passage.end():]
		#collbible.insert({'kap' : chapter, 'vers' : versus, "text" : text, 'book' : book})
	else:
		print 'ok'
		break