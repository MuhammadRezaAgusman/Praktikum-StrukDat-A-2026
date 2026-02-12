class Person:
    def __init__(self, nama, jenisKelamin, umur):
        self.nama = nama
        self.jenisKelamin = jenisKelamin
        self.umur = umur

class Karyawan(Person):
    def __init__(self, nama, jenisKelamin, umur, gaji):
        super().__init__(nama, jenisKelamin, umur)
        self._gaji = gaji
    
    def get_gaji(self):
        return self._gaji
        
class Rekening:
    def __init__(self, noRekening, PIN):
        self.noRekening = noRekening
        self.__PIN = PIN
    
    def get_PIN(self):
        return self.__PIN
    
    def set_PIN(self, PIN):
        if len(PIN)>0:
            self.__PIN = PIN
        else:
            print("PIN Minimal punya 1 karakter")

objek1 = Person("Muhammad Reza", "Laki-Laki", 18)
objek2 = Karyawan("Ejaaa", "Laki-Laki", 18, 300000)
objek3 = Rekening("1471034578", "123SATUDUATIGA")
print(objek2.get_gaji())