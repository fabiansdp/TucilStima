# Nama : Fabian Savero Diaz Pranoto
# NIM : 13519140
# Kelas : K03

# Fungsi untuk inisialisasi graf berbentuk dictionary
def initializeGraph(filename):
    f = open("test/" + filename)

    # Inisialisasi dictionary dengan
    # key kode_kuliah dan value kuliah_prasyarat
    grafKuliah = dict()

    # Baca setiap line, matkul pertama jadi key
    # dan sisanya menjadi value berbentuk array
    for line in f.read().splitlines():
        arrayKuliah = line.replace(".", "").replace(" ", "").split(",")
        grafKuliah[arrayKuliah[0]] = arrayKuliah[1:]

    f.close()

    return grafKuliah

# Fungsi rekursif untuk pengecekan node di toposort
def recursiveSortHelper(visited, solution, graf, node):
    # Loop adjacency list di setiap node/key
    # Jika node tidak memiliki node adjacent, tambah ke visited
    # Jika memiliki adjacency list, loop dan apabila tidak ada di visited maka
    # panggil fungsi rekursif untuk pengecekan node adjacent tersebut
    # Jika node tidak ada di solusi, append ke list solution
    if len(graf[node]) == 0:
        visited.add(node)
    else:
        for adjacent in graf[node]:
            if adjacent not in visited:
                visited.add(adjacent)
                recursiveSortHelper(visited, solution, graf, adjacent)

    if node not in solution:
        solution.append(node)

# Fungsi toposort utama
def topoSort(graf):
    # Solution merupakan list hasil akhir toposort
    # Visited merupakan sebuah set yang berisi node yang sudah
    # dikunjungi
    solution = list()
    visited = set()

    # Loop setiap key di graf dan panggil fungsi rekursif
    for key in graf.keys():
        recursiveSortHelper(visited, solution, graf, key)

    return solution

# Fungsi untuk print solusi
def printSolution(solution):
    print("\nRencana Kuliah:")
    for i in range(len(solution)):
        print(str(i+1)+".", solution[i])


# Main Program
filename = input("Masukkan nama berkas: ")
grafKuliah = initializeGraph(filename) # Inisialisasi graf
solution = topoSort(grafKuliah) # list solusi
printSolution(solution) # print solusi