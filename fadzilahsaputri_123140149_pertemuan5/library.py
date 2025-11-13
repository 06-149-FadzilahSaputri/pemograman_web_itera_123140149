"""
library.py
==========
Module ini berisi class Library untuk mengelola koleksi perpustakaan.
Implementasi encapsulation, composition, dan berbagai operasi manajemen.

Author: [Nama Anda]
Date: November 2024
"""

from typing import List, Optional
from library_item import LibraryItem
from items import Book, Magazine


class Library:
    """
    Class untuk mengelola koleksi perpustakaan.
    Implementasi encapsulation dan composition.
    
    Attributes:
        __name (str): Nama perpustakaan (private)
        __items (List[LibraryItem]): Koleksi item perpustakaan (private)
        __borrowed_count (int): Jumlah total peminjaman (private)
    """
    
    def __init__(self, name: str):
        """
        Constructor untuk Library.
        
        Args:
            name (str): Nama perpustakaan
        """
        self.__name = name                    # Private attribute
        self.__items: List[LibraryItem] = []  # Private attribute - composition
        self.__borrowed_count = 0             # Private attribute
    
    # ========================================================================
    # PROPERTY DECORATORS (Encapsulation)
    # ========================================================================
    
    @property
    def name(self) -> str:
        """Getter untuk nama perpustakaan"""
        return self.__name
    
    @property
    def total_items(self) -> int:
        """
        Getter untuk total item di perpustakaan.
        
        Returns:
            int: Jumlah total item
        """
        return len(self.__items)
    
    @property
    def available_items(self) -> int:
        """
        Getter untuk jumlah item yang tersedia (tidak dipinjam).
        
        Returns:
            int: Jumlah item tersedia
        """
        return sum(1 for item in self.__items if item.is_available)
    
    # ========================================================================
    # CRUD OPERATIONS
    # ========================================================================
    
    def add_item(self, item: LibraryItem) -> bool:
        """
        Menambahkan item ke perpustakaan.
        Validasi: ID harus unik.
        
        Args:
            item (LibraryItem): Object LibraryItem atau turunannya
            
        Returns:
            bool: True jika berhasil, False jika ID sudah ada
        """
        # Validasi: cek apakah ID sudah ada
        if any(i.item_id == item.item_id for i in self.__items):
            print(f"❌ Error: Item dengan ID '{item.item_id}' sudah ada!")
            return False
        
        self.__items.append(item)
        print(f"✓ Item '{item.title}' berhasil ditambahkan ke perpustakaan.")
        return True
    
    def remove_item(self, item_id: str) -> bool:
        """
        Menghapus item dari perpustakaan berdasarkan ID.
        
        Args:
            item_id (str): ID item yang akan dihapus
            
        Returns:
            bool: True jika berhasil, False jika tidak ditemukan
        """
        for i, item in enumerate(self.__items):
            if item.item_id == item_id:
                removed_item = self.__items.pop(i)
                print(f"✓ Item '{removed_item.title}' berhasil dihapus.")
                return True
        
        print(f"❌ Item dengan ID '{item_id}' tidak ditemukan.")
        return False
    
    # ========================================================================
    # DISPLAY METHODS
    # ========================================================================
    
    def display_all_items(self):
        """
        Menampilkan semua item yang ada di perpustakaan (ringkas).
        Demonstrasi polymorphism - method __str__() berbeda untuk setiap subclass.
        """
        if not self.__items:
            print("\n📚 Perpustakaan masih kosong.")
            return
        
        print(f"\n{'='*60}")
        print(f"📚 DAFTAR KOLEKSI {self.__name.upper()}")
        print(f"{'='*60}")
        print(f"Total Item: {self.total_items} | Tersedia: {self.available_items}")
        print(f"{'='*60}\n")
        
        for item in self.__items:
            print(item)  # Menggunakan __str__ method
        print()
    
    def display_detailed_items(self):
        """
        Menampilkan detail lengkap semua item.
        Demonstrasi polymorphism dengan method display_info().
        """
        if not self.__items:
            print("\n📚 Perpustakaan masih kosong.")
            return
        
        print(f"\n{'='*60}")
        print(f"📚 DETAIL KOLEKSI {self.__name.upper()}")
        print(f"{'='*60}\n")
        
        for item in self.__items:
            print(item.display_info())  # Polymorphism in action!
    
    # ========================================================================
    # SEARCH METHODS
    # ========================================================================
    
    def search_by_title(self, keyword: str) -> List[LibraryItem]:
        """
        Mencari item berdasarkan judul (case-insensitive).
        
        Args:
            keyword (str): Kata kunci pencarian
            
        Returns:
            List[LibraryItem]: List item yang ditemukan
        """
        keyword_lower = keyword.lower()
        results = [item for item in self.__items 
                  if keyword_lower in item.title.lower()]
        
        if results:
            print(f"\n🔍 Ditemukan {len(results)} item dengan keyword '{keyword}':\n")
            for item in results:
                print(item)
        else:
            print(f"\n❌ Tidak ditemukan item dengan keyword '{keyword}'")
        
        return results
    
    def search_by_id(self, item_id: str) -> Optional[LibraryItem]:
        """
        Mencari item berdasarkan ID.
        
        Args:
            item_id (str): ID item yang dicari
            
        Returns:
            Optional[LibraryItem]: Item jika ditemukan, None jika tidak
        """
        for item in self.__items:
            if item.item_id == item_id:
                print(f"\n✓ Item ditemukan:")
                print(item.display_info())
                return item
        
        print(f"\n❌ Item dengan ID '{item_id}' tidak ditemukan.")
        return None
    
    def search_by_type(self, item_type: str) -> List[LibraryItem]:
        """
        Mencari item berdasarkan tipe (Buku/Majalah).
        
        Args:
            item_type (str): Tipe item ("book" atau "magazine")
            
        Returns:
            List[LibraryItem]: List item dengan tipe tersebut
        """
        if item_type.lower() == "book":
            results = [item for item in self.__items if isinstance(item, Book)]
        elif item_type.lower() == "magazine":
            results = [item for item in self.__items if isinstance(item, Magazine)]
        else:
            print(f"❌ Tipe '{item_type}' tidak valid. Gunakan 'book' atau 'magazine'.")
            return []
        
        if results:
            print(f"\n🔍 Ditemukan {len(results)} {item_type}:\n")
            for item in results:
                print(item)
        else:
            print(f"\n❌ Tidak ada {item_type} dalam perpustakaan.")
        
        return results
    
    # ========================================================================
    # BORROWING OPERATIONS
    # ========================================================================
    
    def borrow_item(self, item_id: str) -> bool:
        """
        Meminjam item dari perpustakaan.
        
        Args:
            item_id (str): ID item yang akan dipinjam
            
        Returns:
            bool: True jika berhasil, False jika gagal
        """
        # Cari item berdasarkan ID tanpa print detail
        item = None
        for i in self.__items:
            if i.item_id == item_id:
                item = i
                break
        
        if item is None:
            print(f"\n❌ Item dengan ID '{item_id}' tidak ditemukan.")
            return False
        
        if not item.is_available:
            print(f"\n❌ Item '{item.title}' sedang dipinjam.")
            return False
        
        item.is_available = False
        self.__borrowed_count += 1
        print(f"\n✓ Item '{item.title}' berhasil dipinjam.")
        return True
    
    def return_item(self, item_id: str) -> bool:
        """
        Mengembalikan item ke perpustakaan.
        
        Args:
            item_id (str): ID item yang akan dikembalikan
            
        Returns:
            bool: True jika berhasil, False jika gagal
        """
        # Cari item berdasarkan ID tanpa print detail
        item = None
        for i in self.__items:
            if i.item_id == item_id:
                item = i
                break
        
        if item is None:
            print(f"\n❌ Item dengan ID '{item_id}' tidak ditemukan.")
            return False
        
        if item.is_available:
            print(f"\n❌ Item '{item.title}' tidak sedang dipinjam.")
            return False
        
        item.is_available = True
        print(f"\n✓ Item '{item.title}' berhasil dikembalikan.")
        return True
    
    # ========================================================================
    # STATISTICS
    # ========================================================================
    
    def get_statistics(self):
        """
        Menampilkan statistik perpustakaan lengkap.
        """
        books = sum(1 for item in self.__items if isinstance(item, Book))
        magazines = sum(1 for item in self.__items if isinstance(item, Magazine))
        
        print(f"\n{'='*60}")
        print(f"📊 STATISTIK {self.__name.upper()}")
        print(f"{'='*60}")
        print(f"Total Item      : {self.total_items}")
        print(f"  - Buku        : {books}")
        print(f"  - Majalah     : {magazines}")
        print(f"Item Tersedia   : {self.available_items}")
        print(f"Item Dipinjam   : {self.total_items - self.available_items}")
        print(f"Total Peminjaman: {self.__borrowed_count}")
        print(f"{'='*60}\n")