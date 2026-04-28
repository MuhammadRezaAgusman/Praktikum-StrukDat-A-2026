def tambah_buku(nama, harga, stok):
    if harga < 0:
        print("[ERROR]  Harga harus diatas 0!")
        return None
    data_buku = {"Nama": nama, "Harga": harga, "Stok": stok}
    return data_buku

i = 0
list_buku = []
while i < 3:
    nameBook = input('Masukkan nama buku: ')
    priceBook = float(input('Masukkan harga buku: '))
    bookStock = int(input('Masukkan jumlah stok buku: '))
    bookData = tambah_buku(nameBook, priceBook, bookStock)
    t=1
    while t<2:
        list1 = []
        for k,l in bookData.items():
         list1.append([k,l])
        list_buku.append(list1)
        t+=1

    i+=1
print(list_buku)

for a in range(len(list_buku)):
    print("daftar ke-", a+1)
    for b in range(len(list_buku[0])):
        print(f"{list_buku[a][b][0]} : {list_buku[a][b][1]}")

