from lxml import html
import requests

page = requests.get('https://www.wahlrecht.de/umfragen/dimap.htm')
tree = html.fromstring(page.content)

scrape = tree.xpath('//td/text()')
list_with_integers = []
for i in range(len(scrape)):
    if scrape[i][0].isdigit():
        list_with_integers.append(scrape[i])
    #print(scrape[i])
    #if scrape[i][0] == ""
chunk_size = 10
chunked_list = []
for i in range(0, len(list_with_integers), chunk_size):
    chunked_list.append(list_with_integers[i:i+chunk_size])

for elem in chunked_list:
    print(elem)
