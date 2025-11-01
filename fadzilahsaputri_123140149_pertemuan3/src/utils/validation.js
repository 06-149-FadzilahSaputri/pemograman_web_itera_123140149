export const validateBook = (book) => {
  const errors = {};

  if (!book.title.trim()) {
    errors.title = 'Judul buku wajib diisi';
  } else if (book.title.length < 2) {
    errors.title = 'Judul buku minimal 2 karakter';
  }

  if (!book.author.trim()) {
    errors.author = 'Penulis wajib diisi';
  } else if (book.author.length < 2) {
    errors.author = 'Nama penulis minimal 2 karakter';
  }

  if (!book.status) {
    errors.status = 'Status buku wajib dipilih';
  }

  return {
    isValid: Object.keys(errors).length === 0,
    errors
  };
};