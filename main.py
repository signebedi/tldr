import json, requests, re
import pandas as pd

# get a dictionary as a json object
# dictionary = json.loads(requests.get('https://raw.githubusercontent.com/adambom/dictionary/master/dictionary.json').text)
# print(dictionary)


tlds = requests.get('https://data.iana.org/TLD/tlds-alpha-by-domain.txt')
for line in tlds:
    print(line)


# tlds = pd.read_html('https://en.wikipedia.org/wiki/List_of_Internet_top-level_domains')
