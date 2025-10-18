// Ambil elemen-elemen DOM
const taskForm = document.getElementById('task-form');
const taskList = document.getElementById('task-list');
const pendingCountSpan = document.getElementById('pending-count');
const filterStatus = document.getElementById('filter-status');
const filterCourse = document.getElementById('filter-course');

// Inisialisasi array tugas dari localStorage atau array kosong
let tasks = JSON.parse(localStorage.getItem('tasks')) || [];

// Fungsi untuk menyimpan tasks ke localStorage
const saveTasks = () => {
    localStorage.setItem('tasks', JSON.stringify(tasks));
    updatePendingCount(); // Perbarui jumlah tugas yang belum selesai setiap kali data berubah
};

// Fungsi untuk memperbarui jumlah tugas yang belum selesai
const updatePendingCount = () => {
    const pendingTasks = tasks.filter(task => !task.completed);
    pendingCountSpan.textContent = pendingTasks.length;
};

// Fungsi untuk membuat ID unik
const generateId = () => {
    return Date.now().toString(36) + Math.random().toString(36).substr(2);
};

const renderTasks = () => {
    // Kosongkan daftar tugas yang ada
    taskList.innerHTML = '';

    // Ambil nilai filter
    const statusFilter = filterStatus.value;
    const courseFilter = filterCourse.value.toLowerCase().trim();

    // Terapkan filter
    const filteredTasks = tasks.filter(task => {
        const isStatusMatch = statusFilter === 'all' || 
                              (statusFilter === 'completed' && task.completed) ||
                              (statusFilter === 'pending' && !task.completed);
        
        const isCourseMatch = !courseFilter || 
                              (task.course && task.course.toLowerCase().includes(courseFilter));
        
        return isStatusMatch && isCourseMatch;
    });

    // Tampilkan tugas yang sudah difilter
    filteredTasks.forEach(task => {
        const listItem = document.createElement('li');
        listItem.className = task.completed ? 'completed' : '';
        listItem.dataset.id = task.id;

        // Tampilan informasi tugas
        listItem.innerHTML = `
            <div>
                <strong>${task.name}</strong> 
                <p>Matkul: ${task.course || '-'} | Deadline: ${task.deadline}</p>
            </div>
            <div class="task-actions">
                <button onclick="toggleComplete('${task.id}')">
                    ${task.completed ? 'Batal Selesai' : 'Selesaikan'}
                </button>
                <button onclick="deleteTask('${task.id}')">Hapus</button>
            </div>
        `;

        taskList.appendChild(listItem);
    });

    updatePendingCount(); // Perbarui hitungan setelah render
};

taskForm.addEventListener('submit', (e) => {
    e.preventDefault();

    const nameInput = document.getElementById('task-name');
    const courseInput = document.getElementById('task-course');
    const deadlineInput = document.getElementById('task-deadline');

    const name = nameInput.value.trim();
    const course = courseInput.value.trim();
    const deadline = deadlineInput.value;

    // --- Validasi Form ---
    if (name === "") {
        alert("Nama tugas tidak boleh kosong.");
        return;
    }

    const today = new Date().toISOString().split('T')[0];
    if (deadline < today) {
        alert("Deadline tidak valid. Tidak bisa memilih tanggal di masa lalu.");
        return;
    }
    // -----------------------

    const newTask = {
        id: generateId(), // Gunakan ID unik
        name: name,
        course: course,
        deadline: deadline,
        completed: false
    };

    tasks.push(newTask);
    saveTasks(); // Simpan ke localStorage
    renderTasks(); // Render ulang daftar tugas

    // Reset Form
    taskForm.reset();
});

// --- Menandai Tugas Selesai/Belum Selesai ---
window.toggleComplete = (id) => {
    const taskIndex = tasks.findIndex(task => task.id === id);
    if (taskIndex > -1) {
        tasks[taskIndex].completed = !tasks[taskIndex].completed;
        saveTasks();
        renderTasks();
    }
};

// --- Menghapus Tugas ---
window.deleteTask = (id) => {
    // Konfirmasi sebelum menghapus
    if (confirm("Apakah Anda yakin ingin menghapus tugas ini?")) {
        tasks = tasks.filter(task => task.id !== id);
        saveTasks();
        renderTasks();
    }
};

// Event listener untuk filter status
filterStatus.addEventListener('change', renderTasks);

// Event listener untuk filter/pencarian mata kuliah
filterCourse.addEventListener('input', renderTasks);

// --- Pemuatan Data saat Halaman Dibuka ---
// Panggil renderTasks untuk memuat data dari localStorage saat halaman pertama kali dibuka
document.addEventListener('DOMContentLoaded', renderTasks);