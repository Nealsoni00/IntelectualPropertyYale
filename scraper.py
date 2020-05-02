import requests
from cookie import *
from bs4 import BeautifulSoup, NavigableString, Tag
import csv
import time


def requestPage():
	url = "https://github.com/search?q=MIT+License&type=Code"
	querystring = {}
	payload = {}
	headers = {
		'Cookie': cookie,
		'User-Agent': "PostmanRuntime/7.20.1",
		'Accept': "*/*",
		'Cache-Control': "no-cache",
		'cache-control': "no-cache"
		}

	response = requests.request("GET", url, headers=headers, params=querystring, data = payload)
	html_content = response.text
	soup = BeautifulSoup(html_content, "lxml")
	return soup

def processPage(soup):
	# print(soup.prettify())
	body = soup.body
	# print(body.prettify())
	maincontent = body.find("div", {"class": "application-main"})
	# print(maincontent)
	pjax_container = body.find("main", {"id":"js-pjax-container"})
	
	nav = pjax_container.find("nav")
	menuOptions = nav.findAll("a", attrs={"class": "menu-item"})
	# print(menuOptions)
	types = ['type=Repositories', 
			 'type=Code', 
			 'type=Commits', 
			 'type=Issues',
			 'type=RegistryPackages', 
			 'type=Marketplace', 
			 'type=Topics', 
			 'type=Wikis', 
			 'type=Users']

	for option in menuOptions:
		for type in types: 
			if type in option['href']:
				if option.find("span"):
					size = option.find("span").contents
					print(type, size)

		# types = ['type=Code']

	# print(nav)




data = requestPage()

processPage(data)

