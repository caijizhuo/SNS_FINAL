import re

def get_country_codes(filename):
    with open(filename,'r') as f:
    data = f.read()
    pattern = re.compile(r'[a-z]{2}')
    new = pattern.findall(data)
    return new

