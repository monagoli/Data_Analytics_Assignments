from flask import Flask, render_template,jsonify,redirect
from flask_pymongo import PyMongo
from scrape_mars import scrape

app=Flask(__name__)
mongo = PyMongo(app) #this is creating the database

@app.route('/')
def home():
	mars_info=mongo.db.mars_info.find_one()
	return render_template('index.html',dict=mars_info)

@app.route('/scrape')
def scrapeAgain():
	fresh_info=scrape()
	collection.update({'$set':fresh_info},upsert=True)
	return('*refreshing data*')

if __name__ == '__main__':
    app.run(debug=True)
	
	

