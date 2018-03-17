import time
from bs4 import BeautifulSoup as bs
import requests
from splinter import Browser
from selenium import webdriver
import pandas as pd
import tweepy


def browser():
	executable_path = {'executable_path': '/Users/monaderakhshan/Documents/chromedriver'}
	browser = Browser('chrome', **executable_path, headless=False)

def scrape():
	browser=browser()

	scraping_dictionary={}

	# mars news

	url = 'https://mars.nasa.gov/news/?page=0&per_page=15&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
	browser.visit(url)
	html=browser.html
	soup=bs(html,'html.parser')
	first_entry=nasa.find('div',class_='features')
	news_p=first_entry.find('div',class_='rollover_description_inner').text.strip()
	news_title=first_entry.find('div',class_='content_title').text.strip()

	scraping_dictionary['news_title']=news_title
	scraping_dictionary['news_paragraph']=news_p

	
	#featured image

	url_jpl = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
	browser.visit(url_jpl)
	html_image = browser.html
	soup = bs(html_image, 'html.parser')
	results = soup.find("div", {"id":"main_container"})
	featured_image_url = results.find_all('a')

	scraping_dictionary['featured_image_url']=featured_image_url

	# mars weather
	consumer_key='mB5iv7BJk5G4yY1P9FxZ7jT8U'
	consumer_secret='2McfxyFLkOj0p5oYTYUePJBRSp36GwY4vylEUuayE5jaU0eJS4'
	access_token='361530585-6bFemMZLwEKjxa6bAZOzeOLEhUCrTVINjB4d1vTW'
	access_token_secret='hPrCNQWn8N36285KJHvkMjWv8Y8434IB4DgBNIUEDR47L'

	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())
	target_user = "marswxreport"
	tweet = api.user_timeline(target_user , count = 1)
	mars_weather=tweet[0]['text']
	scraping_dictionary['full tweet']=mars_weather

	#mars facts 
	data = pd.read_html('https://space-facts.com/mars/')
	mars_facts=pd.DataFrame(data[0])
	mars_facts.columns=['Mars','Data']
	mars_facts.set_index('Mars')
	mars_facts=mars_facts.to_html(classes='mars_facts')
	mars_facts=mars_facts.replace('\n',' ')
	scraping_dictionary['facts']=mars_facts

	#mars hemispheres
	hemi_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
	browser.visit(hemi_url)

	html = browser.html
	soup = bs(html, 'html.parser')
	hemis=[]
	for i in range (4):
	    images = browser.find_by_tag('h3')
	    images[i].click()
	    html = browser.html
	    soup = bs(html, 'html.parser')
	    src = soup.find("img", class_="wide-image")["src"]
	    img_title = soup.find("h2",class_="title").text
	    url = 'https://astrogeology.usgs.gov'+ src
	    dictionary={"title":img_title,"img_url":url}
	    hemis.append(dictionary)
	    browser.back()

	scraping_dictionary['hemispheres']=hemis








		