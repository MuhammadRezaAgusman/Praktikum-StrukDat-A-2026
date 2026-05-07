class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        #Langkah 1
        new = Node(data)

        #Langkah 2
        if self.root is None:
            #Jika iya
            self.root = new
            return
        
        #Langkah 3
        P = self.root
        Q = self.root

        #Langkah 4
        while Q is not None and new.data != P.data:
            #Langkah 5
            P = Q
            
            #Langkah 6
            if new.data < P.data:
                Q = P.left
            else:
                Q = P.right
            
        #Langkah 7
        if new.data == P.data:
            #Jika iya
            print("Data Duplikat")

        #Langkah 8
        if new.data < P.data:
            #Jika iya
            P.left = new
        #Jika tidak
        else:
            P.right = new

bst = BinarySearchTree()


def in_order(node):
    if node is not None:
        in_order(node.left)
        print(node.data, end=' --> ')
        in_order(node.right)

in_order(bst.root)

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert_root(self, data):
        self.root = Node(data)
    
    def insert_left(self, parent_node, data):
        if parent_node.left is None:
            parent_node.left = Node(data)
        else:
            new_node = Node(data)
            new_node.left = parent_node.left
            parent_node.left = new_node
    
    def insert_right(self, parent_node, data):
        if parent_node.right is None:
            parent_node.right = Node(data)
        else:
            new_node = Node(data)
            new_node.right = parent_node.right
            parent_node.right = new_node

bt = BinaryTree()


bt.insert_root("F")
bt.insert_left(bt.root, "B")
bt.insert_right(bt.root, "G")
bt.insert_left(bt.root.left, "A")
bt.insert_right(bt.root.left, "D")
bt.insert_left(bt.root.left.right, "C")
bt.insert_right(bt.root.left.right, "E")
bt.insert_right(bt.root.right, "I")
bt.insert_left(bt.root.right.right, "H")


def inorder(node):
    if node is not None:
        inorder(node.left)
        print(node.data, end=' --> ')
        inorder(node.right)

inorder(bt.root)
