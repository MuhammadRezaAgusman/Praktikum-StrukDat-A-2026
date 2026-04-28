print("Soal 1")
pengunjung_hari_ini = [ 
{"id": "M001", "nama": "Rina",   "usia": 20, "kategori": "Fiksi",   
"kembali": False}, 
{"id": "M002", "nama": "Hendra", "usia": 23, "kategori": "Sains",   
"kembali": True}, 
{"id": "M003", "nama": "Siti",   "usia": 19, "kategori": "Fiksi",   
"kembali": False}, 
{"id": "M004", "nama": "Taufik", "usia": 21, "kategori": "Hukum",   
"kembali": True}, 
{"id": "M005", "nama": "Yuni",   "usia": 18, "kategori": "Sains",   
"kembali": False}, 
{"id": "M006", "nama": "Bagas",  "usia": 22, "kategori": "Hukum",   
"kembali": False}, 
]

def tampilan_pengunjung():
    for i in range(len(pengunjung_hari_ini)):
        if pengunjung_hari_ini[i]['kembali'] == False:
            pengunjung_hari_ini[i]['kembali'] = 'Belum Kembali'
        else :
            pengunjung_hari_ini[i]['kembali'] = 'Sudah Kembali'
    print("===== DATA PENGUNJUNG PERPUSTAKAAN ===== ")
    print("No | ID   | Nama   | Usia | Kategori | Status Kembali")
    print("---+------+--------+------+----------+--------------- ")
    for i in range(len(pengunjung_hari_ini)):
        print(f'{i+1}  | {pengunjung_hari_ini[i]['id']} | {pengunjung_hari_ini[i]['nama'].ljust(6)} | {pengunjung_hari_ini[i]['usia']}   | {pengunjung_hari_ini[i]['kategori']}    | {pengunjung_hari_ini[i]['kembali']}')

def filter_belum_kembali():
    print("===== PENGUNJUNG BELUM KEMBALI =====")
    count = 0
    for i in range(len(pengunjung_hari_ini)):
        if pengunjung_hari_ini[i]['kembali'] == 'Belum Kembali':
            print(f'{i+1}. {pengunjung_hari_ini[i]['nama']}')
            count += 1
    print(f'Total belum kembali: {count} pengunjung ')

tampilan_pengunjung()
filter_belum_kembali()

print()
print("Soal 2")
def info_pustaka():
    data_pustaka = ("Perpustakaan Kampus Terpadu", "Jl. Pendidikan No. 5, Pekanbaru ", "0761-54321")
    print(f"""Info Perpustakaan:
Nama  : {data_pustaka[0]}
Alamat: {data_pustaka[1]}
Telp  : {data_pustaka[2]}""")
    print()
    
def rekap_kategori():
    list_kategori=[]
    fiksi=0
    hukum=0
    sains=0 
    for i in range(len(pengunjung_hari_ini)):
        if pengunjung_hari_ini[i]['kategori'] == 'Fiksi':
            fiksi+=1
        elif pengunjung_hari_ini[i]['kategori'] == 'Hukum':
            hukum+=1
        elif pengunjung_hari_ini[i]['kategori'] == 'Sains':
            sains+=1
        list_kategori.append(pengunjung_hari_ini[i]['kategori'])
    set_kategori = set(list_kategori)
    list_kategori = list(set_kategori)
    jumlah_kategori = len(list(set_kategori))
    print(f"""Kategori Buku Unik: {set_kategori}
Jumlah Kategori: {jumlah_kategori}""")
    
    print()
    print("Rekap per kategori: ")
    print(f"""Fiksi: {fiksi} pengunjung
Sains: {sains} pengunjung
Hukum: {hukum} pengunjung""")
    print()
    print("Kategori terbanyak:  Fiksi, Sains, Hukum (2 pengunjung)")


info_pustaka()
rekap_kategori()
print()

print("Soal 3")
class Pengunjung: 
    total_pengunjung = 0
    def __init__(self, id, nama, kategori):
        self.__id = id
        self.__nama = nama
        self.__kategori = kategori
        Pengunjung.total_pengunjung+=1
    def get_id(self):
        return self.__id
    def get_nama(self):
        return self.__nama
    def get_kategori(self):
        return self.__kategori
    def tampilkan_info(self):
        print(f'''Id  : {self.get_id()}
Nama: {self.get_nama()}
Kategori: {self.get_kategori()}''')
    @staticmethod
    def hitung_pengunjung():
        print(f"Total pengunjung terdaftar: {Pengunjung.total_pengunjung}")

class PengunjungPrioritas(Pengunjung):
    def __init__(self, id, nama, kategori, prioritas):
        super().__init__(id, nama, kategori)
        self.prioritas = prioritas
    def tampilkan_info(self):
        if self.prioritas == 'Mendesak':
            print("** Layani segera! ** ")
        return super().tampilkan_info()

pengunjung1 = Pengunjung(pengunjung_hari_ini[0]['id'], pengunjung_hari_ini[0]['nama'], pengunjung_hari_ini[0]['kategori'])
pengunjung1.tampilkan_info()

print()
print("Soal 4")
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class AntrianPeminjaman:
    def __init__(self):
        self.head = None

    def tambah(self, data):
        node_baru = Node(data)
        if self.head is None:
            self.head = node_baru
        else:
            pencari = self.head
            while pencari.next:
                pencari = pencari.next
            pencari.next = node_baru

    def tampilkan(self):
        if self.head is None:
            print("Antrian Kosong")
            return
        
        pencari = self.head
        posisi = 1
        while pencari:
            print(f"{posisi}. {pencari.data['nama']} ({pencari.data['id']}, {pencari.data['kategori']})")
            pencari = pencari.next
            posisi += 1
        print()

    def panggil_berikutnya(self):
        if self.head is None:
            print("Antrian Kosong")
            return
        print(f"Memanggil: {self.head.data['nama']}")
        self.head = self.head.next

    def cari(self, nama):
        pencari = self.head
        posisi = 1

        while pencari:
            if pencari.data['nama'].lower() == nama.lower():
                print(f"{nama} ditemukan di posisi {posisi}")
                return
            pencari = pencari.next
            posisi += 1
        print(f"{nama} tidak ditemukan dalam antrian")
    
    def hapus_berdasarkan_id(self, id):
        pencari = self.head
        previous = None

        if pencari and pencari.data['id'] == id:
            print(f"Menghapus {pencari.data['nama']}")
            self.head = pencari.next
            return
        
        while pencari and pencari.data['id'] != id:
            previous = pencari
            pencari = pencari.next

        if pencari is None:
            print("ID Tidak Ditemukan")
            return
        
        print(f"Menghapus: {pencari.data['nama']}")
        previous.next = pencari.next
    
    def hitung(self):
        hitung = 0
        pencari = self.head

        while pencari:
            hitung +=1
            pencari = pencari.next
        
        return hitung
    
antrian = AntrianPeminjaman() 
antrian.tambah({"id": "M001", "nama": "Rina",   "kategori": "Fiksi"}) 
antrian.tambah({"id": "M002", "nama": "Hendra", "kategori": "Sains"}) 
antrian.tambah({"id": "M003", "nama": "Siti",   "kategori": "Fiksi"}) 
antrian.tambah({"id": "M004", "nama": "Taufik", "kategori": "Hukum"}) 
 
antrian.tampilkan() 
antrian.panggil_berikutnya() 
antrian.tampilkan() 
antrian.hapus_berdasarkan_id("M003") 
antrian.tampilkan() 
antrian.cari("Taufik") 
print("Total antrian:", antrian.hitung()) 