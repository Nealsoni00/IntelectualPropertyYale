import requests
from cookie import *
from bs4 import BeautifulSoup, NavigableString, Tag
import csv
import time


def requestPage(type, search):
	url = "https://github.com/search"
	querystring = {
		'q': search,
		'type': type
	}
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

def processPage(type, soup):
	# print(soup.prettify())
	body = soup.body
	# print(body.prettify())
	maincontent = body.find("div", {"class": "application-main"})
	# print(maincontent)
	pjax_container = body.find("main", {"id":"js-pjax-container"})
	
	nav = pjax_container.find("nav")
	menuOptions = nav.findAll("a", attrs={"class": "menu-item"})
	# print(menuOptions)
	

	for option in menuOptions:
		# for type in types: 
		if "type="+type in option['href']:
			if option.find("span"):
				size = option.find("span").contents[0]
				print(type, size)


		# types = ['type=Code']

	# print(nav)

types = ['Repositories', 
		 'Code', 
		 'Commits', 
		 'Issues',
		 'RegistryPackages', 
		 'Marketplace', 
		 'Topics', 
		 'Wikis', 
		 'Users']

for type in types:

	data = requestPage(type, 'MIT+License')
	processPage(type, data)

