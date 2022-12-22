# Program do stworzenia binarnego pliku z txt z wygenerowanymi danymi na wypadek gdyby cos sie skrzaczylo
# Jesli dwa gorne printy printuja to samo co dwa dolne printy to jest git

import pickle

phone_book = []
with open('persons.txt', 'r', encoding='utf-8') as file_in:
    lines = file_in.readlines()
    line = []
    for line in lines:
        data_line = line.split('  ')
        phone_book.append([data_line[0], data_line[1], data_line[2], data_line[3]])
print(len(phone_book))
print(phone_book)


#serializacja i zapis do pliku binarnego z uzyciem pickle.dump
with open('person.binary', 'wb') as file:
    pickle.dump(phone_book, file)


#deserializacja danych i odczyt z pliku binarnego z uzyciem pickle.load
with open('person.binary', 'rb') as file:
    loaded_phone_book = pickle.load(file)


print(len(loaded_phone_book))
print(loaded_phone_book)

