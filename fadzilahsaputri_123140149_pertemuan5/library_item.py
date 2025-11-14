from abc import ABC, abstractmethod


class LibraryItem(ABC):
    """
    Abstract base class untuk semua item perpustakaan.
    Menerapkan konsep abstraksi dan menjadi blueprint untuk subclass.    
    """
    
    def __init__(self, item_id: str, title: str, year: int): #_item_id (str): ID unik item (protected), _title (str): Judul item (protected), _year (int): Tahun publikasi (protected)
        """Constructor untuk inisialisasi atribut dasar item perpustakaan."""
        self._item_id = item_id      # Protected attribute item_id (str): ID unik item
        self._title = title          # Protected attribute title (str): Judul item
        self._year = year            # Protected attribute year (int): Tahun publikasi
        self._is_available = True    # Protected attribute _is_available (bool): Status ketersediaan item (protected)
    
    # PROPERTY DECORATORS (Encapsulation)
    
    @property
    def item_id(self) -> str:
        """Getter untuk item_id"""
        return self._item_id
    
    @property
    def title(self) -> str:
        """Getter untuk title"""
        return self._title
    
    @property
    def year(self) -> int:
        """Getter untuk year"""
        return self._year
    
    @property
    def is_available(self) -> bool:
        """Getter untuk status ketersediaan"""
        return self._is_available
    
    @is_available.setter
    def is_available(self, status: bool):
        """Setter untuk status ketersediaan."""
        self._is_available = status
    
    # ABSTRACT METHODS (harus diimplementasikan oleh subclass)
    
    @abstractmethod
    def display_info(self) -> str:
        """Abstract method yang harus diimplementasikan oleh subclass."""
        pass
    
    @abstractmethod
    def get_type(self) -> str:
        """Abstract method untuk mendapatkan tipe item."""
        pass
    
    # CONCRETE METHODS
    
    def __str__(self) -> str:
        """String representation untuk item."""
        status = "Tersedia" if self._is_available else "Dipinjam"
        return f"[{self._item_id}] {self._title} ({self._year}) - {status}"
    
    def __repr__(self) -> str:
        """Developer-friendly representation."""
        return f"{self.__class__.__name__}(id='{self._item_id}', title='{self._title}')"