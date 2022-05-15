import requests
from bs4 import BeautifulSoup

page = requests.get('https://www.wahlrecht.de/umfragen/dimap.htm')
soup = BeautifulSoup(page.content, "html.parser")


first_story_paragraph = soup.findAll("td", "s")

for child in first_story_paragraph:
    print(child.find_all_next())
    print('')

#for item in soup.select("td"):
    #print(item.get_text())