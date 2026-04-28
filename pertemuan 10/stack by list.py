class StackList:
    def __init__(self):
        self.items = [] # Menggunakan list bawaan Python
    def is_empty(self):
        if len(self.items) == 0:
            return True
        return False
    def push(self, url):
        return self.items.append(url)
    def pop(self):
        if len(self.items) > 0:
            self.items.pop()
            return
        return print("Riwayat Kosong")
    def peek(self):
        print(self.items[-1])
    def size(self):
        if len(self.items) > 0:
            return print(len(self.items), "URL")
        return print(None)

o1 = StackList()
o1.push("google.com")
o1.push("detik.com")
o1.peek()
o1.pop()
print(o1.is_empty())
o1.size()
