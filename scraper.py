import requests
from cookie import *
from bs4 import BeautifulSoup, NavigableString, Tag
import csv
import time
import re

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
	
	if pjax_container == None:
		return {'type': type, 'count': 0, 'codeDist': {}}

	nav = pjax_container.find("nav")
	menuOptions = nav.findAll("a", attrs={"class": "menu-item"})
	# print(menuOptions)
	
	for option in menuOptions:
		# for type in types: 
		if "type="+type in option['href']:
			if option.find("span"):
				size = option.find("span").contents[0]
				# print(type, size.replace(',','').replace('K','000').replace('M','000000'))

	rightSide = pjax_container.find("div", {"class": "codesearch-results"})

	exactNum = 0
	
	topText = rightSide.find("span", {"class":"v-align-middle"})
	if topText and topText.contents:
		strippedstring = topText.contents[0].strip().replace(',','').replace('K','000').replace('M','000000')
		num = re.findall("\d+",strippedstring)
		if (num and num[0]):
			exactNum =  num[0]

	topText = rightSide.find("h3")

	if topText and topText.contents:
		strippedstring = topText.contents[0].strip().replace(',','').replace('K','000').replace('M','000000')
		num = re.findall("\d+",strippedstring)
		if (num and num[0]):
			exactNum =  num[0]

	# get languages
	codeDist = {}
	listCotainer = pjax_container.find("ul", attrs={"class": "filter-list"})
	if listCotainer:
		listOfCodes = listCotainer.findAll("li")
		
		for codeType in listOfCodes:
			container = codeType.find('a', {"class": "filter-item"})
			count = container.find('span', {"class": "count"})
			code = container.text.strip().split('\n              ')
			if len(code) >= 2:
				codeDist[code[1]] = code[0]
	return {'type': type, 'count': exactNum, 'codeDist': codeDist}



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

codeLicenses = ['MIT License', 
			   'Apache License', 
			   'GPLv3', 
			   'BSD 2-clause',
			   'BSD 3-clause',
			   'GPLv2', 
			   'GPLv2.1',
			   'LGPLv2.1',
			   'LGPLv3', 
			   'Mozilla Public License',
			   'The Unilicense',
			   'Boost Software License',
			   'Pre-Release Software']

nonCodeLicenses = ['CC0-1.0', 'CC-BY-4', 'CC-BY-SA-4']

copyright = ['copyright']

allLicenses = sum([codeLicenses,nonCodeLicenses,copyright],[])
print(allLicenses)
scrapedData = {}

for codeLicense in allLicenses:
	licenseData = {}
	for type in types:
		data = requestPage(type, codeLicense)
		licenseData[type] = processPage(type, data)
	scrapedData[codeLicense] = licenseData
	print(scrapedData)

print(scrapedData)
