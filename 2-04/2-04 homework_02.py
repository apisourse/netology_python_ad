from pprint import pprint


class Contact():

    def __init__(self, name, surname, phone, favourites=False, **kwargs):
        self.name = name
        self.surname = surname
        self.phone = phone
        self.favourites = favourites
        self.original_kwargs = kwargs
        self.kwargs = ''
        for k, v in kwargs.items():
            self.kwargs += '\n\t\t{}: {}'.format(k, v)
        self.str = '========\nИмя: {n}\nФамилия: {s}\nТелефон: {p}\nВ избранных: {f}\nДополнительная информация:{k}'.format(
            n=self.name, s=self.surname, p=self.phone, f=self.favourites, k=self.kwargs)

    def __str__(self):
        return self.str


jhon = Contact('Jhon', 'Smith', '+71234567809', favourites=True, telegram='@jhony', email='jhony@smith.com')
sam = Contact('Sam', 'Jonson', '+79876543210', favourites=False, telegram='@sammy', email='sammy@jonson.com')
garry = Contact('Garry', 'Hagrid', '+79998887766', favourites=True, telegram='@garry', email='garry@hagrid.com')
tom = Contact('Tom', 'Sanders', '+71112223344', telegram='@tom', email='tom@sanders.com')

# =====================================================

pb = dict()


class PhoneBook():

    def __init__(self, pb_name):
        self.pb_name = pb_name

    def add_contact_pb(self, contact, pd):
        self.contact = contact

        if self.pb_name not in pb:
            pd[self.pb_name] = []
        else:
            pass

        pb[self.pb_name].append({
            self.contact.phone: {
                'Имя': self.contact.name,
                'Фамилия': self.contact.surname,
                'Избранное': self.contact.favourites,
                'Прочее': self.contact.original_kwargs
            }
        })

    def del_contact_pb(self, phone):
        for i in pb[self.pb_name]:
            if phone in i:
                pb[self.pb_name].remove(i)

    def show_all_contacts(self):
        for i in pb[self.pb_name]:
            for k, v in i.items():
                text_export = '{n} {f}\n{k}\nИзбранное: {i}\n==============='.format(n=v['Имя'], f=v['Фамилия'], k=k,
                                                                                     i=v['Избранное'])
                print(text_export)

    def search_contacts_by_name(self, insert_name):
        for i in pb[self.pb_name]:
            for k, v in i.items():
                if v['Имя'] == insert_name.split(' ')[0] and v['Фамилия'] == insert_name.split(' ')[1]:
                    print(v['Имя'], v['Фамилия'], '===', k)
                else:
                    pass

    def search_favourites_contacts(self):
        for i in pb[self.pb_name]:
            for k, v in i.items():
                if v['Избранное'] == True:
                    print(v['Имя'], v['Фамилия'], '===', k)


# Чекаем:

# >>>>> Выводим контакты класса
# print(jhon)
# print(sam)
# print(garry)
# print(tom)


# >>>>> Добавляем контакт в телефонную книга
PhoneBook('Рабочая телефонная книга').add_contact_pb(jhon, pb)
PhoneBook('Рабочая телефонная книга').add_contact_pb(sam, pb)
PhoneBook('Личная телефонная книга').add_contact_pb(garry, pb)
PhoneBook('Личная телефонная книга').add_contact_pb(tom, pb)
pprint(pb)  # Проверяем

# >>>>> Удаляем контакт из телефонной книги
# PhoneBook('Личная телефонная книга').del_contact_pb('+71112223344')
# PhoneBook('Рабочая телефонная книга').del_contact_pb('+79876543210')
# pprint(pb) # Проверяем

# >>>>> Отображаем контакты телефонной книги
# PhoneBook('Рабочая телефонная книга').show_all_contacts()
# PhoneBook('Личная телефонная книга').show_all_contacts()

# >>>>> Ищем контакты в телефонной книге по имени
# PhoneBook('Рабочая телефонная книга').search_contacts_by_name('Jhon Smith')
# PhoneBook('Рабочая телефонная книга').search_contacts_by_name('Sam Jonson')

# >>>>> Ищем контакты в телефонной книге по признаку избранности
# PhoneBook('Личная телефонная книга').search_favourites_contacts()
# PhoneBook('Рабочая телефонная книга').search_favourites_contacts()
