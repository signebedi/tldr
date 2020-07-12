import json, requests
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

    # create another  list to store matches
    matches = {'word':[],'tld':[]}
    for word in dictionary.keys():
        for tld in tlds:
            if word.lower().endswith(tld):
                matches['word'].append(word.lower())
                matches['tld'].append(tld)

    return matches
    
def main():

    matches = get_matches()
    
    # convert output to a pandas df and write to csv
    df = pd.DataFrame(matches)
    df.to_csv('output.csv', index=False)
    
if __name__ == '__main__':
    main()