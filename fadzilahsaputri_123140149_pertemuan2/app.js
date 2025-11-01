// Kelas Note untuk mengelola objek catatan
class Note {
    constructor(id, content, pinned = false) {
        this.id = id;
        this.content = content;
        this.pinned = pinned;
        this.createdAt = new Date();
        this.updatedAt = new Date();
    }

    // Metode untuk mengubah status pin
    togglePin() {
        this.pinned = !this.pinned;
        this.updatedAt = new Date();
        return this.pinned;
    }

    // Metode untuk mengubah konten catatan
    updateContent(newContent) {
        this.content = newContent;
        this.updatedAt = new Date();
    }

    // Metode untuk memeriksa apakah catatan baru (dibuat dalam 24 jam terakhir)
    isRecent() {
        const now = new Date();
        const diffTime = Math.abs(now - this.createdAt);
        const diffDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24));
        return diffDays <= 1;
    }

    // Metode untuk format tanggal
    getFormattedDate() {
        const options = { 
            day: 'numeric', 
            month: 'short', 
            year: 'numeric',
            hour: '2-digit',
            minute: '2-digit'
        };
        return this.updatedAt.toLocaleDateString('id-ID', options);
    }
}

// Kelas NoteManager untuk mengelola semua catatan
class NoteManager {
    constructor() {
        this.notes = [];
        this.currentFilter = 'all';
        this.editingNoteId = null;
    }

    // Metode untuk menambah catatan baru
    addNote(content) {
        const newNote = new Note(Date.now(), content);
        this.notes.unshift(newNote); // Tambahkan di awal array
        return newNote;
    }

    // Metode untuk menghapus catatan
    deleteNote(id) {
        this.notes = this.notes.filter(note => note.id !== id);
    }

    // Metode untuk mendapatkan catatan berdasarkan ID
    getNote(id) {
        return this.notes.find(note => note.id === id);
    }

    // Metode untuk memperbarui catatan
    updateNote(id, newContent) {
        const note = this.getNote(id);
        if (note) {
            note.updateContent(newContent);
            return note;
        }
        return null;
    }

    // Metode untuk mengubah status pin
    toggleNotePin(id) {
        const note = this.getNote(id);
        if (note) {
            return note.togglePin();
        }
        return false;
    }

    // Metode untuk mendapatkan catatan berdasarkan filter
    getFilteredNotes() {
        switch (this.currentFilter) {
            case 'pinned':
                return this.notes.filter(note => note.pinned);
            case 'recent':
                return this.notes.filter(note => note.isRecent());
            default:
                return this.notes;
        }
    }

    // Metode untuk mengatur filter
    setFilter(filter) {
        this.currentFilter = filter;
    }

    // Metode untuk mendapatkan statistik catatan
    getStats() {
        const total = this.notes.length;
        const pinned = this.notes.filter(note => note.pinned).length;
        const recent = this.notes.filter(note => note.isRecent()).length;

        return { total, pinned, recent };
    }
}

// Inisialisasi aplikasi
const noteManager = new NoteManager();

// DOM Elements
const noteForm = document.getElementById('note-form');
const noteInput = document.getElementById('note-input');
const noteList = document.getElementById('note-list');
const emptyState = document.getElementById('empty-state');
const filterTabs = document.querySelectorAll('.filter-tab');
const editModal = document.getElementById('edit-modal');
const editNoteInput = document.getElementById('edit-note-input');
const closeModalBtn = document.getElementById('close-modal');
const cancelEditBtn = document.getElementById('cancel-edit');
const saveEditBtn = document.getElementById('save-edit');
const toastContainer = document.getElementById('toast-container');

// Arrow function untuk menyimpan data ke localStorage
const saveNotesToStorage = async () => {
    try {
        const notesData = JSON.stringify(noteManager.notes);
        localStorage.setItem('notes', notesData);
        return true;
    } catch (error) {
        console.error('Error saving notes:', error);
        showToast('Gagal menyimpan catatan', 'error');
        return false;
    }
};

// Arrow function untuk memuat data dari localStorage
const loadNotesFromStorage = async () => {
    try {
        const notesData = localStorage.getItem('notes');
        if (notesData) {
            const notes = JSON.parse(notesData);
            // Mengubah kembali objek JSON menjadi objek Note
            noteManager.notes = notes.map(note => {
                const newNote = new Note(note.id, note.content, note.pinned);
                newNote.createdAt = new Date(note.createdAt);
                newNote.updatedAt = new Date(note.updatedAt);
                return newNote;
            });
        }
        return true;
    } catch (error) {
        console.error('Error loading notes:', error);
        showToast('Gagal memuat catatan', 'error');
        return false;
    }
};

// Arrow function untuk menampilkan notifikasi toast
const showToast = (message, type = 'info') => {
    const toast = document.createElement('div');
    toast.className = `toast ${type}`;
    
    let icon = '';
    switch (type) {
        case 'success':
            icon = '<i class="bi bi-check-circle-fill" style="color: var(--success-color);"></i>';
            break;
        case 'error':
            icon = '<i class="bi bi-x-circle-fill" style="color: var(--danger-color);"></i>';
            break;
        default:
            icon = '<i class="bi bi-info-circle-fill" style="color: var(--primary-color);"></i>';
    }
    
    toast.innerHTML = `${icon} <span>${message}</span>`;
    toastContainer.appendChild(toast);
    
    // Menghapus toast setelah 3 detik
    setTimeout(() => {
        toast.style.animation = 'slideIn 0.3s ease reverse';
        setTimeout(() => {
            if (toastContainer.contains(toast)) {
                toastContainer.removeChild(toast);
            }
        }, 300);
    }, 3000);
};

// Arrow function untuk merender catatan
const renderNotes = () => {
    const filteredNotes = noteManager.getFilteredNotes();
    
    // Menggunakan template literals untuk rendering dinamis
    if (filteredNotes.length === 0) {
        noteList.innerHTML = '';
        emptyState.style.display = 'block';
    } else {
        emptyState.style.display = 'none';
        noteList.innerHTML = filteredNotes.map(note => `
            <li class="note-item ${note.pinned ? 'pinned' : ''}" data-id="${note.id}">
                <div class="note-content">${note.content}</div>
                <div class="note-meta">
                    <i class="bi bi-clock"></i> ${note.getFormattedDate()}
                    ${note.pinned ? '<i class="bi bi-pin-angle-fill" style="color: var(--warning-color); margin-left: 10px;"></i> Disematkan' : ''}
                </div>
                <div class="note-actions">
                    <button class="note-btn pin ${note.pinned ? 'pinned' : ''}" data-id="${note.id}" title="Sematkan">
                        <i class="bi bi-pin-angle"></i>
                    </button>
                    <button class="note-btn edit" data-id="${note.id}" title="Edit">
                        <i class="bi bi-pencil"></i>
                    </button>
                    <button class="note-btn delete" data-id="${note.id}" title="Hapus">
                        <i class="bi bi-trash"></i>
                    </button>
                </div>
            </li>
        `).join('');
    }
    
    updateStats();
    
    // Set up event listeners for the new buttons
    setupNoteButtonListeners();
};

// Arrow function untuk memperbarui statistik
const updateStats = () => {
    // Menggunakan destructuring untuk mendapatkan nilai dari objek statistik
    const { total, pinned, recent } = noteManager.getStats();
    document.getElementById('total-notes').textContent = total;
    document.getElementById('pinned-notes').textContent = pinned;
    document.getElementById('recent-notes').textContent = recent;
};

// Arrow function untuk setup event listeners pada tombol catatan
const setupNoteButtonListeners = () => {
    // Get all pin buttons
    const pinButtons = document.querySelectorAll('.note-btn.pin');
    pinButtons.forEach(button => {
        button.addEventListener('click', async (e) => {
            e.stopPropagation();
            const noteId = parseInt(button.dataset.id);
            const isPinned = noteManager.toggleNotePin(noteId);
            await saveNotesToStorage();
            renderNotes();
            showToast(isPinned ? 'Catatan disematkan' : 'Sematan catatan dilepas', 'success');
        });
    });
    
    // Get all edit buttons
    const editButtons = document.querySelectorAll('.note-btn.edit');
    editButtons.forEach(button => {
        button.addEventListener('click', async (e) => {
            e.stopPropagation();
            const noteId = parseInt(button.dataset.id);
            const note = noteManager.getNote(noteId);
            if (note) {
                noteManager.editingNoteId = noteId;
                editNoteInput.value = note.content;
                editModal.classList.add('active');
                editNoteInput.focus();
            }
        });
    });
    
    // Get all delete buttons
    const deleteButtons = document.querySelectorAll('.note-btn.delete');
    deleteButtons.forEach(button => {
        button.addEventListener('click', async (e) => {
            e.stopPropagation();
            const noteId = parseInt(button.dataset.id);
            noteManager.deleteNote(noteId);
            await saveNotesToStorage();
            renderNotes();
            showToast('Catatan berhasil dihapus', 'success');
        });
    });
};

// Event listener untuk form tambah catatan
noteForm.addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const noteContent = noteInput.value.trim();
    if (noteContent) {
        noteManager.addNote(noteContent);
        await saveNotesToStorage();
        renderNotes();
        noteInput.value = '';
        showToast('Catatan berhasil ditambahkan', 'success');
    }
});

// Event listener untuk filter tabs
filterTabs.forEach(tab => {
    tab.addEventListener('click', () => {
        // Menghapus kelas active dari semua tab
        filterTabs.forEach(t => t.classList.remove('active'));
        // Menambahkan kelas active ke tab yang diklik
        tab.classList.add('active');
        
        // Mengatur filter dan merender ulang catatan
        const filter = tab.dataset.filter;
        noteManager.setFilter(filter);
        renderNotes();
    });
});

// Event listener untuk modal edit
closeModalBtn.addEventListener('click', () => {
    editModal.classList.remove('active');
    noteManager.editingNoteId = null;
});

cancelEditBtn.addEventListener('click', () => {
    editModal.classList.remove('active');
    noteManager.editingNoteId = null;
});

saveEditBtn.addEventListener('click', async () => {
    const newContent = editNoteInput.value.trim();
    if (newContent && noteManager.editingNoteId) {
        noteManager.updateNote(noteManager.editingNoteId, newContent);
        await saveNotesToStorage();
        renderNotes();
        editModal.classList.remove('active');
        noteManager.editingNoteId = null;
        showToast('Catatan berhasil diperbarui', 'success');
    }
});

// Menutup modal dengan mengklik di luar modal
editModal.addEventListener('click', (e) => {
    if (e.target === editModal) {
        editModal.classList.remove('active');
        noteManager.editingNoteId = null;
    }
});

// Fungsi untuk membersihkan localStorage jika ada masalah
const clearCorruptedData = () => {
    try {
        const notesData = localStorage.getItem('notes');
        if (notesData) {
            const notes = JSON.parse(notesData);
            // Check if data is corrupted
            if (!Array.isArray(notes)) {
                localStorage.removeItem('notes');
                showToast('Data yang rusak telah dibersihkan', 'info');
                return true;
            }
        }
        return false;
    } catch (error) {
        localStorage.removeItem('notes');
        showToast('Data yang rusak telah dibersihkan', 'info');
        return true;
    }
};

// Fungsi asinkron untuk inisialisasi aplikasi
const initApp = async () => {
    try {
        // Clear corrupted data if needed
        clearCorruptedData();
        
        await loadNotesFromStorage();
        renderNotes();
        showToast('Aplikasi berhasil dimuat', 'success');
    } catch (error) {
        console.error('Error initializing app:', error);
        showToast('Gagal memuat aplikasi', 'error');
    }
};

// Memastikan DOM sudah dimuat sebelum menjalankan aplikasi
document.addEventListener('DOMContentLoaded', initApp);