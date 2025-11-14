#  Sistem Manajemen Perpustakaan - OOP Python

Sistem manajemen perpustakaan interaktif yang dibangun menggunakan konsep Object-Oriented Programming (OOP) dalam Python. Program ini memungkinkan user untuk mengelola koleksi buku dan majalah dengan mudah melalui menu interaktif.

---

### Penjelasan Struktur File

| File | Fungsi | Konsep OOP |
| :--- | :--- | :--- |
| `library_item.py` | Abstract base class untuk semua item | Abstraction, Encapsulation |
| `items.py` | Class `Book` dan `Magazine` | Inheritance, Polymorphism |
| `library.py` | Manajemen koleksi perpustakaan | Composition, Encapsulation |
| `main.py` | Interface user & menu interaktif | - |

---

##  Konsep OOP yang Diterapkan

### 1. Abstract Class & Abstraction

```python
from abc import ABC, abstractmethod

class LibraryItem(ABC):
    @abstractmethod
    def display_info(self) -> str:
        pass
    
    @abstractmethod
    def get_type(self) -> str:
        pass
```
- LibraryItem sebagai abstract base class.
- Memiliki 2 abstract methods yang wajib diimplementasikan.
- Menggunakan module abc (Abstract Base Classes).

### 2. Inheritance (Pewarisan)

```python
class Book(LibraryItem):
    def __init__(self, ...):
        super().__init__(item_id, title, year)
        # atribut tambahan...

class Magazine(LibraryItem):
    def __init__(self, ...):
        super().__init__(item_id, title, year)
        # atribut tambahan...
```
- Book dan Magazine mewarisi dari LibraryItem.
- Menggunakan super() untuk memanggil constructor parent.
- Menambahkan atribut spesifik untuk setiap subclass.

### 3. Encapsulation (Enkapsulasi)

```python
class Book(LibraryItem):
    def __init__(self, ...):
        self._author = author      # Protected
        self._pages = pages        # Protected
        self.__isbn = isbn         # Private
    
    @property
    def isbn(self):
        return self.__isbn
```
- Protected (_): Dapat diakses subclass.
- Private (__): Hanya dapat diakses dalam class itu sendiri.
- Property decorator: Kontrol akses ke atribut.

### 4. Polymorphism (Polimorfisme)

```python
# Book version
def display_info(self) -> str:
    return "Detail Buku..."

# Magazine version
def display_info(self) -> str:
    return "Detail Majalah..."
```
- Method yang sama, implementasi berbeda.
- Runtime polymorphism melalui method overriding.
- Satu interface, banyak bentuk.

### 5. Property Decorator

```python
@property
def title(self) -> str:
    return self._title

@is_available.setter
def is_available(self, status: bool):
    self._is_available = status
```
- Getter dan setter untuk kontrol akses.
- Validasi data sebelum di-set.
- Pythonic way untuk encapsulation.

### 6. Composition

```python
class Library:
    def __init__(self, name: str):
        self.__items: List[LibraryItem] = []
```
- Library "has-a" LibraryItem.
- Relationship: Composition (Library memiliki koleksi item).
- Library mengelola lifecycle item.

## Screenshot Hasil Running Program
![alt text](<Screenshot 2025-11-14 160424.png>)
![alt text](<Screenshot 2025-11-14 160521.png>)
![alt text](<Screenshot 2025-11-14 160613.png>)
![alt text](<Screenshot 2025-11-14 160629.png>)
![alt text](<Screenshot 2025-11-14 160657.png>)
![alt text](<Screenshot 2025-11-14 160716.png>)
![alt text](<Screenshot 2025-11-14 160745.png>)
![alt text](<Screenshot 2025-11-14 160815.png>)
![alt text](<Screenshot 2025-11-14 160832.png>)
![alt text](<Screenshot 2025-11-14 160901.png>)
![alt text](<Screenshot 2025-11-14 160919.png>)
![alt text](<Screenshot 2025-11-14 160946.png>)
![alt text](<Screenshot 2025-11-14 160957.png>)
![alt text](<Screenshot 2025-11-14 161011.png>)