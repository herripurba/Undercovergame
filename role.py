import random


def pickImpostor(val):
    impostor = random.choice(val)
    return impostor


def kataKunci():
    kata = [["shampo", "sabun"], ["Bergandengan", "Berpelukan"],
            ["CR7", "messi"], ["windows", "window"], ["pulpen", "pensil"] ]

    kataTerpilih = random.choice(kata)

    return kataTerpilih


def shuffle(arr):
    for n in range(len(arr) - 1):
        rnd = random.randint(0, (len(arr) - 1))
        val1 = arr[rnd]
        val2 = arr[rnd - 1]

        arr[rnd - 1] = val1
        arr[rnd] = val2

    return arr
