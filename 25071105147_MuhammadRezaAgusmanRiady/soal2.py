katalog = [ {'nama': 'belajar python',  'harga': 75000, 'stok': 5},
            {'nama': 'struktur data',   'harga': 95000, 'stok': 3}, 
            {'nama': 'algoritma dasar', 'harga': 60000, 'stok': 8}, ] 
if katalog[0]['nama'] == 'belajar python':
    print(True)

def cari_buku(katalog, keyword):
    for i in range(len(katalog)):
        if katalog[i]["nama"] == keyword:
            buku = list(i)
            print(buku)
            break                
        else:
            print("Buku tak ditemukan")

kunci = input("Masukkan nama buku: ").lower()
cari_buku(katalog, kunci)


