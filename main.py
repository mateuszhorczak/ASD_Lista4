import pickle


class Node:  # 0 - czarny, 1 - czerwony
    def __init__(self, person_surname, person_name, person_address, person_number):
        self.surname = person_surname
        self.name = person_name
        self.address = person_address
        self.number = person_number
        self.parent = None  # Rodzic wezla
        self.left = None  # Lewe dziecko wezla
        self.right = None  # Prawe dziecko wezla
        self.color = 1  # Czerwony wezel ktory jest nowo wstaiony zawsze jest jako czerwony


class RBTree:  # zlozonosc pamieciowa O(n), gdzie n to liczba wezlow, dokladna O(9n)
    def __init__(self):
        self.NULL = Node(0, 0, 0, 0)
        self.NULL.color = 0
        self.NULL.surname = 0
        self.NULL.name = 0
        self.NULL.address = 0
        self.NULL.number = 0
        self.NULL.left = None
        self.NULL.right = None
        self.root = self.NULL

    def insertNode(self, person_surname, person_name, person_address, person_number):  # O(log n)
        node = Node(person_surname, person_name, person_address, person_number)
        node.parent = None
        node.surname = person_surname
        node.name = person_name
        node.address = person_address
        node.number = person_number
        node.left = self.NULL
        node.right = self.NULL
        node.color = 1  # ustawia kolor roota na czerwony

        y = None
        x = self.root

        while x != self.NULL:  # szuka miejsca na nowy wezel
            y = x
            if node.surname < x.surname or \
                    (node.surname == x.surname and node.name < x.name) or \
                    (node.surname == x.surname and node.name == x.name and node.address < x.address):
                x = x.left
            else:
                x = x.right
        node.parent = y
        if y is None:  # jesli wezel po przypisaniu nie ma rodzica, to jest to root
            self.root = node
        elif node.surname < y.surname or \
                (node.surname == y.surname and node.name < y.name) or \
                (node.surname == y.surname and node.name == y.name and node.address < y.address):
            y.left = node
        else:
            y.right = node
        if node.parent is None:  # root jest zawsze czarny
            node.color = 0
            return
        if node.parent.parent is None:  # czy rodzic wezla jest rootem
            return
        self.fixInsert(node)  # Jesli nie zakonczy wyzej, to naprawi wstawianie

    def minimum(self, node):
        while node.left != self.NULL:
            node = node.left
        return node

    def LeftRotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.NULL:
            y.left.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def RightRotate(self, x):
        y = x.left  # y = Lewe dziecko x
        x.left = y.right  # lewe dziecko x przypisuje na prawe dziecko y
        if y.right != self.NULL:
            y.right.parent = x
        y.parent = x.parent  # zmiana rodzica y na rodzica x
        if x.parent is None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def fixInsert(self, k):
        while k.parent.color == 1:  # dopoki rodzic jest czerwony
            if k.parent == k.parent.parent.right:
                u = k.parent.parent.left
                if u.color == 1:
                    u.color = 0
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    k = k.parent.parent
                else:
                    if k == k.parent.left:
                        k = k.parent
                        self.RightRotate(k)
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    self.LeftRotate(k.parent.parent)
            else:
                u = k.parent.parent.right
                if u.color == 1:
                    u.color = 0
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    k = k.parent.parent
                else:
                    if k == k.parent.right:
                        k = k.parent
                        self.LeftRotate(k)
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    self.RightRotate(k.parent.parent)
            if k == self.root:
                break
        self.root.color = 0

    def fixDelete(self, x):
        while x != self.root and x.color == 0:  # dopoki x nie jest rootem i nie jest czarne
            if x == x.parent.left:
                s = x.parent.right
                if s.color == 1:
                    s = x.parent.right
                    s.color = 0
                    x.parent.color = 1
                    self.LeftRotate(x.parent)
                    s = x.parent.right
                if s.left.color == 0 and s.right.color == 0:
                    s.color = 1
                    x = x.parent
                else:
                    if s.right.color == 0:
                        s.left.color = 0
                        s.color = 1
                        self.RightRotate(s)
                        s = x.parent.right
                    s.color = x.parent.color
                    x.parent.color = 0
                    s.right.color = 0
                    self.LeftRotate(x.parent)
                    x = self.root
            else:
                s = x.parent.left
                if s.color == 1:
                    s.color = 0
                    x.parent.color = 1
                    self.RightRotate(x.parent)
                    s = x.parent.left
                if s.right.color == 0 and s.right.color == 0:
                    s.color = 1
                    x = x.parent
                else:
                    if s.left.color == 0:
                        s.right.color = 0
                        s.color = 1
                        self.LeftRotate(s)
                        s = x.parent.left
                    s.color = x.parent.color
                    x.parent.color = 0
                    s.left.color = 0
                    self.RightRotate(x.parent)
                    x = self.root
        x.color = 0

    def __rb_transplant(self, u, v):
        if u.parent is None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def delete_node_helper(self, node, surname, name, address):
        z = self.NULL
        while node != self.NULL:
            if node.surname == surname and node.name == name and node.address == address:
                z = node
            if node.surname < surname or \
                    (node.surname == surname and node.name < name) or \
                    (node.surname == surname and node.name == name and node.address < address):
                node = node.right
            else:
                node = node.left
        if z == self.NULL:
            print("Nie znaleziono podanej osoby")
            return
        y = z
        y_original_color = y.color
        if z.left == self.NULL:
            x = z.right
            self.__rb_transplant(z, z.right)
        elif z.right == self.NULL:
            x = z.left
            self.__rb_transplant(z, z.left)
        else:
            y = self.minimum(z.right)
            y_original_color = y.color
            x = y.right
            if y.parent == z:
                x.parent = y
            else:
                self.__rb_transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            self.__rb_transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color
        if y_original_color == 0:
            self.fixDelete(x)
        print("Poprawnie usunieto osobe")

    def delete_node(self, surname, name, address):  # O(log n)
        self.delete_node_helper(self.root, surname, name, address)

    def searchElement(self, root, surname, name, address):  # O(log n)
        if root is None or (root.surname == surname and root.name == name and root.address == address):
            return root

        if str(root.surname) < surname or \
                (str(root.surname) == surname and str(root.name) < name) or \
                (str(root.surname) == surname and str(root.name) == name and str(root.address) < address):
            return self.searchElement(root.right, surname, name, address)

        return self.searchElement(root.left, surname, name, address)

    def get_root(self):
        return self.root

    def get_persons(self, node, list_of_persons):
        if node is None:
            return
        self.get_persons(node.left, list_of_persons)
        person = [node.surname, node.name, node.address, node.number]
        if person[0] != 0 and person[1] != 0 and person[2] != 0:
            list_of_persons.append(person)
        self.get_persons(node.right, list_of_persons)


def from_binary_convert_to_string(word):
    int_word = int(word, base=2)
    str_word = int_word.to_bytes((int_word.bit_length() + 7) // 8, 'big').decode()
    return str_word


def switch_choice(num):
    def add():
        print(
            "1 - Dodawanie: Podaj w nowych liniach: Imie, Nazwisko, adres, numer(y) telefonu (jak wiecej niz jeden to po spacji)")
        name = str(input())
        surname = str(input())
        address = str(input())
        number = str(input())
        phone_book.insertNode(surname, name, address, number)
        print("Dodano abonenta")

    def delete():
        print("2 - Usuwanie: Podaj w nowych liniach: Imie, Nazwisko, adres")
        name = str(input())
        surname = str(input())
        address = str(input())
        phone_book.delete_node(surname, name, address)

    def search():
        print("3 - Wyszukiwanie: Podaj w nowych liniach: Imie, Nazwisko, adres")
        name = str(input())
        surname = str(input())
        address = str(input())
        searched_node = phone_book.searchElement(phone_book.get_root(), surname, name, address)
        print(searched_node.number) if searched_node is not None else print("Abonent nie istnieje")

    def save_data():
        print("4 - Zapis: Podaj nazwe pliku:")
        file_name = str(input())
        list_of_persons = []
        phone_book.get_persons(phone_book.get_root(), list_of_persons)
        with open(f'{file_name}', 'wb') as file:
            pickle.dump(list_of_persons, file)
        print(f'Zapisano do pliku: {file_name}')

    def load_data():
        print('5 - Wczytywanie danych: Podaj nazwe pliku:')
        file_name = str(input())
        with open(f'{file_name}', 'rb') as file:
            persons = pickle.load(file)
        for person in persons:
            phone_book.insertNode(str(person[0]), str(person[1]), str(person[2]), str(person[3]))
        print(f'Wczytano dane z pliku: {file_name}')

    match num:
        case 1:
            add()
        case 2:
            delete()
        case 3:
            search()
        case 4:
            save_data()
        case 5:
            load_data()
        case 6:
            exit()
        case _:
            print("Zly przycisk")

    print("\n")


if __name__ == '__main__':
    phone_book = RBTree()
    while True:
        print("Co chcesz zrobic?")
        print(" 1 - Wstawic nowego abonenta \n 2 - Usunac abonenta \n 3 - Wyszukac numer(y) abonenta \n "
              "4 - zapis danych do pliku \n 5 - wczytac dane z pliku \n 6 - wyjsc")
        switch_choice(int(input()))
