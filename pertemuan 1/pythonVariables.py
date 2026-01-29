#                                   A. variabel python
#variabel merupakan wadah penampung nilai data

#python takda command untuk mendeklarasi sebuah variabel
#variabel baru kebuat jika kita memasukkan nilai ke dalamnya
#contoh
life="hard"
hard="life"
a=110
b=911 
print(life)
print(hard)
print(a,b)

#variabel ga perlu ditetapkan dengan suatu tipe, dan akan mengubah tipe datanya sendiri
#saat kamu set
p=7            #p adalah bertipe data integer sekarang
p="ganti aja"  #nah p sekarang bertipe data string

#jika ingin menspesifikasi tipedata sebuah variabel, bisa dengan casting
p=str(67)  #p akan jadi '67'
q=int(76)  #q akan jadi  76
r=float(7) #r akan jadi  7.0

#                                   B. nama variabel 

#variabel bisa aja make 1 huruf seperti x, y, z. 
#tapi ada juga yang make kata kata
#berikut cobtoh penamaan variabel yang legal
namaku = "ejaaa"
nama_ku = "ejaaa"
_nama_ku = "ejaaa"
namaKu = "ejaaa"
NAMAKU = "ejaaa"
namaku7 = "ejaaa"

#nama variabel dengan multikata 
"""
variabel dengan 1 huruf susah banget dibaca, jadi di python ada beberapa 
cara untuk menuliskan nama variabel dengan kata yang banyak
seperti camelCase, PascalCase, dan snake_case
"""
namaVariabelKu=3 #ini camel case
NamaVariabelKu=3 #ini pascal case
nama_variabel_ku=3 #ini snake case

#                                   C. memasukkan banyak nilai

#di python kamu juga bisa memasukkan banyak nilai dalam 1 baris kode
k, l, m = "lemon", "warnanya", "kuning"
print(k)
print(l)
print(m)

#atau masukkan nilai yang sama ke banyak variabel
f=g=h="yo ndak tau"
print(f)
print(g)
print(h)

#jika kamu punya list, tuple atau semacamnya, python juga bisa
#mengekstrak nilai ke dalam variabel
negara = ["Indonesia", "Malaysia", "singapura"]
i,m,s=negara
print(i)
print(m)
print(s)

#oke sekarang output variable, yang digunakan di python adalah kode print()
x="saya pintar"
print(x)

d="pintar"
e="otaknya"
print(d,e) #outputnya mencetak nilai d dan e bersamaan
print(d+e) #kalo yang ini malah ngegabungin nilai variabelnya

j=3
k=6
print(j+k) #tadi tanda plus untuk menggabungkan string, nah kini dia jadi operator matematika
#namun ingat, kamu ga bisa menambah variabel yang mana salah satunya nilainya adalah bilangan
#yang lain adalah string

v=2030
w="Indonesia Emas"
print(w,v) #nah berka bisa digabungkan jika hanya menggunakan koma
