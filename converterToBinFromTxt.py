# Program do stworzenia binarnego pliku z txt z wygenerowanymi danymi na wypadek gdyby cos sie skrzaczylo

def load_data():
    with open('persons.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()
    persons_list = []
    for line in lines:
        data_line = line.split('  ')
        persons_list.append([data_line[0], data_line[1], data_line[2], data_line[3]])
    return persons_list


def save_data(list_of_persons):
    with open('person.binary', 'w') as file:
        for person in list_of_persons:
            file.write(f'{"".join(format(ord(i), "08b") for i in person[0])}  '
                       f'{"".join(format(ord(i), "08b") for i in person[1])}  '
                       f'{"".join(format(ord(i), "08b") for i in person[2])}  '
                       f'{"".join(format(ord(i), "08b") for i in person[3])}  ')

persons = load_data()
print(persons)
save_data(persons)
