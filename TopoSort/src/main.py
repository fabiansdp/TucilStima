
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

def recursiveSortHelper(seen, solution, graf, node):
    for adjacent in graf[node]:
        if adjacent not in seen:
            seen.add(adjacent)
            recursiveSortHelper(seen, solution, graf, adjacent)
    if node not in solution:
        solution.append(node)

def topoSort(graf):
    solution = list()
    seen = set()

    for key in graf.keys():
        recursiveSortHelper(seen, solution, graf, key)

    return solution

def printSolution(solution):
    print("\nRencana Kuliah:")
    for i in range(len(solution)):
        print(str(i+1)+".", solution[i])



filename = input("Masukkan nama berkas: ")

grafKuliah = initializeGraph(filename)
    
solution = topoSort(grafKuliah)

printSolution(solution)