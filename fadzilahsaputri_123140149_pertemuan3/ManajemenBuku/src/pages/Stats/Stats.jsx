import React from 'react';
import { useBookStats } from '../../hooks/useBookStats';

const Stats = () => {
  const stats = useBookStats();

  const statCards = [
    {
      label: 'Total Buku',
      value: stats.total,
      color: '#9C27B0'
    },
    {
      label: 'Dimiliki',
      value: stats.owned,
      percentage: stats.percentageOwned,
      color: '#4CAF50'
    },
    {
      label: 'Sedang Dibaca',
      value: stats.reading,
      percentage: stats.percentageReading,
      color: '#2196F3'
    },
    {
      label: 'Ingin Dibeli',
      value: stats.wantToBuy,
      percentage: stats.percentageWantToBuy,
      color: '#FF9800'
    }
  ];

  return (
    <div className="stats">
      <h1>Statistik Koleksi Buku</h1>
      
      <div className="stats-grid">
        {statCards.map((card, index) => (
          <div key={index} className="stat-card" style={{ borderColor: card.color }}>
            <div className="stat-header">
              <h3>{card.label}</h3>
              <div 
                className="stat-icon" 
                style={{ backgroundColor: card.color }}
              >
                📚
              </div>
            </div>
            <div className="stat-value">{card.value}</div>
            {card.percentage !== undefined && (
              <div className="stat-percentage">
                {card.percentage}% dari total
              </div>
            )}
          </div>
        ))}
      </div>

      {stats.total === 0 && (
        <div className="empty-stats">
          <p>Belum ada buku dalam koleksi</p>
          <p>Mulai tambahkan buku untuk melihat statistik</p>
        </div>
      )}
    </div>
  );
};

export default Stats;