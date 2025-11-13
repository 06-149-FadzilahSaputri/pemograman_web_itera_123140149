"""
main.py
=======
Entry point program sistem manajemen perpustakaan.
Program interaktif dengan menu untuk user.

Author: [Nama Anda]
Date: November 2024

Cara menjalankan:
    python main.py
"""

from library import Library
from items import Book, Magazine


def clear_screen():
    """Utility function untuk membersihkan layar (opsional)"""
    print("\n" * 2)


def print_header(title: str):
    """
    Utility function untuk print header section.
    
    Args:
        title (str): Judul section
    """
    print(f"\n{'='*60}")
    print(f"  {title}")
    print(f"{'='*60}")


def initialize_sample_data(library: Library):
    """
    Menginisialisasi data sample untuk demonstrasi.
    User bisa skip ini dan input data sendiri.
    
    Args:
        library (Library): Instance perpustakaan
    """
    # Sample Books
    book1 = Book(
        item_id="B001",
        title="Pemrograman Python untuk Pemula",
        year=2023,
        author="Dr. Budi Santoso",
        pages=450,
        isbn="978-602-1234-56-7"
    )
    
    book2 = Book(
        item_id="B002",
        title="Algoritma dan Struktur Data",
        year=2022,
        author="Prof. Ahmad Dahlan",
        pages=520,
        isbn="978-602-9876-54-3"
    )
    
    book3 = Book(
        item_id="B003",
        title="Machine Learning dengan Python",
        year=2024,
        author="Dr. Siti Nurhaliza",
        pages=680,
        isbn="978-602-5555-12-8"
    )
    
    # Sample Magazines
    magazine1 = Magazine(
        item_id="M001",
        title="InfoTech Indonesia",
        year=2024,
        publisher="TechMedia",
        issue_number=156,
        month="Oktober"
    )
    
    magazine2 = Magazine(
        item_id="M002",
        title="Sains Komputer",
        year=2024,
        publisher="Gramedia",
        issue_number=89,
        month="November"
    )
    
    # Tambahkan ke library
    library.add_item(book1)
    library.add_item(book2)
    library.add_item(book3)
    library.add_item(magazine1)
    library.add_item(magazine2)


def menu_tambah_buku(library: Library):
    """Menu untuk menambah buku baru"""
    print_header("📖 TAMBAH BUKU BARU")
    
    try:
        item_id = input("ID Buku (contoh: B001): ").strip()
        if not item_id:
            print("❌ ID tidak boleh kosong!")
            return
        
        title = input("Judul Buku: ").strip()
        if not title:
            print("❌ Judul tidak boleh kosong!")
            return
        
        year = int(input("Tahun Terbit: "))
        author = input("Nama Penulis: ").strip()
        pages = int(input("Jumlah Halaman: "))
        isbn = input("Nomor ISBN: ").strip()
        
        book = Book(item_id, title, year, author, pages, isbn)
        library.add_item(book)
        
    except ValueError:
        print("❌ Error: Input tahun/halaman harus berupa angka!")
    except Exception as e:
        print(f"❌ Error: {e}")


def menu_tambah_majalah(library: Library):
    """Menu untuk menambah majalah baru"""
    print_header("📰 TAMBAH MAJALAH BARU")
    
    try:
        item_id = input("ID Majalah (contoh: M001): ").strip()
        if not item_id:
            print("❌ ID tidak boleh kosong!")
            return
        
        title = input("Judul Majalah: ").strip()
        if not title:
            print("❌ Judul tidak boleh kosong!")
            return
        
        year = int(input("Tahun Terbit: "))
        publisher = input("Nama Penerbit: ").strip()
        issue_number = int(input("Nomor Edisi: "))
        month = input("Bulan Terbit: ").strip()
        
        magazine = Magazine(item_id, title, year, publisher, issue_number, month)
        library.add_item(magazine)
        
    except ValueError:
        print("❌ Error: Input tahun/nomor edisi harus berupa angka!")
    except Exception as e:
        print(f"❌ Error: {e}")


def menu_tampilkan_items(library: Library):
    """Menu untuk menampilkan items"""
    print_header("📚 TAMPILKAN KOLEKSI")
    print("1. Tampilkan Ringkas")
    print("2. Tampilkan Detail Lengkap")
    print("3. Tampilkan Buku Saja")
    print("4. Tampilkan Majalah Saja")
    
    choice = input("\nPilih opsi (1-4): ").strip()
    
    if choice == "1":
        library.display_all_items()
    elif choice == "2":
        library.display_detailed_items()
    elif choice == "3":
        library.search_by_type("book")
    elif choice == "4":
        library.search_by_type("magazine")
    else:
        print("❌ Pilihan tidak valid!")


def menu_cari_item(library: Library):
    """Menu untuk mencari item"""
    print_header("🔍 CARI ITEM")
    print("1. Cari berdasarkan Judul")
    print("2. Cari berdasarkan ID")
    print("3. Cari berdasarkan Tipe (Buku/Majalah)")
    
    choice = input("\nPilih opsi (1-3): ").strip()
    
    if choice == "1":
        keyword = input("\nMasukkan kata kunci judul: ").strip()
        if keyword:
            library.search_by_title(keyword)
        else:
            print("❌ Kata kunci tidak boleh kosong!")
    
    elif choice == "2":
        item_id = input("\nMasukkan ID item: ").strip()
        if item_id:
            library.search_by_id(item_id)
        else:
            print("❌ ID tidak boleh kosong!")
    
    elif choice == "3":
        print("\nTipe:")
        print("1. Buku")
        print("2. Majalah")
        type_choice = input("Pilih (1-2): ").strip()
        
        if type_choice == "1":
            library.search_by_type("book")
        elif type_choice == "2":
            library.search_by_type("magazine")
        else:
            print("❌ Pilihan tidak valid!")
    else:
        print("❌ Pilihan tidak valid!")


def menu_pinjam_item(library: Library):
    """Menu untuk meminjam item"""
    print_header("📤 PINJAM ITEM")
    
    # Tampilkan item yang tersedia
    print("\nItem yang tersedia untuk dipinjam:")
    items_available = False
    for i in range(library.total_items):
        # Kita perlu cara untuk akses items, tapi __items private
        # Solusi: tampilkan semua dulu
        pass
    
    library.display_all_items()
    
    item_id = input("\nMasukkan ID item yang akan dipinjam: ").strip()
    if item_id:
        library.borrow_item(item_id)
    else:
        print("❌ ID tidak boleh kosong!")


def menu_kembalikan_item(library: Library):
    """Menu untuk mengembalikan item"""
    print_header("📥 KEMBALIKAN ITEM")
    
    # Tampilkan semua item
    library.display_all_items()
    
    item_id = input("\nMasukkan ID item yang akan dikembalikan: ").strip()
    if item_id:
        library.return_item(item_id)
    else:
        print("❌ ID tidak boleh kosong!")


def menu_hapus_item(library: Library):
    """Menu untuk menghapus item"""
    print_header("🗑️  HAPUS ITEM")
    
    # Tampilkan semua item
    library.display_all_items()
    
    item_id = input("\nMasukkan ID item yang akan dihapus: ").strip()
    if item_id:
        confirm = input(f"Yakin ingin menghapus item '{item_id}'? (y/n): ").strip().lower()
        if confirm == 'y':
            library.remove_item(item_id)
        else:
            print("❌ Penghapusan dibatalkan.")
    else:
        print("❌ ID tidak boleh kosong!")


def interactive_menu():
    """
    Menu interaktif utama untuk pengguna.
    User dapat berinteraksi dengan sistem perpustakaan.
    """
    # Banner
    print("="*60)
    print("🏛️  SISTEM MANAJEMEN PERPUSTAKAAN")
    print("     Object-Oriented Programming (OOP) Python")
    print("="*60)
    
    # Input nama perpustakaan
    library_name = input("\n📝 Masukkan nama perpustakaan: ").strip()
    if not library_name:
        library_name = "Perpustakaan Saya"
    
    library = Library(library_name)
    print(f"\n✓ Perpustakaan '{library.name}' berhasil dibuat!")
    
    # Tanya apakah mau load sample data
    print("\n" + "="*60)
    load_sample = input("Mau load data contoh? (y/n): ").strip().lower()
    if load_sample == 'y':
        print("\n⏳ Memuat data contoh...")
        initialize_sample_data(library)
        print("✓ Data contoh berhasil dimuat!")
    
    # Main loop
    while True:
        print("\n" + "="*60)
        print(f"📚 MENU UTAMA - {library.name.upper()}")
        print("="*60)
        print("1.  Tambah Buku")
        print("2.  Tambah Majalah")
        print("3.  Tampilkan Koleksi")
        print("4.  Cari Item")
        print("5.  Pinjam Item")
        print("6.  Kembalikan Item")
        print("7.  Hapus Item")
        print("8.  Statistik Perpustakaan")
        print("9.  Demonstrasi Konsep OOP")
        print("0.  Keluar")
        print("="*60)
        
        choice = input("Pilih menu (0-9): ").strip()
        
        if choice == "1":
            menu_tambah_buku(library)
        
        elif choice == "2":
            menu_tambah_majalah(library)
        
        elif choice == "3":
            menu_tampilkan_items(library)
        
        elif choice == "4":
            menu_cari_item(library)
        
        elif choice == "5":
            menu_pinjam_item(library)
        
        elif choice == "6":
            menu_kembalikan_item(library)
        
        elif choice == "7":
            menu_hapus_item(library)
        
        elif choice == "8":
            library.get_statistics()
        
        elif choice == "9":
            demonstrasi_oop(library)
        
        elif choice == "0":
            print("\n" + "="*60)
            print("✓ Terima kasih telah menggunakan sistem perpustakaan!")
            print("="*60)
            break
        
        else:
            print("\n❌ Pilihan tidak valid! Silakan pilih 0-9.")
        
        # Pause sebelum kembali ke menu
        input("\n⏎ Tekan Enter untuk kembali ke menu...")


def demonstrasi_oop(library: Library):
    """
    Demonstrasi konsep OOP yang diterapkan.
    Menjelaskan konsep-konsep yang digunakan dalam program.
    """
    print_header("🎓 DEMONSTRASI KONSEP OOP")
    
    print("""
Sistem ini menerapkan 6 konsep utama OOP:

1. ABSTRACT CLASS (Abstraction)
   - LibraryItem sebagai abstract base class
   - Memiliki abstract methods: display_info() dan get_type()
   - Subclass WAJIB mengimplementasikan abstract methods

2. INHERITANCE (Pewarisan)
   - Book mewarisi dari LibraryItem
   - Magazine mewarisi dari LibraryItem
   - Menggunakan super().__init__() untuk constructor parent

3. ENCAPSULATION (Enkapsulasi)
   - Protected attributes: _item_id, _title, _year
   - Private attributes: __isbn (Book), __name (Library)
   - Akses melalui property decorator (@property)

4. POLYMORPHISM (Polimorfisme)
   - Method display_info() berbeda untuk Book dan Magazine
   - Method get_type() mengembalikan nilai berbeda
   - Satu interface, banyak implementasi

5. PROPERTY DECORATOR
   - Semua atribut diakses melalui getter/setter
   - Kontrol akses dan validasi data
   - Contoh: @property untuk item_id, title, dll

6. COMPOSITION
   - Library memiliki (has-a) LibraryItem
   - Library mengelola koleksi item perpustakaan
    """)
    
    # Demonstrasi praktis jika ada data
    if library.total_items > 0:
        print("\n" + "-"*60)
        print("CONTOH POLYMORPHISM:")
        print("-"*60)
        print("\nMethod display_info() menghasilkan output berbeda:")
        library.display_detailed_items()
    else:
        print("\n💡 Tip: Tambahkan item dulu untuk melihat demonstrasi praktis!")


def demonstrasi_otomatis():
    """
    Fungsi demonstrasi otomatis (untuk keperluan testing/presentasi).
    Tidak digunakan di menu utama, tapi bisa dipanggil manual.
    """
    print("="*60)
    print("🏛️  DEMONSTRASI OTOMATIS SISTEM PERPUSTAKAAN")
    print("="*60)
    
    library = Library("Perpustakaan Demo")
    
    print("\n📥 Menambahkan data sample...")
    initialize_sample_data(library)
    
    print("\n📚 Menampilkan semua item...")
    library.display_all_items()
    
    print("\n🔍 Mencari item dengan keyword 'python'...")
    library.search_by_title("python")
    
    print("\n📤 Meminjam beberapa item...")
    library.borrow_item("B001")
    library.borrow_item("M001")
    
    print("\n📊 Menampilkan statistik...")
    library.get_statistics()
    
    print("\n✓ Demonstrasi selesai!")


# ============================================================================
# ENTRY POINT
# ============================================================================

if __name__ == "__main__":
    # Mode 1: Menu Interaktif (DEFAULT)
    interactive_menu()
    
    # Mode 2: Demonstrasi Otomatis (uncomment jika perlu)
    # demonstrasi_otomatis()