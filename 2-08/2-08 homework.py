from pprint import pprint
import re
import csv

with open("phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
    # pprint(contacts_list)
d = dict()
for x in contacts_list[1:]:
    j = ','.join(x)
    regex = r"(([А-ЯЁ][а-яё]*)\s*\,?([А-ЯЁ][а-яё]*)\s*\,?([А-ЯЁ][а-яё]*|)\s*),{1,3}(.*),(.*),(((\+7|8)\s?\(?(\d+)\)?\-?\s?(\d*)\-?\s?(\d*)\-?\s?(\d*)\-?\s?\(?([доб]*)\.?\s?(\d*)\)?|).*),(.*\@?\w*)"
    # https://regex101.com/r/vTzXwU/1
    subst = "\\2,\\3,\\4,\\5,\\6,\\9\\10\\11\\12\\13,\\15,\\16"
    result = re.sub(regex, subst, j, 0)
    r = result.split(',')
    d_key_name = r[0] + r[1]
    if d_key_name in d:
        for _ in d[d_key_name]:
            if d[d_key_name]['lastname'] == '': d[d_key_name]['lastname'] = r[0]
            if d[d_key_name]['firstname'] == '': d[d_key_name]['firstname'] = r[1]
            if d[d_key_name]['surname'] == '': d[d_key_name]['surname'] = r[2]
            if d[d_key_name]['organization'] == '': d[d_key_name]['organization'] = r[3]
            if d[d_key_name]['position'] == '': d[d_key_name]['position'] = r[4]
            if d[d_key_name]['phone'] == '': d[d_key_name]['phone'] = r[5]
            if d[d_key_name]['dob_phone'] == '': d[d_key_name]['dob_phone'] = r[6]
            if d[d_key_name]['email'] == '': d[d_key_name]['email'] = r[7]
    else:
        d[d_key_name] = {
            'lastname': r[0],
            'firstname': r[1],
            'surname': r[2],
            'organization': r[3],
            'position': r[4],
            'phone': r[5],
            'dob_phone': r[6],
            'email': r[7],
        }
# pprint(d)
l = list()
for k, v in d.items():
    export = [d[k]['lastname'], d[k]['firstname'], d[k]['surname'], d[k]['organization'], d[k]['position'],
              d[k]['phone'], d[k]['dob_phone'], d[k]['email']]
    l.append(export)
    pprint(l)

with open("phonebook.csv", "w", encoding="utf-8", newline='') as f:
    datawriter = csv.writer(f, delimiter=';')
    datawriter.writerows(l)
