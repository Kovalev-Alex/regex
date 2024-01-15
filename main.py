from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv

with open("phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
# pprint(contacts_list)
structure = contacts_list[0]
for item in contacts_list[1:]:
    template = " ".join(item[:3]).strip(' ').split(',')[0]
    print()





