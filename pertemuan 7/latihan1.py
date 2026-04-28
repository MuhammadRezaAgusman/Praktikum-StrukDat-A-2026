data_input = ["B 1234 ABC", "D 8888 XYZ", "A 111 TUV", "B 2022 EFG"]
def ganjil_genap(array):
    ganjil = []
    genap = []
    for item in data_input:
        data_angka = item.split()[1]
        if int(data_angka) % 2 == 0:
            genap.append(item)
        else:
            ganjil.append(item)
    print("Ganjil: ", ganjil)
    print("Genap: ", genap)
ganjil_genap(data_input)
