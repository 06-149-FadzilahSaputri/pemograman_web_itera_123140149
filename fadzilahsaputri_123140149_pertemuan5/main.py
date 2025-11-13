"""
main.py
=======
Entry point program sistem manajemen perpustakaan.
Demonstrasi lengkap penggunaan semua fitur dan konsep OOP.

Author: [Nama Anda]
Date: November 2024

Cara menjalankan:
    python main.py
"""

from library import Library
from items import Book, Magazine


def print_header(title: str):
    """
    Utility function untuk print header section.
    
    Args:
        title (str): Judul section
    """
    print(f"\n{title}")
    print("-" * 60)


def main():
    """
    Fungsi utama untuk demonstrasi sistem perpustakaan.
    Mendemonstrasikan semua fitur dan konsep OOP yang diimplementasikan.
    """
    print("="*60)
    print("🏛️  SISTEM MANAJEMEN PERPUSTAKAAN")
    print("     Demonstrasi Konsep OOP Python")
    print("="*60)
    
    # ========================================================================
    # INISIALISASI PERPUSTAKAAN
    # ========================================================================
    library = Library("Perpustakaan Universitas Indonesia")
    print(f"\n✓ Perpustakaan '{library.name}' berhasil dibuat!")
    
    # ========================================================================
    # MEMBUAT OBJEK BUKU (Inheritance & Encapsulation)
    # ========================================================================
    print_header("📥 MENAMBAHKAN BUKU KE PERPUSTAKAAN")
    
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
    
    library.add_item(book1)
    library.add_item(book2)
    library.add_item(book3)
    
    # ========================================================================
    # MEMBUAT OBJEK MAJALAH (Inheritance & Encapsulation)
    # ========================================================================
    print_header("📥 MENAMBAHKAN MAJALAH KE PERPUSTAKAAN")
    
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
    
    magazine3 = Magazine(
        item_id="M003",
        title="Cyber Security Today",
        year=2024,
        publisher="SecurePress",
        issue_number=45,
        month="November"
    )
    
    library.add_item(magazine1)
    library.add_item(magazine2)
    library.add_item(magazine3)
    
    # ========================================================================
    # VALIDASI: MENCOBA MENAMBAH ITEM DENGAN ID DUPLIKAT
    # ========================================================================
    print_header("🔄 VALIDASI: MENCOBA ID DUPLIKAT")
    duplicate_book = Book("B001", "Duplicate Book", 2024, "Unknown", 100, "000-000")
    library.add_item(duplicate_book)
    
    # ========================================================================
    # MENAMPILKAN SEMUA ITEM (Polymorphism)
    # ========================================================================
    library.display_all_items()
    
    # ========================================================================
    # MENAMPILKAN DETAIL ITEM (Polymorphism - display_info())
    # ========================================================================
    library.display_detailed_items()
    
    # ========================================================================
    # PENCARIAN BERDASARKAN JUDUL
    # ========================================================================
    print_header("🔍 PENCARIAN BERDASARKAN JUDUL")
    library.search_by_title("python")
    
    print_header("🔍 PENCARIAN KATA 'SAINS'")
    library.search_by_title("sains")
    
    # ========================================================================
    # PENCARIAN BERDASARKAN ID
    # ========================================================================
    print_header("🔍 PENCARIAN BERDASARKAN ID")
    library.search_by_id("B002")
    library.search_by_id("M001")
    
    # ========================================================================
    # PENCARIAN BERDASARKAN TIPE
    # ========================================================================
    print_header("🔍 PENCARIAN SEMUA BUKU")
    library.search_by_type("book")
    
    print_header("🔍 PENCARIAN SEMUA MAJALAH")
    library.search_by_type("magazine")
    
    # ========================================================================
    # OPERASI PEMINJAMAN
    # ========================================================================
    print_header("📤 PEMINJAMAN ITEM")
    library.borrow_item("B001")
    library.borrow_item("M001")
    library.borrow_item("B003")
    
    # Validasi: Mencoba meminjam item yang sudah dipinjam
    print_header("🔄 VALIDASI: MEMINJAM ITEM YANG SUDAH DIPINJAM")
    library.borrow_item("B001")
    
    # Menampilkan status setelah peminjaman
    library.display_all_items()
    
    # ========================================================================
    # OPERASI PENGEMBALIAN
    # ========================================================================
    print_header("📥 PENGEMBALIAN ITEM")
    library.return_item("B001")
    library.return_item("M001")
    
    # Validasi: Mencoba mengembalikan item yang tidak dipinjam
    print_header("🔄 VALIDASI: MENGEMBALIKAN ITEM YANG TIDAK DIPINJAM")
    library.return_item("B002")
    
    # Menampilkan status setelah pengembalian
    library.display_all_items()
    
    # ========================================================================
    # STATISTIK PERPUSTAKAAN
    # ========================================================================
    library.get_statistics()
    
    # ========================================================================
    # DEMONSTRASI PROPERTY & ENCAPSULATION
    # ========================================================================
    print_header("🔐 DEMONSTRASI ENCAPSULATION & PROPERTY")
    print(f"Nama Perpustakaan : {library.name}")
    print(f"Total Item        : {library.total_items}")
    print(f"Item Tersedia     : {library.available_items}")
    print()
    print("Akses atribut buku melalui property:")
    print(f"  - Judul  : {book1.title}")
    print(f"  - Penulis: {book1.author}")
    print(f"  - ISBN   : {book1.isbn}")  # Akses private attribute via property
    print()
    
    # ========================================================================
    # DEMONSTRASI POLYMORPHISM
    # ========================================================================
    print_header("🔄 DEMONSTRASI POLYMORPHISM")
    print("Method get_type() mengembalikan nilai berbeda untuk setiap class:\n")
    print(f"book1.get_type()     = {book1.get_type()}")
    print(f"magazine1.get_type() = {magazine1.get_type()}")
    print()
    print("Method display_info() memiliki implementasi berbeda:")
    print(book1.display_info())
    print(magazine1.display_info())
    
    # ========================================================================
    # PENUTUP
    # ========================================================================
    print("="*60)
    print("✓ Demonstrasi Program Selesai")
    print("="*60)
    print("\n📝 KONSEP OOP YANG DITERAPKAN:")
    print("  ✅ Abstract Class (LibraryItem)")
    print("  ✅ Inheritance (Book, Magazine)")
    print("  ✅ Encapsulation (Protected & Private Attributes)")
    print("  ✅ Property Decorator (@property)")
    print("  ✅ Polymorphism (display_info, get_type)")
    print("  ✅ Composition (Library memiliki LibraryItem)")
    print("="*60)


# ============================================================================
# MENU INTERAKTIF (Bonus)
# ============================================================================

def interactive_menu():
    """
    Menu interaktif untuk pengguna.
    Bonus: Memungkinkan user untuk berinteraksi dengan sistem.
    """
    library = Library("Perpustakaan Saya")
    
    while True:
        print("\n" + "="*60)
        print("📚 MENU PERPUSTAKAAN")
        print("="*60)
        print("1. Tambah Buku")
        print("2. Tambah Majalah")
        print("3. Tampilkan Semua Item")
        print("4. Cari Item")
        print("5. Pinjam Item")
        print("6. Kembalikan Item")
        print("7. Statistik")
        print("0. Keluar")
        print("="*60)
        
        choice = input("Pilih menu (0-7): ").strip()
        
        if choice == "1":
            # Tambah buku
            print("\n--- Tambah Buku ---")
            item_id = input("ID Buku: ")
            title = input("Judul: ")
            year = int(input("Tahun: "))
            author = input("Penulis: ")
            pages = int(input("Jumlah Halaman: "))
            isbn = input("ISBN: ")
            
            book = Book(item_id, title, year, author, pages, isbn)
            library.add_item(book)
        
        elif choice == "2":
            # Tambah majalah
            print("\n--- Tambah Majalah ---")
            item_id = input("ID Majalah: ")
            title = input("Judul: ")
            year = int(input("Tahun: "))
            publisher = input("Penerbit: ")
            issue_number = int(input("Nomor Edisi: "))
            month = input("Bulan: ")
            
            magazine = Magazine(item_id, title, year, publisher, issue_number, month)
            library.add_item(magazine)
        
        elif choice == "3":
            library.display_all_items()
        
        elif choice == "4":
            keyword = input("\nMasukkan kata kunci pencarian: ")
            library.search_by_title(keyword)
        
        elif choice == "5":
            item_id = input("\nMasukkan ID item yang akan dipinjam: ")
            library.borrow_item(item_id)
        
        elif choice == "6":
            item_id = input("\nMasukkan ID item yang akan dikembalikan: ")
            library.return_item(item_id)
        
        elif choice == "7":
            library.get_statistics()
        
        elif choice == "0":
            print("\n✓ Terima kasih telah menggunakan sistem perpustakaan!")
            break
        
        else:
            print("\n❌ Pilihan tidak valid!")


# ============================================================================
# ENTRY POINT
# ============================================================================

if __name__ == "__main__":
    # Jalankan demonstrasi otomatis
    main()
    
    # Uncomment baris di bawah untuk menjalankan menu interaktif
    # print("\n\n")
    # interactive_menu()