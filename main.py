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
        key = name[0], name[1]
        phonebook2 = {
            'surname': name[2],
            'organization': item[3],
            'position': item[4],
            'phone': format_phone_number(item[5]),
            'email': item[6]
        }
        if phonebook.get(key):
            for value in phonebook.get(key):
                if item[2] in value.get("surname"):
                    value.update(
                        {key: phonebook2.get(key) for key in value if not value.get(key)}
                    )
                else:
                    phonebook.get(key).append(phonebook2)
        else:
            phonebook[key] = [phonebook2]

    return phonebook


def format_phone_number(phone):
    pattern = r"\+?([7|8])\s?\(?(\d{3})\)?[\s-]?(\d{3,})\-?(\d{2,})\-?(\d{2,})\s?\(?(\w{3})?\.?\s?(\d{4})?\)?"
    new_format = re.sub(pattern, r"+7 (\2) \3-\4-\5 \6 \7", phone)
    return new_format


def write_contacts():
    phonebook = insert_to_contact_list()
    with open("phonebook.csv", "w", encoding="utf-8", newline="") as file:
        datawriter = csv.DictWriter(file, fieldnames=contact_list[0], delimiter=",")
        datawriter.writeheader()
        for key, value_list in phonebook.items():
            for value in value_list:
                datawriter.writerow(
                    {
                        "lastname": key[0],
                        "firstname": key[1],
                        "surname": value.get("surname"),
                        "organization": value.get("organization"),
                        "position": value.get("position"),
                        "phone": value.get("phone"),
                        "email": value.get("email"),
                    }
                )


if __name__ == "__main__":
    write_contacts()
