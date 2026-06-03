# 🎓 Sistem Pendukung Keputusan Pemilihan Tempat Magang Menggunakan Metode SAW

![Python](https://img.shields.io/badge/Python-3.14-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-Web%20App-red)
![Method](https://img.shields.io/badge/Method-SAW-green)
![Status](https://img.shields.io/badge/Status-Deployed-success)

---

## 📖 Deskripsi Project

Sistem Pendukung Keputusan (SPK) Pemilihan Tempat Magang merupakan aplikasi berbasis web yang dirancang untuk membantu mahasiswa menentukan tempat magang terbaik berdasarkan beberapa kriteria penilaian.

Dalam proses mencari tempat magang, mahasiswa sering dihadapkan pada banyak pilihan perusahaan dengan kelebihan dan kekurangan masing-masing. Oleh karena itu diperlukan sebuah sistem yang mampu membantu proses pengambilan keputusan secara objektif, cepat, dan terukur.

Aplikasi ini menerapkan metode **Simple Additive Weighting (SAW)** untuk melakukan proses normalisasi, pembobotan, dan perankingan alternatif perusahaan sehingga pengguna dapat memperoleh rekomendasi tempat magang terbaik berdasarkan preferensi yang diberikan.

---

## 🌐 Live Demo

Aplikasi dapat diakses secara online melalui:

### 🔗 https://dss-magang-2nmiwypfhmev2amabhndqf.streamlit.app/

---

## 🎯 Tujuan Sistem

Sistem ini dibuat untuk:

- Membantu mahasiswa memilih tempat magang terbaik.
- Mengurangi subjektivitas dalam pengambilan keputusan.
- Memberikan hasil perankingan yang objektif berdasarkan kriteria tertentu.
- Menerapkan metode SAW pada kasus nyata pemilihan tempat magang.
- Menyediakan visualisasi hasil perhitungan yang mudah dipahami.

---

## 🧮 Metode Simple Additive Weighting (SAW)

Metode SAW merupakan salah satu metode dalam Sistem Pendukung Keputusan yang digunakan untuk menentukan alternatif terbaik dari sejumlah alternatif berdasarkan beberapa kriteria.

Tahapan metode SAW:

1. Menentukan alternatif.
2. Menentukan kriteria.
3. Memberikan bobot pada setiap kriteria.
4. Melakukan normalisasi matriks keputusan.
5. Menghitung nilai preferensi.
6. Melakukan proses perankingan.

---

## 📊 Rumus Normalisasi

### Benefit Criteria

Kriteria yang semakin besar nilainya semakin baik.

```text
Rij = Xij / Max(Xij)
```

### Cost Criteria

Kriteria yang semakin kecil nilainya semakin baik.

```text
Rij = Min(Xij) / Xij
```

---

## 📈 Rumus Nilai Preferensi

```text
Vi = Σ(Wj × Rij)
```

Keterangan:

| Simbol | Keterangan |
|---------|---------|
| Vi | Nilai akhir alternatif |
| Wj | Bobot kriteria |
| Rij | Nilai normalisasi |
| Xij | Nilai alternatif |

Alternatif dengan nilai preferensi tertinggi akan menempati peringkat pertama.

---

## 📋 Kriteria Penilaian

| Kode | Kriteria | Jenis |
|--------|--------|--------|
| C1 | Kesesuaian Bidang | Benefit |
| C2 | Jarak | Cost |
| C3 | Uang Saku | Benefit |
| C4 | Reputasi Perusahaan | Benefit |
| C5 | Fasilitas | Benefit |
| C6 | Peluang Direkrut | Benefit |

---

## 🚀 Fitur Sistem

### 📌 Manajemen Data Perusahaan

- Menambahkan data perusahaan magang
- Mengubah data perusahaan
- Menghapus data perusahaan
- Menampilkan seluruh alternatif perusahaan

### ⚖️ Pengaturan Bobot Kriteria

- Input bobot masing-masing kriteria
- Validasi total bobot harus 100%

### 🏆 Perhitungan Metode SAW

- Normalisasi otomatis
- Perhitungan nilai preferensi
- Perankingan alternatif perusahaan

### 📊 Visualisasi Hasil

- Dashboard informasi
- Tabel ranking perusahaan
- Grafik hasil ranking
- Podium 3 besar perusahaan terbaik

### 📥 Export Data

- Download hasil ranking dalam format CSV

---

## 🖥️ Teknologi yang Digunakan

| Teknologi | Kegunaan |
|------------|------------|
| Python | Bahasa Pemrograman |
| Streamlit | Framework Web Application |
| Pandas | Pengolahan Data |
| NumPy | Perhitungan Numerik |
| Git | Version Control |
| GitHub | Repository Management |

---

## 📂 Struktur Project

```text
DSS-MAGANG
│
├── app.py
├── saw.py
├── data.csv
├── requirements.txt
└── README.md
```

---

## 📄 Penjelasan File

### app.py

File utama aplikasi Streamlit yang berisi:

- Dashboard
- Input data perusahaan
- Input bobot kriteria
- Perhitungan ranking
- Visualisasi hasil
- Export CSV

### saw.py

Berisi implementasi metode SAW:

- Normalisasi Benefit
- Normalisasi Cost
- Perhitungan skor akhir
- Perankingan alternatif

### requirements.txt

Berisi daftar library yang dibutuhkan aplikasi.

---

## 🔄 Alur Kerja Sistem

1. Pengguna memasukkan data perusahaan.
2. Pengguna memberikan nilai setiap kriteria.
3. Pengguna menentukan bobot kriteria.
4. Sistem melakukan normalisasi data.
5. Sistem menghitung nilai preferensi menggunakan metode SAW.
6. Sistem menghasilkan ranking perusahaan.
7. Sistem menampilkan visualisasi grafik.
8. Pengguna dapat mengunduh hasil ranking.

---

## ⚙️ Cara Menjalankan Secara Lokal

### Clone Repository

```bash
git clone https://github.com/shafaauray/DSS-MAGANG.git
```

### Masuk ke Folder Project

```bash
cd DSS-MAGANG
```

### Membuat Virtual Environment

```bash
python3 -m venv .venv
```

### Aktivasi Virtual Environment

MacOS / Linux

```bash
source .venv/bin/activate
```

Windows

```bash
.venv\Scripts\activate
```

### Install Dependency

```bash
pip install -r requirements.txt
```

### Menjalankan Aplikasi

```bash
streamlit run app.py
```

---

## 👥 Kelompok 5

### Mata Kuliah

Sistem Pendukung Keputusan (SPK)

### Judul Project

**Sistem Pendukung Keputusan Pemilihan Tempat Magang Menggunakan Metode SAW**

---

## 📚 Manfaat Project

Project ini diharapkan dapat membantu mahasiswa dalam menentukan tempat magang terbaik secara objektif berdasarkan berbagai kriteria yang relevan serta memberikan pengalaman implementasi metode Sistem Pendukung Keputusan menggunakan metode Simple Additive Weighting (SAW).

---

## 📄 Lisensi

Project ini dibuat untuk keperluan akademik dan pembelajaran pada mata kuliah Sistem Pendukung Keputusan.
