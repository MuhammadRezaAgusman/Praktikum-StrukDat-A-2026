nilai = [75, 80, 65, 90, 85]
nilai.append(95) #menambahkan nilai baru
nilai.remove(65) #menghapus nilai terendah
print(nilai)
nilai.sort()#mengurutkan list dari terkecil hingga terbesar
print("nilai tertinggi         : ", max(nilai))#nilai tertinggi
print("nilai terendah          : ", min(nilai))#nilai terendah
print("jumlah data             : ", sum(nilai))#total nilai
print("nilai rata rata         : ", (sum(nilai)/len(nilai)))#rata rata nilai
print("nilai setelah perubahan : ", nilai)#menampilkan list nilai yang telah diolah