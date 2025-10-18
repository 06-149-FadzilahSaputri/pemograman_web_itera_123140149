const taskForm = document.getElementById('task-form');
const taskList = document.getElementById('task-list');
const pendingCountSpan = document.getElementById('pending-count');
const filterStatus = document.getElementById('filter-status');
const filterCourse = document.getElementById('filter-course');

let tasks = JSON.parse(localStorage.getItem('tasks')) || [];

const saveTasks = () => {
    localStorage.setItem('tasks', JSON.stringify(tasks));
    updatePendingCount(); 
};

const updatePendingCount = () => {
    const pendingTasks = tasks.filter(task => !task.completed);
    pendingCountSpan.textContent = pendingTasks.length;
};

const generateId = () => {
    return Date.now().toString(36) + Math.random().toString(36).substr(2);
};

const renderTasks = () => {
    taskList.innerHTML = '';

    const statusFilter = filterStatus.value;
    const courseFilter = filterCourse.value.toLowerCase().trim();


    const filteredTasks = tasks.filter(task => {
        const isStatusMatch = statusFilter === 'all' || 
                              (statusFilter === 'completed' && task.completed) ||
                              (statusFilter === 'pending' && !task.completed);
        
        const isCourseMatch = !courseFilter || 
                              (task.course && task.course.toLowerCase().includes(courseFilter));
        
        return isStatusMatch && isCourseMatch;
    });

    filteredTasks.forEach(task => {
        const listItem = document.createElement('li');
        listItem.className = task.completed ? 'completed' : '';
        listItem.dataset.id = task.id;

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

    updatePendingCount();
};

taskForm.addEventListener('submit', (e) => {
    e.preventDefault();

    const nameInput = document.getElementById('task-name');
    const courseInput = document.getElementById('task-course');
    const deadlineInput = document.getElementById('task-deadline');

    const name = nameInput.value.trim();
    const course = courseInput.value.trim();
    const deadline = deadlineInput.value;

    if (name === "") {
        alert("Nama tugas tidak boleh kosong.");
        return;
    }

    const today = new Date().toISOString().split('T')[0];
    if (deadline < today) {
        alert("Deadline tidak valid. Tidak bisa memilih tanggal di masa lalu.");
        return;
    }


    const newTask = {
        id: generateId(), 
        name: name,
        course: course,
        deadline: deadline,
        completed: false
    };

    tasks.push(newTask);
    saveTasks(); 
    renderTasks(); 

    taskForm.reset();
});

window.toggleComplete = (id) => {
    const taskIndex = tasks.findIndex(task => task.id === id);
    if (taskIndex > -1) {
        tasks[taskIndex].completed = !tasks[taskIndex].completed;
        saveTasks();
        renderTasks();
    }
};

window.deleteTask = (id) => {
    if (confirm("Apakah Anda yakin ingin menghapus tugas ini?")) {
        tasks = tasks.filter(task => task.id !== id);
        saveTasks();
        renderTasks();
    }
};

filterStatus.addEventListener('change', renderTasks);

filterCourse.addEventListener('input', renderTasks);

document.addEventListener('DOMContentLoaded', renderTasks);