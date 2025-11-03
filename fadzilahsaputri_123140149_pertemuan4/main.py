"""
Program Pengelolaan Data Nilai Mahasiswa
Aplikasi untuk mengelola data dan nilai mahasiswa dengan fitur lengkap
"""

data_mahasiswa = [
    {"nama": "Ahmad Rizki", "nim": "2101001", "nilai_uts": 85, "nilai_uas": 88, "nilai_tugas": 90},
    {"nama": "Siti Nurhaliza", "nim": "2101002", "nilai_uts": 78, "nilai_uas": 82, "nilai_tugas": 85},
    {"nama": "Budi Santoso", "nim": "2101003", "nilai_uts": 65, "nilai_uas": 70, "nilai_tugas": 68},
    {"nama": "Dewi Lestari", "nim": "2101004", "nilai_uts": 92, "nilai_uas": 95, "nilai_tugas": 93},
    {"nama": "Eko Prasetyo", "nim": "2101005", "nilai_uts": 55, "nilai_uas": 60, "nilai_tugas": 58}
]


def hitung_nilai_akhir(nilai_uts, nilai_uas, nilai_tugas):
    """
    Menghitung nilai akhir berdasarkan presentase penilaian:
    30% UTS + 40% UAS + 30% Tugas
    """
    nilai_akhir = (nilai_uts * 0.3) + (nilai_uas * 0.4) + (nilai_tugas * 0.3)
    return round(nilai_akhir, 2)


def tentukan_grade(nilai_akhir):
    """
    Menentukan grade berdasarkan nilai akhir:
    A: ≥80, B: ≥70, C: ≥60, D: ≥50, E: <50
    """
    if nilai_akhir >= 80:
        return 'A'
    elif nilai_akhir >= 70:
        return 'B'
    elif nilai_akhir >= 60:
        return 'C'
    elif nilai_akhir >= 50:
        return 'D'
    else:
        return 'E'


def tampilkan_data_tabel(data):
    """
    Menampilkan data mahasiswa dalam format tabel
    """
    if not data:
        print("\nTidak ada data untuk ditampilkan.")
        return
    
    print("\n" + "="*100)
    print(f"{'No':<5} {'Nama':<20} {'NIM':<10} {'UTS':<6} {'UAS':<6} {'Tugas':<6} {'N.Akhir':<8} {'Grade':<6}")
    print("="*100)
    
    for i, mhs in enumerate(data, 1):
        nilai_akhir = hitung_nilai_akhir(mhs['nilai_uts'], mhs['nilai_uas'], mhs['nilai_tugas'])
        grade = tentukan_grade(nilai_akhir)
        
        print(f"{i:<5} {mhs['nama']:<20} {mhs['nim']:<10} {mhs['nilai_uts']:<6} "
              f"{mhs['nilai_uas']:<6} {mhs['nilai_tugas']:<6} {nilai_akhir:<8} {grade:<6}")
    
    print("="*100)


def cari_mahasiswa_tertinggi(data):
    """
    Mencari mahasiswa dengan nilai akhir tertinggi
    """
    if not data:
        return None
    
    mhs_tertinggi = data[0]
    nilai_tertinggi = hitung_nilai_akhir(mhs_tertinggi['nilai_uts'], 
                                         mhs_tertinggi['nilai_uas'], 
                                         mhs_tertinggi['nilai_tugas'])
    
    for mhs in data[1:]:
        nilai_akhir = hitung_nilai_akhir(mhs['nilai_uts'], mhs['nilai_uas'], mhs['nilai_tugas'])
        if nilai_akhir > nilai_tertinggi:
            nilai_tertinggi = nilai_akhir
            mhs_tertinggi = mhs
    
    return mhs_tertinggi, nilai_tertinggi


def cari_mahasiswa_terendah(data):
    """
    Mencari mahasiswa dengan nilai akhir terendah
    """
    if not data:
        return None
    
    mhs_terendah = data[0]
    nilai_terendah = hitung_nilai_akhir(mhs_terendah['nilai_uts'], 
                                        mhs_terendah['nilai_uas'], 
                                        mhs_terendah['nilai_tugas'])
    
    for mhs in data[1:]:
        nilai_akhir = hitung_nilai_akhir(mhs['nilai_uts'], mhs['nilai_uas'], mhs['nilai_tugas'])
        if nilai_akhir < nilai_terendah:
            nilai_terendah = nilai_akhir
            mhs_terendah = mhs
    
    return mhs_terendah, nilai_terendah


def tambah_mahasiswa_baru(data):
    """
    Menambahkan data mahasiswa baru ke dalam list
    """
    print("\n--- Input Data Mahasiswa Baru ---")
    
    try:
        nama = input("Nama Mahasiswa: ").strip()
        nim = input("NIM: ").strip()
        nilai_uts = float(input("Nilai UTS (0-100): "))
        nilai_uas = float(input("Nilai UAS (0-100): "))
        nilai_tugas = float(input("Nilai Tugas (0-100): "))
        
        if not (0 <= nilai_uts <= 100 and 0 <= nilai_uas <= 100 and 0 <= nilai_tugas <= 100):
            print("Error: Nilai harus berada di rentang 0-100!")
            return False
        
        mahasiswa_baru = {
            "nama": nama,
            "nim": nim,
            "nilai_uts": nilai_uts,
            "nilai_uas": nilai_uas,
            "nilai_tugas": nilai_tugas
        }
        
        data.append(mahasiswa_baru)
        print(f"\nData mahasiswa {nama} berhasil ditambahkan!")
        return True
        
    except ValueError:
        print("Error: Input nilai tidak valid!")
        return False


def filter_berdasarkan_grade(data, grade_target):
    """
    Filter mahasiswa berdasarkan grade tertentu
    """
    hasil_filter = []
    
    for mhs in data:
        nilai_akhir = hitung_nilai_akhir(mhs['nilai_uts'], mhs['nilai_uas'], mhs['nilai_tugas'])
        grade = tentukan_grade(nilai_akhir)
        
        if grade == grade_target.upper():
            hasil_filter.append(mhs)
    
    return hasil_filter


def hitung_rata_rata_kelas(data):
    """
    Menghitung rata-rata nilai akhir kelas
    """
    if not data:
        return 0
    
    total_nilai = 0
    for mhs in data:
        nilai_akhir = hitung_nilai_akhir(mhs['nilai_uts'], mhs['nilai_uas'], mhs['nilai_tugas'])
        total_nilai += nilai_akhir
    
    rata_rata = total_nilai / len(data)
    return round(rata_rata, 2)


def tampilkan_statistik(data):
    """
    Menampilkan statistik lengkap kelas
    """
    print("\n" + "="*60)
    print("STATISTIK KELAS")
    print("="*60)
    
    print(f"Jumlah Mahasiswa: {len(data)}")
    
    rata_rata = hitung_rata_rata_kelas(data)
    print(f"Rata-rata Nilai Kelas: {rata_rata}")
    
    mhs_tertinggi, nilai_tertinggi = cari_mahasiswa_tertinggi(data)
    print(f"\nNilai Tertinggi: {nilai_tertinggi}")
    print(f"  - Nama: {mhs_tertinggi['nama']}")
    print(f"  - NIM: {mhs_tertinggi['nim']}")
    print(f"  - Grade: {tentukan_grade(nilai_tertinggi)}")
    
    mhs_terendah, nilai_terendah = cari_mahasiswa_terendah(data)
    print(f"\nNilai Terendah: {nilai_terendah}")
    print(f"  - Nama: {mhs_terendah['nama']}")
    print(f"  - NIM: {mhs_terendah['nim']}")
    print(f"  - Grade: {tentukan_grade(nilai_terendah)}")
    
    print("\nDistribusi Grade:")
    for grade in ['A', 'B', 'C', 'D', 'E']:
        jumlah = len(filter_berdasarkan_grade(data, grade))
        print(f"  Grade {grade}: {jumlah} mahasiswa")
    
    print("="*60)


def menu_utama():
    """
    Menu utama program
    """
    while True:
        print("\n" + "="*60)
        print("PROGRAM PENGELOLAAN DATA NILAI MAHASISWA")
        print("="*60)
        print("1. Tampilkan Semua Data Mahasiswa")
        print("2. Tambah Data Mahasiswa Baru")
        print("3. Cari Mahasiswa Nilai Tertinggi")
        print("4. Cari Mahasiswa Nilai Terendah")
        print("5. Filter Mahasiswa Berdasarkan Grade")
        print("6. Tampilkan Statistik Kelas")
        print("7. Hitung Rata-rata Nilai Kelas")
        print("0. Keluar")
        print("="*60)
        
        pilihan = input("Pilih menu (0-7): ").strip()
        
        if pilihan == '1':
            tampilkan_data_tabel(data_mahasiswa)
            
        elif pilihan == '2':
            tambah_mahasiswa_baru(data_mahasiswa)
            
        elif pilihan == '3':
            if data_mahasiswa:
                mhs, nilai = cari_mahasiswa_tertinggi(data_mahasiswa)
                print(f"\nMahasiswa dengan nilai tertinggi:")
                print(f"Nama: {mhs['nama']}")
                print(f"NIM: {mhs['nim']}")
                print(f"Nilai Akhir: {nilai}")
                print(f"Grade: {tentukan_grade(nilai)}")
            else:
                print("\nTidak ada data mahasiswa.")
                
        elif pilihan == '4':
            if data_mahasiswa:
                mhs, nilai = cari_mahasiswa_terendah(data_mahasiswa)
                print(f"\nMahasiswa dengan nilai terendah:")
                print(f"Nama: {mhs['nama']}")
                print(f"NIM: {mhs['nim']}")
                print(f"Nilai Akhir: {nilai}")
                print(f"Grade: {tentukan_grade(nilai)}")
            else:
                print("\nTidak ada data mahasiswa.")
                
        elif pilihan == '5':
            grade = input("Masukkan grade yang ingin difilter (A/B/C/D/E): ").strip().upper()
            if grade in ['A', 'B', 'C', 'D', 'E']:
                hasil = filter_berdasarkan_grade(data_mahasiswa, grade)
                print(f"\nMahasiswa dengan grade {grade}:")
                tampilkan_data_tabel(hasil)
            else:
                print("Grade tidak valid!")
                
        elif pilihan == '6':
            tampilkan_statistik(data_mahasiswa)
            
        elif pilihan == '7':
            rata_rata = hitung_rata_rata_kelas(data_mahasiswa)
            print(f"\nRata-rata nilai kelas: {rata_rata}")
            
        elif pilihan == '0':
            print("\nTerima kasih telah menggunakan program ini!")
            break
            
        else:
            print("\nPilihan tidak valid! Silakan pilih menu 0-7.")

if __name__ == "__main__":
    menu_utama()