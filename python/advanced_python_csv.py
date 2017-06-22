import csv
import re

def emails(csv_file_name):
    emails = []
    emails=re.findall('[\w\.0-9]+@[\w\.0-9]+',open('faculty.csv').read())
    return emails

def write_to_csv(list_of_emails):
    import csv
    writer = csv.writer(open("emails.csv", "w"))
    writer.writerow(["Emails"])
    for each in list_of_emails:
        writer.writerow([each])

def domain_finder(emails):
    dm = set()
    for each in emails:
        domain = re.findall('@[^ ]+',each)
        dm.add(domain[0])
    return dm
