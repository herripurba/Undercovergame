import random

# Memilih impostor


def pickImpostor(val):
    impostor = random.choice(val)
    return impostor

# Memilih kata kunci


def kataKunci():
    kata = [["Shampoo", "Sabun"], ["Bergandengan", "Berpelukan"],
            ["CR7", "Messi"], ["Kaca", "Pintu"], ["Pulpen", "Pensil"],
            ["Ayam", "Burung"], ["Semangka", "Melon"],
            ["Monitor", "TV"], ["Kadal", "Bunglon"], ["Sungai", "Danau"],
            ["Singa", "Harimau"], ["Kaos", "Kemeja"],
            ["Sepatu", "Sandal"], ["Pisau", "Cutter"], ["Ember", "Baskom"],
            ["Kerbau", "Sapi"], ["Buaya", "Komodo"],
            ["Ular", "Ulat"], ["Tempe", "Tahu"], ["Garam", "Gula"],
            ["Pasir", "Tanah"], ["Nyamuk", "Lalat"],
            ["Beras", "Ketan"], ["Laptop", "Komputer"], ["Bantal", "Guling"],
            ["Kipas", "AC"], ["Bulan", "Bintang"],
            ["Truk", "Bis"], ["Gitar", "Biola"], ["Gendang", "Drum"],
            ["Piring", "Mangkok"], ["Tali", "Benang"],
            ["Komik", "Novel"], ["Buku", "Majalah"], ["Bulu", "Rambut"],
            ["Angsa", "Bebek"], ["Sepeda", "Motor"],
            ["Anak Panah", "Tombak"], ["Lift", "Eskalator"], [
                "Lumba-Lumba", "Pesut"],
            ["Penyu", "Kura-Kura"], ["Kepiting", "Rajungan"],
            ["Mie", "Bihun"], ["Pangsit", "Siomay"], ["Cumi", "Gurita"],
            ["Kubus", "Balok"], ["Lengkuas", "Jahe"],
            ["Microwave", "Oven"], ["Bakar", "Panggang"], ["Ubi", "Singkong"],
            ["Hiu", "Paus"], ["Apartemen", "Hotel"],
            ["Panci", "Wajan"], ["Jaket", "Sweater"], ["Minyak", "Air"],
            ["Udang", "Lobster"], ["Monyet", "Gorila"],
            ["Apel", "Pear"], ["Lampu", "Senter"], ["Kerupuk", "Keripik"],
            ["Pesawat", "Helikopter"], ["Kambing", "Domba"],
            ["Goreng", "Tumis"], ["Kumis", "Jenggot"], ["Puisi", "Pantun"]]

    kataTerpilih = random.choice(kata)

    return kataTerpilih
