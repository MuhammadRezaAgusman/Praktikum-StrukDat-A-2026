class Node:
    def __init__(self, judul, pengarang):
        self.judul = judul
        self.pengarang = pengarang
        self.next = None
        self.prev = None

class TokoBukuLiterasi:
    def __init__(self):
        self.head = None
    def insert_tail(self, judul, pengarang):
        new_node = Node(judul, pengarang)

        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next

        current.next = new_node
        new_node.prev = current
    def print_forward(self):
        current = self.head
        while current:
            print(current.judul,current.pengarang, end=" <-> ")
            current = current.next
        print("None")
    def print_backward(self):
        current = self.head

        while current and current.next:
            current = current.next

        while current:
            print(f"Judul: {current.judul}, Pengarang: {current.pengarang}", end=" <-> ")
            current = current.prev
        print("None")
    def delete_by_judul(self, judul):
        current = self.head

        while current:
            if current.judul == judul:
                if current.prev is None:
                    self.head = current.next
                    if self.head:
                        self.head.prev = None
                else:
                    current.prev.next = current.next

                    if current.next:
                        current.next.prev = current.prev
                return

            current = current.next

#command
o1 = TokoBukuLiterasi()
o1.insert_tail("Laskar Pelangi", "eja")
o1.insert_tail("Bumi Manusia", "Sapri")
o1.insert_tail("Sang Pemimpi", "Sujatmoko")
print("Forward: ")
o1.print_forward()
o1.delete_by_judul("Buku Manusia")
print("Backward: ")
o1.print_backward()
