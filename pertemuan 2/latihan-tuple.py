dosen = ("D001", "Dr. Andi", "Struktur data", 12)

print("Nama Dosen  : ", dosen[1])
print("Mata Kuliah : ", dosen[2])

print("isi data dosen :")
for x in dosen:
    print(x)

#mengubah isi tuple
ubah = list(dosen)
ubah[3] = 14
dosen = tuple(ubah)
print(dosen)
""" sks pada tuple dosen berubah setelah diubah saat tuple
dikonversi menjadi list kemudian diganti elemennya, kemudian list tadi 
dikonversi kembali menjadi tuple. tuple mestilah diubah menjadi list dahulu 
karena elemen tuple tak dapat diubah alias unmuteamble.
"""
"""kelebihan tuple adalah element tuple itu tak dapat diubah jadi 
dapat digunakan sebagai nilai pasti di dalam kode, namun list dapat diubah ubah."""