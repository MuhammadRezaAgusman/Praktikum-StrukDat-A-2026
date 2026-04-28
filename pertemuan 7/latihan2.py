plat_nomor = ["B 1234 ABC", "D 8888 XYZ", "A 111 TUV", "B 2022 EFG"]
class Plat:
    def __init__(self, data):
        self.data = data
        self.next = None

def traverseAndPrint(head):
  currentNode = head
  while currentNode:
    print(currentNode.data, end=" -> ")
    currentNode = currentNode.next
  print("null")

def tambahKendaraan(head, platBaru, position=len(plat_nomor)):
    if position == 1:
        platBaru.next = head
        return platBaru

    currentNode = head
    for _ in range(position - 2):
        if currentNode is None:
            break
        currentNode = currentNode.next

    platBaru.next = currentNode.next
    currentNode.next = platBaru
    return head
def hapusKendaraan(head, platDihapus):
    if head == platDihapus:
        return head.next

    currentNode = head
    while currentNode.next and currentNode.next != platDihapus:
        currentNode = currentNode.next

    if currentNode.next is None:
        return head

    currentNode.next = currentNode.next.next

    return head

plat1 = Plat(plat_nomor[0])
plat2 = Plat(plat_nomor[1])
plat3 = Plat(plat_nomor[2])
plat4 = Plat(plat_nomor[3])

plat1.next = plat2
plat2.next = plat3
plat3.next = plat4

print("sebelum dihapus: ")
traverseAndPrint(plat1)

plat5 = Plat(plat_nomor.append("B 4433 TUV"))
tambahKendaraan(plat1, plat5)

print("sesudah ditambah: ")
traverseAndPrint(plat1)

hapusKendaraan(plat1, plat2)

print("sesudah dihapus: ")
traverseAndPrint(plat1)
