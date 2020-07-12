import json, requests, re
import pandas as pd

# get a dictionary as a json object
# dictionary = json.loads(requests.get('https://raw.githubusercontent.com/adambom/dictionary/master/dictionary.json').text)
# print(dictionary)

dictionary = { # temporary dictionary to start testing the functionality
    'a':'def',
    'a':'def',
    'a':'def',
    'a':'def',
    'a':'def',
    'a':'def',
    'a':'def',
    'a':'def',
    'a':'def',
    'a':'def',
    'a':'def',
    'a':'def',

}


r = requests.get('https://data.iana.org/TLD/tlds-alpha-by-domain.txt', stream=True)

tlds = []

for line in r.iter_lines():
    if line: 
        tlds.append(line.decode())
    # print(tlds)
    
    
    
# tlds = pd.read_html('https://en.wikipedia.org/wiki/List_of_Internet_top-level_domains')
