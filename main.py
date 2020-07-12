import json, requests, re
import pandas as pd

# get a dictionary as a json object
dictionary = json.loads(requests.get('https://raw.githubusercontent.com/adambom/dictionary/master/dictionary.json').text)
# print(dictionary)


tlds = pd.read_html('https://en.wikipedia.org/wiki/List_of_Internet_top-level_domains')

git config --global credential.helper store
