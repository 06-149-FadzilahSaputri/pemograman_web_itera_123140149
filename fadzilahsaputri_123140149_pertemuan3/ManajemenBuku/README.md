# Deskripsi Aplikasi
Manajemen Buku Pribadi adalah aplikasi Single Page Application (SPA) yang dirancang dengan antarmuka yang bersih dan responsif. Aplikasi ini memungkinkan pengguna untuk melakukan CRUD (Create, Read, Update, Delete) pada data buku, serta menyediakan fitur pencarian dan penyaringan untuk memudahkan manajemen koleksi. Data buku disimpan secara lokal di browser menggunakan localStorage, sehingga tidak akan hilang meskipun halaman di-refresh.

# Instruksi instalasi dan menjalankan
Pertama Install semua dependensi yang diperlukan yang tercantum dalam file package.json dengan menjalankan *npm install*.

Jalankan aplikasi dalam mode development. Server akan otomatis membuka aplikasi di browser default pada alamat http://localhost:3000, dengan menjalankan perintah *npm start*.

# Penjelasan fitur React yang digunakan
1. Functional Components dengan Hooks
Seluruh aplikasi menggunakan functional components bukan class components. State dan logika lifecycle dikelola menggunakan Hooks:

- useState: Digunakan untuk mengelola state lokal dalam komponen, seperti data form di BookForm.jsx, visibilitas modal, dan state UI lainnya.
- useEffect: Digunakan untuk side effects, meskipun dalam proyek ini logika side effect utama (interaksi dengan localStorage) telah dikapsulasi ke dalam custom hook.
2. Custom Hooks
Dua custom hooks dibuat untuk mengkapsulasi dan menggunakan kembali logika state:

- useLocalStorage.js: Hook ini mengabstraksi logika untuk membaca dan menulis data ke localStorage. Hook ini mengelola state dan sinkronisasi dengan storage secara otomatis, serta menangani error yang mungkin terjadi. Ini membuat komponen yang menggunakannya menjadi lebih bersih.
- useBookStats.js: Hook ini bertanggung jawab untuk menghitung statistik (total buku, persentase per kategori) dari data buku. Hook ini menggunakan useMemo untuk mengoptimalkan performa, memastikan perhitungan hanya dijalankan ulang ketika data buku berubah, bukan pada setiap render.
3. Context API untuk State Management
Untuk menghindari "prop drilling" (mengirim props melalui banyak tingkatan komponen), aplikasi ini menggunakan React Context API:

- BookContext.js: Membuat sebuah context global yang menyimpan state utama aplikasi: daftar buku (books), filter (filter), dan istilah pencarian (search).
- BookProvider: Komponen provider yang membungkus seluruh aplikasi dan menyediakan akses ke state dan fungsi-fungsi untuk memanipulasinya (addBook, updateBook, deleteBook).
- useBooks: Custom hook yang disediakan untuk mempermudah komponen mengakses data dari BookContext.
4. React Router untuk Navigasi
React Router digunakan untuk implementasi navigasi multi-halaman dalam SPA:

- BrowserRouter: Komponen yang membungkus aplikasi untuk mengaktifkan fungsionalitas routing.
- Routes dan Route: Mendefinisikan rute URL dan komponen yang akan dirender. / untuk halaman Home dan /stats untuk halaman Stats.
- Link: Digunakan untuk navigasi antar halaman tanpa menyebabkan reload penuh halaman, memberikan pengalaman pengguna yang lebih cepat dan mulus.
5. Komponen Reusable (Reusable Components)
Aplikasi ini dirancang dengan prinsip komponen yang dapat digunakan kembali:

- BookForm: Komponen form yang digunakan untuk menambah dan mengedit buku. Perilakunya diubah berdasarkan prop bookToEdit yang diberikan.
- BookList dan BookItem: BookList menampilkan daftar buku, sementara BookItem adalah komponen untuk setiap item buku individual, lengkap dengan aksi edit dan hapus.
- BookFilter: Komponen yang menghandle input pencarian dan dropdown filter, dan dapat ditempatkan di berbagai halaman jika diperlukan.
6. Error Handling
Error handling diimplementasikan pada sisi klien untuk validasi input:

- utils/validation.js: Modul yang berisi fungsi validateBook untuk memvalidasi data form sebelum dikirim. Fungsi ini mengembalikan objek error yang dapat ditampilkan kepada pengguna.
- BookForm: Menampilkan pesan error di bawah input yang tidak valid, memberikan feedback yang jelas kepada pengguna.
7. Testing dengan React Testing Library
Aplikasi ini dilengkapi dengan unit test untuk memastikan kualitas dan keandalan kode:

- 5+ Test File: Test ditulis untuk komponen-komponen utama (BookForm, BookList, BookFilter), custom hooks (useBookStats), dan utilitas (validation).
- Fokus pada Pengguna: Test menggunakan React Testing Library, yang mendorong penulisan test dari perspektif pengguna, seperti memastikan komponen merender dengan benar, merespons interaksi (klik, ketik), dan menampilkan pesan error dengan tepat.

# Screenshot
<img width="1365" height="722" alt="Screenshot 2025-11-01 163235" src="https://github.com/user-attachments/assets/e3b297de-2860-408b-a36c-0b04cc11a117" />
<img width="1365" height="714" alt="Screenshot 2025-11-01 163331" src="https://github.com/user-attachments/assets/177343ca-4189-44c3-9032-0cd04227508b" />
<img width="1352" height="721" alt="Screenshot 2025-11-01 163543" src="https://github.com/user-attachments/assets/0cb96e75-8124-4b81-9f08-c6d036f0f5d4" />
<img width="1365" height="720" alt="Screenshot 2025-11-01 163556" src="https://github.com/user-attachments/assets/11776888-76c7-4a50-bbb7-1d0edff38426" />
<img width="1365" height="719" alt="Screenshot 2025-11-01 163610" src="https://github.com/user-attachments/assets/dc0bfd9c-3395-474b-89d1-068885ea306c" />
