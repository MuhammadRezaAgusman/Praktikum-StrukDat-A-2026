"""
Ada 3 jenis tipe data numerik di python yaitu
1. integer(bilangan bulat, mulai dari bilangan negatif berapapun hingga positif berapapun tanpa koma)
2. float(bilangan berkoma, baik angka positif maupun negatif yang minimal punya 1 koma)
3. complex(bilangan dengan bagian imajiner)
"""

#contoh 
x = 17   # int
y = 99.9  # float
z = 1j   # complex

#kamu bisa convert masing bilang ini ke bilangan lain

#convert dari int ke float:
a = float(x)

#convert dari float ke int:
b = int(y)

#convert dari int ke complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))