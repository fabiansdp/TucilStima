
def initializeGraph(filename):
    f = open("test/" + filename)

    # Inisialisasi dictionary dengan
    # key kode_kuliah dan value kuliah_prasyarat
    grafKuliah = dict()

    for line in f.read().splitlines():
        arrayKuliah = line.replace(".", "").split(",")
        grafKuliah[arrayKuliah[0]] = arrayKuliah[1:]

    f.close()

    return grafKuliah




filename = input("Masukkan nama berkas: ")

grafKuliah = initializeGraph(filename)

solution = list()

for key,value in grafKuliah.copy().items():
    if len(value) == 0:
        solution.append(key)
        grafKuliah.pop(key)

print(solution)