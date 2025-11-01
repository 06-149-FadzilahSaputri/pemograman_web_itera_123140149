import React from 'react';

const BookItem = ({ book, onEdit, onDelete }) => {
  const getStatusColor = (status) => {
    switch (status) {
      case 'milik':
        return '#4CAF50';
      case 'baca':
        return '#2196F3';
      case 'beli':
        return '#FF9800';
      default:
        return '#9E9E9E';
    }
  };

  const getStatusText = (status) => {
    switch (status) {
      case 'milik':
        return 'Dimiliki';
      case 'baca':
        return 'Sedang Dibaca';
      case 'beli':
        return 'Ingin Dibeli';
      default:
        return status;
    }
  };

  return (
    <div className="book-item">
      <div className="book-info">
        <h3 className="book-title">{book.title}</h3>
        <p className="book-author">oleh {book.author}</p>
        <span 
          className="book-status"
          style={{ backgroundColor: getStatusColor(book.status) }}
        >
          {getStatusText(book.status)}
        </span>
      </div>
      <div className="book-actions">
        <button 
          onClick={() => onEdit(book)}
          className="btn-edit"
          aria-label="Edit buku"
        >
          ✏️
        </button>
        <button 
          onClick={() => onDelete(book.id)}
          className="btn-delete"
          aria-label="Hapus buku"
        >
          🗑️
        </button>
      </div>
    </div>
  );
};

export default BookItem;