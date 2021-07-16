
# UndercoverGame

**Panduan Penggunaan**
1. Jalankan serverside.py pada terminal dengan mengetikkan "python serverside.py"
2. Jalankan client.py untuk memainkan game, dengan mengetikkan "python client.py" pada terminal
3. Akan muncul window kecil untuk memasukkan nama pemain, silahkan masukkan nama anda, lalu "OK"
4. Dibutuhkan 3 pemain untuk memulai permainan
5. Jika sudah ada 3 pemain yang masuk, maka permainan dapat dimulai dengan cara pemain yang pertama masuk menekan tombol start.
(Permainan hanya dapat di-start oleh pemain pertama, jika pemain lainnya mencoba menekan tombol start, maka akan muncul pesan "Hanya player 1 yang dapat memulai game")
6. Saat permainan dimulai, akan mendapatkan kata kunci sesuai role yang mereka dapat, terdapat 2 role yaitu civillian dan impostor
(2 civillian dan 1 impostor)
7. Setiap pemain diharap untuk menyebutkan kata yang berkaitan dengan kata kuncinya tanpa menyebut kata kunci itu sendiri.
8. Jika dikira sudah tau siapakah impostornya, maka player 1 dapat menekan tombol "Mulai Vote"
(Tombol "Mulai Vote" hanya dapat ditekan oleh player 1, jika player lain mencoba menekan tombol "Mulai Vote" maka akan muncul pesan "Hanya player 1 yang dapat memulai vote")
9. Jika lebih banyak orang yang mengevote player yang merupakan impostor, maka civillian menang.
Begitu juga sebaliknya, jika lebih banyak orang yang mengevote player yang merupakan civillian, maka impostor menang, 
Jika semua vote berjumlah sama, maka game akan berakhir imbang.
10. Setelah vote selesai maka akan muncul pesan "Permainan Telah Berakhir"

**Library**

 - Tkinter 
 - Thread 
 - Socket 
 - Random