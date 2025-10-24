# Personal Dashboard
Aplikasi Personal Dashboard Catatan Pribadi adalah aplikasi web sederhana yang dirancang untuk membantu pengguna mengelola catatan harian mereka secara digital. Aplikasi ini berfungsi sebagai buku catatan pribadi yang dapat diakses langsung melalui browser, tanpa perlu instalasi atau registrasi.

## Fungsi Aplikasi dan Fitur
1. Manajemen Catatan (CRUD):
- Tambah Catatan: Pengguna dapat menulis catatan baru melalui area teks (textarea) yang cukup besar untuk menampung paragraf.
- Lihat Catatan: Semua catatan ditampilkan dalam daftar yang rapi, dengan konten, waktu pembuatan/pembaruan, dan status sematan.
- Edit Catatan: Pengguna dapat mengubah konten catatan yang sudah ada melalui jendela modal (pop-up) yang user-friendly.
- Hapus Catatan: Pengguna dapat menghapus catatan yang tidak lagi diperlukan secara permanen.
2. Organisasi & Filter:
- Sematkan Catatan (Pin): Fitur untuk menandai catatan penting. Catatan yang disematkan akan memiliki tampilan visual yang berbeda (warna latar dan ikon) agar mudah dikenali.
- Filter Tampilan: Pengguna dapat memfilter daftar catatan berdasarkan kategori:
    - Semua: Menampilkan seluruh catatan.
    - Disematkan: Hanya menampilkan catatan yang di-pin.
    - Terbaru: Menampilkan catatan yang dibuat dalam 24 jam terakhir.
3. Statistik Real-time:
- Dashboard menampilkan tiga statistik utama yang diperbarui secara otomatis:
    - Total Catatan: Jumlah keseluruhan catatan.
    - Catatan Disematkan: Jumlah catatan yang di-pin.
    - Catatan Baru: Jumlah catatan yang dibuat dalam 24 jam terakhir.
4. Penyimpanan Lokal (LocalStorage):
- Semua data catatan disimpan secara lokal di browser pengguna menggunakan localStorage. Ini berarti data tidak akan hilang meskipun browser ditutup atau halaman di-refresh.
5. Antarmuka & Pengalaman Pengguna (UI/UX):
- Notifikasi Toast: Memberikan feedback singkat kepada pengguna untuk setiap aksi (misalnya, "Catatan berhasil ditambahkan").
- Desain Responsif: Tampilan aplikasi akan menyesuaikan dengan baik di berbagai ukuran layar, dari desktop hingga ponsel.
- Animasi & Transisi: Terdapat animasi halus pada interaksi elemen untuk meningkatkan pengalaman pengguna.

## Daftar fitur ES6+ yang diimplementasikan
1. let dan const. Menggunakan let untuk variabel yang nilainya bisa berubah (seperti editingNoteId) dan const untuk variabel yang nilainya tetap (seperti noteManager dan referensi DOM).
2. Arrow Functions. Aplikasi ini mengimplementasikan lebih dari 3 arrow function.
3. Template Literals. Memungkinkan penyisipan ekspresi dan string multi-baris dengan mudah menggunakan backticks (`). Digunakan untuk rendering HTML secara dinamis.
4. Classes. Digunakan untuk membuat blueprint objek. Aplikasi ini memiliki dua kelas utama: Note (untuk membuat objek catatan) dan NoteManager (untuk mengelola seluruh catatan).
5. Async/Await untuk menangani operasi asinkron (seperti penyimpanan ke localStorage) dengan cara yang terlihat seperti kode sinkron, membuatnya lebih mudah dibaca.
6. Destructuring. Mengekstrak properti dari objek menjadi variabel terpisah secara singkat.
7. Metode Array Modern (Higher-Order Functions). Menggunakan fungsi bawaan array seperti filter, map, dan find untuk memproses data array secara fungsional.
8. Default Parameter. Memberikan nilai default kepada parameter fungsi jika tidak ada argumen yang diberikan.
## Screenshot