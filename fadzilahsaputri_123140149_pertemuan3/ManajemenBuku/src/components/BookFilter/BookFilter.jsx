import React from 'react';
import { useBooks } from '../../context/BookContext';
import './BookFilter.css';

const BookFilter = () => {
  const { filter, setFilter, search, setSearch } = useBooks();

  return (
    <div className="book-filter">
      <div className="filter-group">
        <label htmlFor="search">Cari Buku</label>
        <input
          type="text"
          id="search"
          value={search}
          onChange={(e) => setSearch(e.target.value)}
          placeholder="Cari berdasarkan judul atau penulis..."
        />
      </div>
      
      <div className="filter-group">
        <label htmlFor="status-filter">Filter Status</label>
        <select
          id="status-filter"
          value={filter}
          onChange={(e) => setFilter(e.target.value)}
        >
          <option value="all">Semua</option>
          <option value="milik">Dimiliki</option>
          <option value="baca">Sedang Dibaca</option>
          <option value="beli">Ingin Dibeli</option>
        </select>
      </div>
    </div>
  );
};

export default BookFilter;