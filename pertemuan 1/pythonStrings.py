"""
String dalam Python dikelilingi oleh tanda kutip satu atau tanda kutip dua,
jadi "halo" dan 'halo' itu sama aja. kamu dapat mencetak string
menggunakan fungsi print()
"""
print("kita")
print('kita')

#a. tanda kutip didalam tanda kutip
# kamu bisa menambahkan tanda kutip didalam tanda kutip asalkan tandakutip yang didalam
#tidak sama dengan tanda kutip yg mengelilingi string tersebut
print("namaku reza tapi bisa dipanggil 'eja'")
print('namaku reza tapi bisa dipanggil "eja"')

#b. memasukkan string kedalam variabel
tst= "milik kita"
print(tst)

#c. string multibaris
ms= """kucing lari menendang kuali
kuali jatuh bising bunyinya
hai anak janganlah berlari
agar engkau tak hilang tenaga"""# tanda petik dua bisa diganti petik satu
print(ms)

#d. string adalah array
#jadi kamu bisa mengakses unsur string menggunakan indeks
kata= "Tambang"
print(kata[0])

#e. looping melalui string
for x in "Watashitachi":
  print(x)

#f. slicing string
#untuk memotong string berdasarkan besaran indeks yang ditentukan
#jadi sistem hanya membaca indeks array strung yang diluar angka indeks yang ditentukan

a="suka"
print(a[:2])#slicing dengan indeks positif

a="suka"
print(a[:-1])#slicing indeks negatif


#selanjutnya adalah memodifikasi string
a = "Haiii ant take a sing!"
print(a.upper())#membesarkan semua huruf (uppercase)

a = "Haiii ant take a sing!"
print(a.lower())#mengecilkan semua huruf (lowercase)

#menghilangkan whitespace
a = " Heiiii ant take a sing!! "
print(a.strip()) #outputnya adalah "Heiiii ant take a sing!!"

#mengganti bagian string
a = "Nama mu siapa?"
print(a.replace("N", "M"))

#split string
#memisahkan 1 string menjadi beberapa string
a = "Terkadang, dilihat saja.. belum tentu, bisa dipercaya"
print(a.split(","))#cara menghitung banyak string yang terbentuk (jumlah pemisah+1)

#penggabungan string
c="kembali"
d="pergi"
e= c+d #gunakan ...+" "+... jika ingin memberi spasi
print(e)

#menformat string menggunakan f-string
umur = 18
txt = f"namaku ejaa, umurku {umur}"
print(txt)
