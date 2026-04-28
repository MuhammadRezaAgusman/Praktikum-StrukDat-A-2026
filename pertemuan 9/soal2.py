class Node:
    def __init__(self, nama):
        self.nama = nama
        self.next = None

class KasirLiterasi:
    def __init__(self):
        self.head = None
    def insert_tail(self, nama):
        new_node = Node(nama)

        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            return

        current = self.head

        while current.next != self.head:
            current = current.next

    
        current.next = new_node
        new_node.next = self.head

    def print_antrian(self):
        if self.head is None:
            print("Antrian kosong")
            return

        current = self.head

        while True:
            print(current.nama, end=" -> ")
            current = current.next

            if current == self.head:
                break

        print("(kembali ke antrian awal)")
    def delete_head(self):
        if self.head is None:
            return

        current = self.head
        prev = None

        if current == self.head:
                    last = self.head
                    
                    # Cari node terakhir
                    while last.next != self.head:
                        last = last.next
                        
                    # Head pindah ke node berikutnya
                    self.head = self.head.next
                    
                    # Node terakhir menunjuk ke head baru
                    last.next = self.head
                    
                # Jika menghapus node biasa / terakhir
        else:
                    
                  # 10 (prev) -> 20 (current) -> 30 (current.next)
                    prev.next = current.next

            

o1 = KasirLiterasi()
o1.insert_tail("Andi")
o1.insert_tail("Budi")
o1.insert_tail("Citra")
o1.insert_tail("Dina")
o1.insert_tail("Edo")
o1.print_antrian()
o1.delete_head()
o1.print_antrian()