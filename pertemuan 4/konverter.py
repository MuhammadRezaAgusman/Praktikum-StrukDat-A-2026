import kurs as krs

def convert():
    mata_uang1 = "".join(input("Dari (IDR/USD/EUR/SGD/JPY): ").split()).upper()
    mata_uang2 = "".join(input("Ke (IDR/USD/EUR/SGD/JPY): ").split()).upper()
    jumlah = int(input("Jumlah: "))

    idr = jumlah * krs.kurs_inInt[mata_uang1]
    hasil = idr / krs.kurs_inInt[mata_uang2]
    print(f"{krs.kode_mata_uang[mata_uang1]} {jumlah} = {krs.kode_mata_uang[mata_uang2]} {hasil:.2f}")


