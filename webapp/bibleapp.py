# -*- coding: utf8 -*- 
from flask import Flask, session, request, redirect, g, jsonify, render_template, flash, Response, send_file
import pymongo
# put URI here
conn = pymongo.MongoClient(uri)
db = conn.biblepap
collbible = db.bible

app = Flask(__name__)

@app.route('/bisami/<buska>')
def buskaAlgu(buska):
	reg = buska
	b = collbible.find({'text' : {'$regex' : reg, '$options' : ['i']}})
	if b.count() == 0:
		return ' e texto ta mucho kortiko of mi no a hanje'
	return render_template('buska.html', b=b)


app.DEBUG = True
app.secret_key = 'dfsass'
if __name__ == "__main__":
    app.run(debug='TRUE', host='0.0.0.0')