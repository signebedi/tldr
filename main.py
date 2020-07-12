import json, requests, re
import pandas as pd

# get a dictionary as a json object
dictionary = json.loads(requests.get('https://raw.githubusercontent.com/adambom/dictionary/master/dictionary.json').text)
# print(dictionary)

# dictionary = { # temporary dictionary to start testing the functionality
#     'a':'def',
#     'com':'def',
#     'co':'def',
#     'aharry':'def',
#     'temporio':'def',
#     'shipsh':'def',
#     'tencom':'def',
#     'builde':'def',
#     'misc':'def',
#     'borg':'def',
#     'apple':'def',
#     'thas':'def',
# }

# tlds = pd.read_html('https://en.wikipedia.org/wiki/List_of_Internet_top-level_domains')
r = requests.get('https://data.iana.org/TLD/tlds-alpha-by-domain.txt', stream=True)

tlds = []

for line in r.iter_lines():
    if line: 
        tlds.append(line.decode().lower())
    # print(tlds)
    
# for word in dictionary.keys():
#     if word in tlds:
#         print(word)

# pat = "$|".join(tlds)

# for word in dictionary.keys():
#     print(word, ': ', re.findall(pat, word))
matches = []
for word in dictionary.keys():
    for tld in tlds:
        if word.lower().endswith(tld):
            matches.append({word.lower():tld})
# print(matches)

with open('output.txt', 'w') as f:
    f.write(str(matches))