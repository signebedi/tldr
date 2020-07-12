import json, requests, re
import pandas as pd

def get_matches():
    # get a dictionary as a json object
    dictionary = json.loads(requests.get('https://raw.githubusercontent.com/adambom/dictionary/master/dictionary.json').text)

    # create empty list to store top level domains
    tlds = []
    
    # pull data from IANA
    r = requests.get('https://data.iana.org/TLD/tlds-alpha-by-domain.txt', stream=True)

    # iterate through text file and add to list
    for line in r.iter_lines():
        if line: 
            tlds.append(line.decode().lower())

    # create another empty list to store matches
    matches = []
    for word in dictionary.keys():
        for tld in tlds:
            if word.lower().endswith(tld):
                matches.append({word.lower():tld})

    return matches
    
def main():

    matches = get_matches()
    
    with open('output.txt', 'w') as f:
        f.write(str(matches))
        
        
        
if __name__ == '__main__':
    main()