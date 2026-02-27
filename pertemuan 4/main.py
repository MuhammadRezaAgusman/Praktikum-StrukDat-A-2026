import tabulate
import kurs as krs
import konverter as kvt 

print("=== KONVERTER MATA UANG ===")
print(tabulate.tabulate(krs.kurs.items(), headers=['Kode', 'Kurs'], tablefmt="pretty"))

kvt.convert()