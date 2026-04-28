class Node:
    def __init__(self, url):
        self.url = url
        self.next = None

class StackLinkedList:
    def __init__(self):
        self.top = None
        self.count = 0 # Variabel bantuan untuk melacak ukuran
    def is_empty(self):
        if self.top is None:
            return True
        return False
    def push(self, url):
        node_baru = Node(url)
        if self.top is None:
            self.top = node_baru
            self.next = None
            self.count+=1
            return
        
        current = node_baru
        current.next = self.top
        self.top = current
        self.count+=1
    def pop(self):

        if self.is_empty() is True:
            print("Riwayat Kosong")
            return
        sampah = self.top.url
        self.top = self.top.next
        self.count-=1
        return sampah
    def peek(self):
        print(self.top.url)
    def size(self):
        print(self.count)

o = StackLinkedList()
o.push("google.com")
o.push("detik.com")
o.peek()
print(o.pop())
print(o.is_empty())
o.size()
