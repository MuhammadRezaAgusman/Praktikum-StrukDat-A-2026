keahlian_A = {"Python", "Java", "SQL", "Git"}
keahlian_B = {"Python", "C++", "Git", "Ducker"}

kesamaan = keahlian_A.intersection(keahlian_B)
print("keahlian sama: ", kesamaan)

beda_A = keahlian_A.difference(keahlian_B)
print("Perbedaan keahlian mahasiswa A dibanding B : ",beda_A)

beda_semua = keahlian_A.symmetric_difference(keahlian_B)
print("beda semua: ", beda_semua)

