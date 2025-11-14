from library_item import LibraryItem

class Book(LibraryItem):
    """
    Class untuk buku yang mewarisi dari LibraryItem.
    Implementasi konsep inheritance dan polymorphism.
    """
    
    def __init__(self, item_id: str, title: str, year: int, 
                 author: str, pages: int, isbn: str):
        """Constructor untuk Book dengan atribut tambahan."""
        # Memanggil constructor parent class
        super().__init__(item_id, title, year) #item_id (str): ID unik buku, title (str): Judul buku, year (int): Tahun terbit
        
        # Atribut khusus untuk Book
        self._author = author       # Protected attribute author (str): Nama penulis
        self._pages = pages         # Protected attribute pages (int): Jumlah halaman
        self.__isbn = isbn          # Private attribute (strong encapsulation) isbn (str): Nomor ISBN
    
    # PROPERTY DECORATORS
    
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
    
    # IMPLEMENTASI ABSTRACT METHODS (Polymorphism)
    
    def display_info(self) -> str:
        """
        Override method dari parent class.
        Menampilkan informasi lengkap buku dengan format yang menarik.
        
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
        """Implementasi method untuk mendapatkan tipe item."""
        return "Buku"


class Magazine(LibraryItem):
    """
    Class untuk majalah yang mewarisi dari LibraryItem.
    Implementasi konsep inheritance dan polymorphism.
    
    """
    
    def __init__(self, item_id: str, title: str, year: int,
                 publisher: str, issue_number: int, month: str):
        """Constructor untuk Magazine dengan atribut tambahan."""
        # Memanggil constructor parent class
        super().__init__(item_id, title, year) #item_id (str): ID unik majalah, title (str): Judul majalah, year (int): Tahun terbit
        
        # Atribut khusus untuk Magazine
        self._publisher = publisher          # Protected attribute publisher (str): Nama penerbit
        self._issue_number = issue_number    # Protected attribute issue_number (int): Nomor edisi
        self._month = month                  # Protected attribute month (str): Bulan terbit
    
    # PROPERTY DECORATORS
    
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
    
    # IMPLEMENTASI ABSTRACT METHODS (Polymorphism)
    
    def display_info(self) -> str:
        """
        Override method dari parent class.
        Menampilkan informasi lengkap majalah dengan format yang menarik.
        """
        status = " Tersedia" if self._is_available else " Dipinjam"
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
        """Implementasi method untuk mendapatkan tipe item."""
        return "Majalah"