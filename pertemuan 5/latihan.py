# 1) Diberikan list stok barang di gudang: stok_barang = [15, 40, 30, 10, 25]
print("nomor 1")
stok_barang = [15, 40, 30, 10, 25]
#a. Temukan indeks dari nilai 10, lalu ubah nilai pada indeks tersebut menjadi 50.
del stok_barang[3]
stok_barang.insert(3, 50)

#b. Tambahkan nilai 5 ke akhir list, kemudian urutkan list secara descending (besar ke kecil).
stok_barang.append(5)
stok_barang.sort(reverse=True)

#c. Tampilkan jumlah total seluruh nilai dalam list tersebut.
print(sum(stok_barang))

#d. Gunakan shorthand if (ternary) untuk menampilkan "Stok Aman" jika rata-rata nilai 
#   dalam list > 20, jika tidak tampilkan "Waspada".
print("Stok Aman") if sum(stok_barang)/len(stok_barang) > 20 else print("Waspada")


#2. Diberikan list berisi tuple data mahasiswa dan poin keaktifan: data_aktivitas = [("Diki",88), ("Aqul", 45), ("Abid", 92), ("Rehan", 70)]
print("nomor 2") 
data_aktivitas = [("Diki",88), ("Aqul", 45), ("Abid", 92), ("Rehan", 70)]
# a. Lakukan perulangan pada list tersebut. Jika poin > 80, tampilkan: "[Nama]
#    mendapatkan predikat Gold". Jika poin 50-80, tampilkan: "[Nama] mendapatkan
#    predikat Silver". Di bawah itu, tampilkan: "[Nama] mendapatkan predikat Bronze"

for nama, nilai in data_aktivitas:
        if nilai >= 80:
            print(f"{nama} mendapatkan predikat Gold")
        elif nilai>=50 or nilai<80 :
            print(f"{nama} mendapatkan predikat Silver")
        else:
            print(f"{nama} mendapatkan predikat Bronze")

print("nomor 3")
ukm_coding = {"Andi", "Budi", "Caca", "Deni"}
ukm_robotik = {"Caca", "Deni", "Euis", "Fafa"}
#a. a. Tampilkan mahasiswa yang hanya mendaftar di ukm_coding saja (tidak mendaftar di robotik).
koding_aja = ukm_coding - ukm_robotik
print(koding_aja)
#b. b. Tampilkan daftar seluruh mahasiswa unik yang mendaftar di salah satu atau kedua UKM tersebut.
salah_satu = ukm_coding | ukm_robotik
print(salah_satu)
#c. Cek apakah "Andi" merupakan anggota dari ukm_robotik. Tampilkan hasil dalam bentuk boolean.
print("Andi" in ukm_robotik)

print("nomor 4")
gudang_pc = [
{"item": "Monitor", "harga": 1500000, "stok": 5},
{"item": "Keyboard", "harga": 400000, "stok": 12},
{"item": "Mouse", "harga": 250000, "stok": 20}
]
#a. Tambahkan satu key baru bernama "kategori" dengan nilai "Aksesoris" untuk produk Keyboard.
for barang in gudang_pc:
    if barang.get("item") == "Keyboard":
        barang.update({"kategori": "Aksesoris"})

print(gudang_pc)

#b. Tambahkan satu item baru: "Headset" dengan harga 350000 dan stok 8.
gudang_pc.append(dict(item = "Headset", harga = 350000, stok = 8))

#c. Hitung Total Nilai Aset (Harga x Stok) untuk setiap item.
for barang in gudang_pc:
    total = barang["harga"]*barang["stok"] 
    print(f"Item: {barang["item"]} | Total Aset: Rp {total}")
