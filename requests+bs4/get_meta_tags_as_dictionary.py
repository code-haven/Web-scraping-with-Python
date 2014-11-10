import requests
from bs4 import BeautifulSoup
import sys

try:
	domain = sys.argv[1]
except IndexError:
	print("Couldn't obtain domain name\nUsage: python <file.py> <domain_name>")
	exit(0)

request = requests.get(domain)

soup = BeautifulSoup(request.content)

all_meta_tags = soup.findAll('meta', content=True)

meta_dictionary = {}

if all_meta_tags == None:
	print 'No Meta tags found'

else:
	print('{')
	for meta_tag in all_meta_tags:
	    try:
	        print('%s : %s,' % (meta_tag['name'], meta_tag['content']))
	    except:
	        pass            #Ignore invalid meta tags
	print('}')