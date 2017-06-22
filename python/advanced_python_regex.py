import re

fhand=open('faculty.csv').read()
degrees = dict()

for each in re.findall('(0|[A-Z][A-Za-z]?\.?[A-Z]\.?[A-Z]?[a-z]?)',fhand):
    each=each.replace('.','')
    degrees[each]=degrees.get(each,0)+1
print (degrees)

def emails(csv_file_name):
    emails = []
    emails=re.findall('[\w\.0-9]+@[\w\.0-9]+',open('faculty.csv').read())
    return emails

def domain_finder(emails):
    dm = set()
    for each in emails:
        domain = re.findall('@[^ ]+',each)
        dm.add(domain[0])
    return dm

def title(filename):
    import re
    title_count=dict()
    fhand = open(filename).read()

    titles=re.findall('.,(Ass.\S+|Prof.\S+|Aso.\S+)',fhand)
    for title in titles:
        title_count[title]=title_count.get(title,0)+1

    return (title_count)
