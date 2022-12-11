class Node:                         # 0 - czarny, 1 - czerwony
    def __init__(self, value):
        self.val = value            # Wartosc wezla
        self.parent = None          # Rodzic wezla
        self.left = None            # Lewe dziecko wezla
        self.right = None           # Prawe dziecko wezla
        self.color = 1              # Czerwony wezel ktory jest nowo wstaiony zawsze jest jako czerwony

class RBTree:
    def __init__(self):
        self.NULL = Node(0)
        self.NULL.color = 0
        self.NULL.left = None
        self.NULL.right = None
        self.root = self.NULL


    def insertNode(self, key):
        node = Node(key)
        node.parent = None
        node.value = key
        node.left = self.NULL
        node.right = self.NULL
        node.color = 1              # ustawia kolor roota na czerwony

        y = None
        x = self.root

        while x != self.NULL:       # szuka miejsca na nowy wezel
            y = x
            if node.val < x.val:
                x = x.left
            else:
                x = x.right

        node.parent = y
        if y is None:               # jesli wezel po przypisaniu nie ma rodzica, to jest to root
            self.root = node
        elif node.val < y.val:      # jezeli wartosc w wezle jest mniejsza przypisuje ja z lewej,
            y.left = node           # jak wieksza lub rowna to z prawej
        else:
            y.right = node

        if node.parent is None:         # root jest zawsze czarny
            node.color = 0              # czarny
            return
        if node.parent.parent is None:  # czy rodzic wezla jest rootem
            return

        self.fixInsert(node)            # Jesli nie zakonczy wyzej, to naprawi wstawianie


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
        if y.left is not None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y


    def RightRotate(self, x):
        y = x.left                  # y = Lewe dziecko x
        x.left = y.right            # lewe dziecko x przypisuje na prawe dziecko y
        if y.right != self.NULL:
            y.right.parent = x

        y.parent = x.parent         # zmiana rodzica y na rodzica x
        if x.parent is None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y


    def fixInsert(self, k):
        while k.parent.color == 1:                      # dopoki rodzic jest czerwony
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
        while x != self.root and x.color == 0:          # dopoki x nie jest rootem i nie jest czarne
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


    def delete_node_helper(self, node, key):
        z = self.NULL
        while node != self.NULL:
            if node.val == key:
                z = node
            if node.val <= key:
                node = node.right
            else:
                node = node.left
        if z == self.NULL:
            print("Value not present in Tree!")
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


    def delete_node(self, val):
        self.delete_node_helper(self.root, val)

    def __printCall(self, node, indent, last):
        if node != self.NULL:
            print(indent, end=' ')
            if last:
                print("R----", end=' ')
                indent += "     "
            else:
                print("L----", end=' ')
                indent += "|    "
            s_color = "RED" if node.color == 1 else "BLACK"
            print(str(node.val) + "(" + s_color + ")")
            self.__printCall(node.left, indent, False)
            self.__printCall(node.right, indent, True)


    def print_tree(self):
        self.__printCall(self.root, "", True)

if __name__ == '__main__':
    bst = RBTree()

    bst.insertNode(10)
    bst.insertNode(20)
    bst.insertNode(30)
    bst.insertNode(5)
    bst.insertNode(4)
    bst.insertNode(2)

    bst.print_tree()

    print("\nAfter deleting an element")
    bst.delete_node(2)
    bst.print_tree()