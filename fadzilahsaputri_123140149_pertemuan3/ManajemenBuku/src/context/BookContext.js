import React, { createContext, useContext } from 'react';
import { useLocalStorage } from '../hooks/useLocalStorage.js';

const BookContext = createContext();

export const BookProvider = ({ children }) => {
  const [books, setBooks] = useLocalStorage('books', []);
  const [filter, setFilter] = React.useState('all');
  const [search, setSearch] = React.useState('');

  const addBook = (book) => {
    const newBook = {
      ...book,
      id: Date.now().toString(),
      createdAt: new Date().toISOString()
    };
    setBooks([...books, newBook]);
  };

  const updateBook = (id, updatedBook) => {
    setBooks(books.map(book => 
      book.id === id ? { ...book, ...updatedBook } : book
    ));
  };

  const deleteBook = (id) => {
    setBooks(books.filter(book => book.id !== id));
  };

  const filteredBooks = books.filter(book => {
    const matchesFilter = filter === 'all' || book.status === filter;
    const matchesSearch = book.title.toLowerCase().includes(search.toLowerCase()) ||
                         book.author.toLowerCase().includes(search.toLowerCase());
    return matchesFilter && matchesSearch;
  });

  const value = {
    books,
    filteredBooks,
    filter,
    search,
    setFilter,
    setSearch,
    addBook,
    updateBook,
    deleteBook
  };

  return (
    <BookContext.Provider value={value}>
      {children}
    </BookContext.Provider>
  );
};

export const useBooks = () => {
  const context = useContext(BookContext);
  if (!context) {
    throw new Error('useBooks must be used within a BookProvider');
  }
  return context;
};