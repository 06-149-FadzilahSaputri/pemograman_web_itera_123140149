import { useMemo } from 'react';
import { useBooks } from '../context/BookContext';

export const useBookStats = () => {
  const { books } = useBooks();

  const stats = useMemo(() => {
    const total = books.length;
    const owned = books.filter(book => book.status === 'milik').length;
    const reading = books.filter(book => book.status === 'baca').length;
    const wantToBuy = books.filter(book => book.status === 'beli').length;

    return {
      total,
      owned,
      reading,
      wantToBuy,
      percentageOwned: total > 0 ? Math.round((owned / total) * 100) : 0,
      percentageReading: total > 0 ? Math.round((reading / total) * 100) : 0,
      percentageWantToBuy: total > 0 ? Math.round((wantToBuy / total) * 100) : 0
    };
  }, [books]);

  return stats;
};