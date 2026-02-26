import tabulate
import kurs as krs
import konverter as kvt 

print("=== KONVERTER MATA UANG ===")
data = [[k, v] for k, v in krs.kurs.items()]
print(tabulate.tabulate(data, headers=['Kode', 'Kurs'], tablefmt="pretty"))

kvt.convert()