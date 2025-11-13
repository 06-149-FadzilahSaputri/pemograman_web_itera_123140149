"""
items.py
========
Module ini berisi concrete classes (Book dan Magazine) yang mewarisi
dari LibraryItem. Implementasi inheritance dan polymorphism.

Author: [Nama Anda]
Date: November 2024
"""

from library_item import LibraryItem


class Book(LibraryItem):
    """
    Class untuk buku yang mewarisi dari LibraryItem.
    Implementasi konsep inheritance dan polymorphism.
    
    Attributes:
        _author (str): Nama penulis (protected)
        _pages (int): Jumlah halaman (protected)
        __isbn (str): Nomor ISBN (private - strong encapsulation)
    """
    
    def __init__(self, item_id: str, title: str, year: int, 
                 author: str, pages: int, isbn: str):
        """
        Constructor untuk Book dengan atribut tambahan.
        
        Args:
            item_id (str): ID unik buku
            title (str): Judul buku
            year (int): Tahun terbit
            author (str): Nama penulis
            pages (int): Jumlah halaman
            isbn (str): Nomor ISBN
        """
        # Memanggil constructor parent class
        super().__init__(item_id, title, year)
        
        # Atribut khusus untuk Book
        self._author = author       # Protected attribute
        self._pages = pages         # Protected attribute
        self.__isbn = isbn          # Private attribute (strong encapsulation)
    
    # ========================================================================
    # PROPERTY DECORATORS
    # ========================================================================
    
    @property
    def author(self) -> str:
        """Getter untuk author"""
        return self._author
    
    @property
    def pages(self) -> int:
        """Getter untuk pages"""
        return self._pages
    
    @property
    def isbn(self) -> str:
        """
        Getter untuk ISBN (private attribute).
        Demonstrasi akses ke private attribute melalui property.
        """
        return self.__isbn
    
    # ========================================================================
    # IMPLEMENTASI ABSTRACT METHODS (Polymorphism)
    # ========================================================================
    
    def display_info(self) -> str:
        """
        Override method dari parent class.
        Menampilkan informasi lengkap buku dengan format yang menarik.
        
        Returns:
            str: Detail lengkap buku
        """
        status = "✓ Tersedia" if self._is_available else "✗ Dipinjam"
        return f"""
╔══════════════════════════════════════════════════════════
║ BUKU
╠══════════════════════════════════════════════════════════
║ ID       : {self._item_id}
║ Judul    : {self._title}
║ Penulis  : {self._author}
║ Tahun    : {self._year}
║ Halaman  : {self._pages}
║ ISBN     : {self.__isbn}
║ Status   : {status}
╚══════════════════════════════════════════════════════════
        """
    
    def get_type(self) -> str:
        """
        Implementasi method untuk mendapatkan tipe item.
        
        Returns:
            str: Tipe item ("Buku")
        """
        return "Buku"


class Magazine(LibraryItem):
    """
    Class untuk majalah yang mewarisi dari LibraryItem.
    Implementasi konsep inheritance dan polymorphism.
    
    Attributes:
        _publisher (str): Nama penerbit (protected)
        _issue_number (int): Nomor edisi (protected)
        _month (str): Bulan terbit (protected)
    """
    
    def __init__(self, item_id: str, title: str, year: int,
                 publisher: str, issue_number: int, month: str):
        """
        Constructor untuk Magazine dengan atribut tambahan.
        
        Args:
            item_id (str): ID unik majalah
            title (str): Judul majalah
            year (int): Tahun terbit
            publisher (str): Nama penerbit
            issue_number (int): Nomor edisi
            month (str): Bulan terbit
        """
        # Memanggil constructor parent class
        super().__init__(item_id, title, year)
        
        # Atribut khusus untuk Magazine
        self._publisher = publisher          # Protected attribute
        self._issue_number = issue_number    # Protected attribute
        self._month = month                  # Protected attribute
    
    # ========================================================================
    # PROPERTY DECORATORS
    # ========================================================================
    
    @property
    def publisher(self) -> str:
        """Getter untuk publisher"""
        return self._publisher
    
    @property
    def issue_number(self) -> int:
        """Getter untuk issue_number"""
        return self._issue_number
    
    @property
    def month(self) -> str:
        """Getter untuk month"""
        return self._month
    
    # ========================================================================
    # IMPLEMENTASI ABSTRACT METHODS (Polymorphism)
    # ========================================================================
    
    def display_info(self) -> str:
        """
        Override method dari parent class.
        Menampilkan informasi lengkap majalah dengan format yang menarik.
        
        Returns:
            str: Detail lengkap majalah
        """
        status = "✓ Tersedia" if self._is_available else "✗ Dipinjam"
        return f"""
╔══════════════════════════════════════════════════════════
║ MAJALAH
╠══════════════════════════════════════════════════════════
║ ID       : {self._item_id}
║ Judul    : {self._title}
║ Penerbit : {self._publisher}
║ Edisi    : #{self._issue_number}
║ Bulan    : {self._month} {self._year}
║ Status   : {status}
╚══════════════════════════════════════════════════════════
        """
    
    def get_type(self) -> str:
        """
        Implementasi method untuk mendapatkan tipe item.
        
        Returns:
            str: Tipe item ("Majalah")
        """
        return "Majalah"