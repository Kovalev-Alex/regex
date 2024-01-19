from pprint import pprint
import csv
import re

with open("phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contact_list = list(rows)


def insert_to_contact_list():
    phonebook = dict()
    for item in contact_list[1:]:
        raw_names = item[0], item[1], item[2]
        name = ', '.join(raw_names).replace(',', '').split(" ")[:3]
        item[0], item[1], item[2] = name[0], name[1], name[2]
        data_dict = {
            'organization': item[3],
            'position': item[4],
            'phone': format_phone_number(item[5]),
            'email': item[6]
        }
        key = name[0], name[1], name[2]
        phonebook[key] = data_dict

    return phonebook


def format_phone_number(phone):
    pattern = r"\+?([7|8])\s?\(?(\d{3})\)?[\s-]?(\d{3,})\-?(\d{2,})\-?(\d{2,})\s?\(?(\w{3})?\.?\s?(\d{4})?\)?"
    new_format = re.sub(pattern, r"+7(\2) \3-\4-\5 \6 \7", phone)
    return new_format


def write_contacts():
    phonebook = insert_to_contact_list()
    with open("phonebook.csv", "w", encoding="utf-8", newline="") as file:
        datawriter = csv.writer(file, delimiter=",")
        datawriter.writerow(contact_list[0])
        datawriter.writerows(phonebook)


write_contacts()
# pprint(insert_to_contact_list())
