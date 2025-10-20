1. Fungsi Utama Aplikasi dan Fitur
Aplikasi ini berfungsi sebagai alat manajemen tugas digital yang interaktif dan persisten bagi mahasiswa untuk mengelola aktivitas akademik mereka.
CRUD Interaktif: Memungkinkan pengguna untuk Menambah (Create), Melihat (Read), Mengedit (melalui toggle status Selesai), dan Menghapus (Delete) tugas.
Penyimpanan Lokal: Data tugas disimpan secara lokal dan persisten di peramban pengguna menggunakan localStorage.
Filter & Pencarian: Menyediakan kemampuan untuk mencari dan menyaring daftar tugas berdasarkan Status (Selesai/Belum Selesai) dan Mata Kuliah.
Visualisasi Status: Menghitung dan menampilkan secara real-time jumlah tugas yang belum selesai.
Validasi Data: Menerapkan validasi form untuk memastikan Nama Tugas tidak kosong dan Deadline tidak memilih tanggal di masa lalu.

2. Cara menggunakan Aplikasi
Setelah aplikasi terbuka, kita dapat mengelola tugas akademik Anda sebagai berikut:
- Menambahkan Tugas Baru:
  Isi kolom Nama Tugas (Wajib).
  Isi kolom Mata Kuliah (Opsional).
  Pilih Deadline (Wajib, tidak boleh tanggal yang sudah lewat).
  Klik tombol "Tambah Tugas". Tugas baru akan muncul di daftar.

- Mengelola Status Tugas:
  Untuk menandai tugas selesai, klik tombol "Selesaikan" di samping tugas. Tugas akan dicoret dan latar belakangnya berubah.
  Untuk mengubah kembali statusnya (Belum Selesai), klik tombol yang sama yang kini berlabel "Batal Selesai".

- Menghapus Tugas:
  Klik tombol "Hapus" di samping tugas yang sudah tidak diperlukan.
  Konfirmasi pop-up akan muncul. Pilih 'OK' untuk menghapus permanen.

- Menemukan Tugas (Filter/Pencarian):
  Filter Status: Gunakan dropdown "Filter Status" untuk menampilkan hanya tugas yang "Belum Selesai" atau hanya yang "Selesai".
  Pencarian Matkul: Ketikkan nama mata kuliah (misalnya, "Pemrograman Web") di kolom "Filter Mata Kuliah". Daftar tugas akan disaring secara otomatis.

- Memantau Kemajuan:
  Perhatikan angka di samping teks "Tugas Belum Selesai". Angka ini akan diperbarui secara otomatis setiap kali kita menambah, menghapus, atau menyelesaikan tugas.

3. Daftar fitur yang telah diimplementasikan
   - Tambah tugas baru (nama, matkul, deadline)
   - Menandai selesai/batal selesai
   - Hapus tugas
   - Penyimpanan data persisten menggunakan localstirage
   - Validasi nama tugas (tidak boleh kosong)
   - Validasi tanggal deadline (tidak boleh tanggal yang sudah lewat)
   - Filter berdasarkan status (semua/selesai/belum selesai)
   - Filter/cari berdasarkan mata kuliah
   - Menampilkan hitungan tugas belum selesai

4. Penjelasan teknis tentang penggunaan LocalStorage dan validasi form
   - Penggunaan LocalStorage
     Aplikasi ini mencapai persistensi data dengan memanfaatkan localStorage.     Setiap array tugas (tasks) diubah menjadi string JSON menggunakan JSON.stringify() sebelum disimpan dengan localStorage.setItem('tasks', ...). Saat aplikasi dimuat, data diambil sebagai string, kemudian diuraikan kembali menjadi array JavaScript yang fungsional menggunakan JSON.parse(localStorage.getItem('tasks')). Proses penyimpanan ini (memanggil saveTasks()) selalu dilakukan setelah setiap operasi perubahan data (tambah, hapus, toggle) untuk menjamin data yang ditampilkan selalu up-to-date dan tersimpan aman di peramban pengguna.
   - Implementasi Validasi Form
     Validasi dilakukan secara proaktif pada event submit form untuk mencegah data yang buruk masuk ke sistem. Ada dua aturan utama yang diterapkan, yaitu:
     - Nama Tugas: Dicek apakah input tidak kosong (name.trim() === "").
     - Deadline: Dicek apakah tanggal yang dipilih tidak berada di masa lampau.   Ini dilakukan dengan membandingkan nilai input deadline dengan tanggal hari ini (new Date().toISOString().split('T')[0]).

      Jika salah satu validasi gagal, sebuah pesan peringatan (alert) ditampilkan kepada pengguna, dan proses submit (penambahan tugas) dihentikan menggunakan pernyataan return.

5. Screenshot aplikasi yang sudah jadi
<img width="1366" height="768" alt="Screenshot (612)" src="https://github.com/user-attachments/assets/cea3c43a-6480-4553-b39c-a9364771b15b" />
<img width="1366" height="768" alt="Screenshot (615)" src="https://github.com/user-attachments/assets/66dfade8-678a-4d3b-b775-b96084363341" />
<img width="1366" height="768" alt="Screenshot (613)" src="https://github.com/user-attachments/assets/67920ec7-4239-44f0-ac9d-3d59f5618e4e" />
<img width="1366" height="768" alt="Screenshot (614)" src="https://github.com/user-attachments/assets/ad13ba35-280b-4577-9645-3363f2fd4a57" />
<img width="1366" height="768" alt="Screenshot (616)" src="https://github.com/user-attachments/assets/f3dcf024-63c3-4788-a9b5-d64daa801f47" />


