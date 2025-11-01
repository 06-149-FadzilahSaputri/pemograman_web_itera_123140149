import React, { useState } from 'react';
import { useBooks } from '../../context/BookContext';
import BookForm from '../../components/BookForm/BookForm';
import BookList from '../../components/BookList/BookList';
import BookFilter from '../../components/BookFilter/BookFilter';

const Home = () => {
  const { filteredBooks, deleteBook } = useBooks();
  const [showForm, setShowForm] = useState(false);
  const [editingBook, setEditingBook] = useState(null);

  const handleAddBook = () => {
    setEditingBook(null);
    setShowForm(true);
  };

  const handleEditBook = (book) => {
    setEditingBook(book);
    setShowForm(true);
  };

  const handleDeleteBook = (id) => {
    if (window.confirm('Apakah Anda yakin ingin menghapus buku ini?')) {
      deleteBook(id);
    }
  };

  const handleCloseForm = () => {
    setShowForm(false);
    setEditingBook(null);
  };

  return (
    <div className="home">
      <div className="home-header">
        <h1>Koleksi Buku Saya</h1>
        <button onClick={handleAddBook} className="btn-add-book">
          + Tambah Buku
        </button>
      </div>

      <BookFilter />

      <div className="book-count">
        Menampilkan {filteredBooks.length} buku
      </div>

      <BookList 
        books={filteredBooks}
        onEdit={handleEditBook}
        onDelete={handleDeleteBook}
      />

      {showForm && (
        <BookForm 
          bookToEdit={editingBook}
          onClose={handleCloseForm}
        />
      )}
    </div>
  );
};

export default Home;