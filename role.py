import random


def pickImpostor(val):
    impostor = random.choice(val)
    return impostor


def kataKunci():
    kata = [["sampho", "sabun"], ["Bergandengan", "Berpelukan"],
            ["CR7", "messi"], ["windows", "window"]]

    kataTerpilih = random.choice(kata)

    return kataTerpilih
