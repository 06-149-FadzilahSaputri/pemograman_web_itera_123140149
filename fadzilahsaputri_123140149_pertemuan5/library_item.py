"""
library_item.py
===============
Module ini berisi abstract base class LibraryItem yang menjadi blueprint
untuk semua jenis item di perpustakaan.

Author: [Nama Anda]
Date: November 2024
"""

from abc import ABC, abstractmethod


class LibraryItem(ABC):
    """
    Abstract base class untuk semua item perpustakaan.
    Menerapkan konsep abstraksi dan menjadi blueprint untuk subclass.
    
    Attributes:
        _item_id (str): ID unik item (protected)
        _title (str): Judul item (protected)
        _year (int): Tahun publikasi (protected)
        _is_available (bool): Status ketersediaan item (protected)
    """
    
    def __init__(self, item_id: str, title: str, year: int):
        """
        Constructor untuk inisialisasi atribut dasar item perpustakaan.
        
        Args:
            item_id (str): ID unik item
            title (str): Judul item
            year (int): Tahun publikasi
        """
        self._item_id = item_id      # Protected attribute
        self._title = title          # Protected attribute
        self._year = year            # Protected attribute
        self._is_available = True    # Protected attribute
    
    # ========================================================================
    # PROPERTY DECORATORS (Encapsulation)
    # ========================================================================
    
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
        """
        Setter untuk status ketersediaan.
        
        Args:
            status (bool): Status ketersediaan baru
        """
        self._is_available = status
    
    # ========================================================================
    # ABSTRACT METHODS (harus diimplementasikan oleh subclass)
    # ========================================================================
    
    @abstractmethod
    def display_info(self) -> str:
        """
        Abstract method yang harus diimplementasikan oleh subclass.
        Menampilkan informasi detail item.
        
        Returns:
            str: String representasi detail item
        """
        pass
    
    @abstractmethod
    def get_type(self) -> str:
        """
        Abstract method untuk mendapatkan tipe item.
        
        Returns:
            str: Tipe item (contoh: "Buku", "Majalah")
        """
        pass
    
    # ========================================================================
    # CONCRETE METHODS
    # ========================================================================
    
    def __str__(self) -> str:
        """
        String representation untuk item.
        
        Returns:
            str: String representasi singkat item
        """
        status = "Tersedia" if self._is_available else "Dipinjam"
        return f"[{self._item_id}] {self._title} ({self._year}) - {status}"
    
    def __repr__(self) -> str:
        """
        Developer-friendly representation.
        
        Returns:
            str: Representasi untuk debugging
        """
        return f"{self.__class__.__name__}(id='{self._item_id}', title='{self._title}')"