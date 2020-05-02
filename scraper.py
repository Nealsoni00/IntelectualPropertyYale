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




data = requestPage()

print(data)
