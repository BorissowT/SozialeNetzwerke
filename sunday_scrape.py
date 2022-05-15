from lxml import html
import requests

page = requests.get('https://www.wahlrecht.de/umfragen/dimap.htm')
tree = html.fromstring(page.content)

scrape = tree.xpath('//td/text()')
list_with_integers = []
for i in range(len(scrape)):
    if scrape[i][0].isdigit():
        list_with_integers.append(scrape[i])

chunk_size = 10
chunked_list = []
for i in range(0, len(list_with_integers), chunk_size):
    chunked_list.append(list_with_integers[i:i+chunk_size])

# here we get only 12 last surveys
chunked_list_shortened = chunked_list[0:12]
named_dictionaries_for_responses = []

for elem in chunked_list_shortened:
    named_dictionaries_for_responses.append(
        {
            "date": elem[0],
            "CDU/CSU": elem[1],
            "SPD": elem[2],
            "GRUENE": elem[3],
            "FPD": elem[4],
            "LINKE": elem[5],
            "AfD": elem[6],
            "Sonstige": elem[7],
            "Befragte": elem[8],
            "Zeitraum": elem[9]
        }
    )

for elem in named_dictionaries_for_responses:
    print(elem)