import time

# Convert huruf ke angka
def valueOfWord(word, dictOfWord):
    value = ""
    for letter in word:
        if letter in dictOfWord:
            value += str(dictOfWord[letter])

    return int(value)

# Cari permutasi angka-angka
def permutation(numbers, r=None):
    pool = tuple(numbers)
    n = len(pool)
    r = n if r is None else r
    if r > n:
        return
    indices = list(range(n))
    cycles = list(range(n, n-r, -1))
    yield tuple(pool[i] for i in indices[:r])
    while n:
        for i in reversed(range(r)):
            cycles[i] -= 1
            if cycles[i] == 0:
                indices[i:] = indices[i+1:] + indices[i:i+1]
                cycles[i] = n - i
            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                yield tuple(pool[i] for i in indices[:r])
                break
        else:
            return

# Fungsi untuk mengeluarkan solusi
def solution(filename):
    f = open("test/" + filename, 'r')

    letters = set()
    numbers = list(range(10))

    added_numbers = []
    result = []
    isLine = False

    print("\nCryptharitm yang perlu dipecahkan:")
    for line in f.read().splitlines():
        print(line)
        if not(isLine) and (line != "------"):
            added_numbers.append(line.replace('+', ''))
        elif line == "------":
            isLine = True
        else:
            result.append(line)

        for letter in line :
            if (letter != "-") and (letter != "+"):
                letters.add(letter)

    print()
    f.close()

    count = 0
    for p in permutation(numbers, len(list(letters))):
        count += 1
        solution = dict(zip(letters, p))
        sumOfNumbers = sum(valueOfWord(word, solution) for word in added_numbers)
        sumOfResult = sum(valueOfWord(word, solution) for word in result)
        if sumOfNumbers == sumOfResult and len(str(sumOfResult)) == len(result[0]):
            return solution, count


# Main program
filename = input("Masukkan nama file: ")

start_time = time.process_time()
# Ambil Solusi dan jumlah percobaan
solution, count = solution(filename)

print("\nSolusi: ")
f = open("test/" + filename, 'r')

# Masukkan kata per line ke dalam wordlist untuk diproses
wordlist = []
for line in f.read().splitlines():
    if (line != '------'):
        wordlist.append(line)

f.close()

# Print solusi dalam angka
for i in range(len(wordlist)):
    if i==len(wordlist)-2:
        print(valueOfWord(wordlist[i],solution), end="")
        print("+")
        print("------")
    else:
        print(valueOfWord(wordlist[i],solution))

print("\nBanyak percobaan:", count)
print("\nExecution Time: ", (time.process_time()-start_time), "seconds")