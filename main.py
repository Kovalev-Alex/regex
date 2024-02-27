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

        phonebook[name[0], name[1], name[2]] = {
            'organization': item[3],
            'position': item[4],
            'phone': format_phone_number(item[5]),
            'email': item[6]
        }
    return phonebook
# new_contact = [y if x="" else x for x,y in zip(contact_1, contact_2)]


def format_phone_number(phone):
    pattern = r"\+?([7|8])\s?\(?(\d{3})\)?[\s-]?(\d{3,})\-?(\d{2,})\-?(\d{2,})\s?\(?(\w{3})?\.?\s?(\d{4})?\)?"
    new_format = re.sub(pattern, r"+7 (\2) \3-\4-\5 \6 \7", phone)
    return new_format


def create_list(list_):
    phonebook_new = []
    for k, v in list_.items():
        name = k[:2]
        person = []
        if name:
            person.append(', '.join(k[:3]).strip())
            person.append(v['organization'].strip())
            person.append(v['position'].strip())
            person.append(v['phone'].strip())
            person.append(v['email'].strip())

        # print(phonebook_new.index(name))
        phonebook_new.append(person)
    return phonebook_new


def write_contacts():
    phonebook = create_list(insert_to_contact_list())
    with open("phonebook.csv", "w", encoding="utf-8", newline="\n") as file:
        datawriter = csv.writer(file, delimiter=",")
        datawriter.writerow(contact_list[0])
        datawriter.writerows(phonebook)


write_contacts()
