# Node untuk menyimpan data pasien
class Node:
    def __init__(self, nama, keluhan):
        self.nama = nama
        self.keluhan = keluhan
        self.next = None


# Queue berbasis Linked List
class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    # 1. Enqueue
    def enqueue(self, nama, keluhan):
        new_node = Node(nama, keluhan)
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self._size += 1
        print(f"[DAFTAR] {nama} terdaftar dengan keluhan: {keluhan} (No. Antrian: {self._size})")

    # 2. Dequeue
    def dequeue(self):
        if self.is_empty():
            print("[ERROR] Antrian kosong!")
            return None
        removed = self.head
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        self._size -= 1
        print(f"[PANGGIL] Dokter memanggil: {removed.nama} (keluhan: {removed.keluhan})")
        return removed

    # 3. Peek
    def peek(self):
        if self.is_empty():
            print("[PEEK] Antrian kosong!")
        else:
            print(f"[PEEK] Pasien berikutnya: {self.head.nama} — {self.head.keluhan}")

    # 4. is_empty
    def is_empty(self):
        return self.head is None

    # 5. size
    def size(self):
        return self._size

    # 6. clear
    def clear(self):
        self.head = None
        self.tail = None
        self._size = 0
        print("[CLEAR] Sesi poliklinik selesai. Antrian dikosongkan.")

    # Tambahan: tampilkan antrian
    def display(self):
        if self.is_empty():
            print("[ANTRIAN] Kosong")
            return
        
        current = self.head
        i = 1
        print("[ANTRIAN SAAT INI]")
        while current:
            print(f"  {i}. {current.nama.upper():<10} → {current.keluhan}")
            current = current.next
            i += 1
# MAIN PROGRAM
q = Queue()

print("====================================")
print("  SISTEM ANTRIAN POLI UMUM")
print("  RS Sehat Bersama")
print("====================================")

# 1
print("[CEK] Apakah antrian kosong? →", "YA" if q.is_empty() else "TIDAK")

# 2-4
q.enqueue("Budi", "demam tinggi")
q.enqueue("Ani", "batuk pilek")
q.enqueue("Citra", "sakit kepala")

# 5
print(f"[INFO] Jumlah pasien menunggu: {q.size()} orang")

# 6
q.peek()

# 7
q.dequeue()

# 8
q.enqueue("Dodi", "nyeri perut")

# 9
q.display()

# 10
q.dequeue()

# 11
print(f"[INFO] Jumlah pasien masih menunggu: {q.size()} orang")

# 12
q.clear()

# 13
print("[CEK] Apakah antrian kosong? →", "YA" if q.is_empty() else "TIDAK")