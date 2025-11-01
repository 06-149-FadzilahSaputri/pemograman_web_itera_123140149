import React, { useState } from 'react';
import { useBooks } from '../../context/BookContext';
import { validateBook } from '../../utils/validation';
import './BookForm.css';

const BookForm = ({ bookToEdit, onClose }) => {
  const { addBook, updateBook } = useBooks();
  const [formData, setFormData] = useState({
    title: bookToEdit?.title || '',
    author: bookToEdit?.author || '',
    status: bookToEdit?.status || 'milik'
  });
  const [errors, setErrors] = useState({});

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData(prev => ({
      ...prev,
      [name]: value
    }));
    
    if (errors[name]) {
      setErrors(prev => ({
        ...prev,
        [name]: ''
      }));
    }
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    
    const validation = validateBook(formData);
    if (!validation.isValid) {
      setErrors(validation.errors);
      return;
    }

    if (bookToEdit) {
      updateBook(bookToEdit.id, formData);
    } else {
      addBook(formData);
    }
    
    onClose();
  };

  return (
    <div className="book-form-overlay">
      <div className="book-form">
        <h2>{bookToEdit ? 'Edit Buku' : 'Tambah Buku Baru'}</h2>
        <form onSubmit={handleSubmit}>
          <div className="form-group">
            <label htmlFor="title">Judul Buku</label>
            <input
              type="text"
              id="title"
              name="title"
              value={formData.title}
              onChange={handleChange}
              className={errors.title ? 'error' : ''}
              placeholder="Masukkan judul buku"
            />
            {errors.title && <span className="error-message">{errors.title}</span>}
          </div>

          <div className="form-group">
            <label htmlFor="author">Penulis</label>
            <input
              type="text"
              id="author"
              name="author"
              value={formData.author}
              onChange={handleChange}
              className={errors.author ? 'error' : ''}
              placeholder="Masukkan nama penulis"
            />
            {errors.author && <span className="error-message">{errors.author}</span>}
          </div>

          <div className="form-group">
            <label htmlFor="status">Status</label>
            <select
              id="status"
              name="status"
              value={formData.status}
              onChange={handleChange}
              className={errors.status ? 'error' : ''}
            >
              <option value="">Pilih Status</option>
              <option value="milik">Dimiliki</option>
              <option value="baca">Sedang Dibaca</option>
              <option value="beli">Ingin Dibeli</option>
            </select>
            {errors.status && <span className="error-message">{errors.status}</span>}
          </div>

          <div className="form-actions">
            <button type="button" onClick={onClose} className="btn-cancel">
              Batal
            </button>
            <button type="submit" className="btn-submit">
              {bookToEdit ? 'Update' : 'Tambah'}
            </button>
          </div>
        </form>
      </div>
    </div>
  );
};

export default BookForm;