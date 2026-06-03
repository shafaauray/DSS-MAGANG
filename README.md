# 🎓 Sistem Pendukung Keputusan Pemilihan Tempat Magang Menggunakan Metode SAW

## 📖 Deskripsi Project

Sistem Pendukung Keputusan (SPK) Pemilihan Tempat Magang merupakan aplikasi berbasis web yang dirancang untuk membantu mahasiswa menentukan tempat magang terbaik berdasarkan beberapa kriteria penilaian.

Pada praktiknya, mahasiswa sering dihadapkan pada banyak pilihan perusahaan magang dengan karakteristik yang berbeda-beda. Oleh karena itu, diperlukan suatu metode yang dapat membantu proses pengambilan keputusan secara objektif dan terukur.

Aplikasi ini menerapkan metode **Simple Additive Weighting (SAW)** untuk melakukan proses perankingan alternatif perusahaan berdasarkan bobot dan nilai kriteria yang diberikan oleh pengguna.

---

## 🎯 Tujuan Sistem

Tujuan utama dari sistem ini adalah:

- Membantu mahasiswa memilih tempat magang yang paling sesuai.
- Mengurangi subjektivitas dalam proses pemilihan tempat magang.
- Memberikan hasil perankingan berdasarkan metode pengambilan keputusan multikriteria.
- Menyediakan visualisasi hasil perhitungan yang mudah dipahami.

---

## 🧮 Metode yang Digunakan

### Simple Additive Weighting (SAW)

Metode SAW merupakan salah satu metode dalam Sistem Pendukung Keputusan (SPK) yang bekerja dengan cara:

1. Menentukan alternatif yang akan dibandingkan.
2. Menentukan kriteria penilaian.
3. Memberikan bobot pada setiap kriteria.
4. Melakukan normalisasi matriks keputusan.
5. Menghitung nilai preferensi setiap alternatif.
6. Menghasilkan ranking alternatif terbaik.

### Rumus Normalisasi

#### Benefit Criteria

Kriteria yang semakin besar nilainya semakin baik.

\[
R_{ij} = \frac{X_{ij}}{Max(X_{ij})}
\]

#### Cost Criteria

Kriteria yang semakin kecil nilainya semakin baik.

\[
R_{ij} = \frac{Min(X_{ij})}{X_{ij}}
\]

### Rumus Nilai Preferensi

\[
V_i = \sum_{j=1}^{n} W_j \times R_{ij}
\]

Keterangan:

- \(V_i\) = Nilai akhir alternatif
- \(W_j\) = Bobot kriteria
- \(R_{ij}\) = Nilai normalisasi

Alternatif dengan nilai tertinggi akan menempati peringkat pertama.

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

### Manajemen Data Perusahaan

- Menambahkan data perusahaan magang
- Mengubah data perusahaan
- Menghapus data perusahaan
- Menampilkan seluruh alternatif perusahaan

### Pengaturan Bobot

- Mengatur bobot setiap kriteria
- Validasi total bobot harus 100%

### Perhitungan SAW

- Normalisasi otomatis
- Perhitungan nilai preferensi
- Perankingan alternatif secara otomatis

### Visualisasi Data

- Dashboard informasi
- Tabel hasil ranking
- Grafik ranking perusahaan
- Tampilan podium 3 besar

### Export Data

- Download hasil ranking dalam format CSV

---

## 🖥️ Teknologi yang Digunakan

| Teknologi | Fungsi |
|------------|---------|
| Python | Bahasa Pemrograman |
| Streamlit | Framework Web App |
| Pandas | Pengolahan Data |
| NumPy | Perhitungan Numerik |
| Git & GitHub | Version Control |

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

### Penjelasan File

#### app.py

Berisi antarmuka aplikasi (UI) menggunakan Streamlit, meliputi:

- Dashboard
- Input data perusahaan
- Input bobot kriteria
- Visualisasi hasil
- Export data

#### saw.py

Berisi implementasi metode SAW:

- Normalisasi Benefit
- Normalisasi Cost
- Perhitungan skor akhir
- Proses ranking

#### requirements.txt

Daftar dependency yang diperlukan aplikasi.

---

## 🌐 Demo Aplikasi

Aplikasi dapat diakses secara online melalui:

👉 https://dss-magang-2nmiwypfhmev2amabhndqf.streamlit.app/

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

Mac/Linux

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

## 📊 Alur Sistem

1. Pengguna memasukkan data perusahaan.
2. Pengguna menentukan bobot kriteria.
3. Sistem melakukan normalisasi data.
4. Sistem menghitung nilai preferensi menggunakan metode SAW.
5. Sistem menampilkan hasil ranking.
6. Pengguna dapat mengunduh hasil ranking dalam format CSV.

---

## 👥 Kelompok 5

### Mata Kuliah
Sistem Pendukung Keputusan (SPK)

### Judul Project
**Sistem Pendukung Keputusan Pemilihan Tempat Magang Menggunakan Metode SAW**

---

## 📄 Lisensi

Project ini dibuat untuk keperluan akademik dan pembelajaran pada mata kuliah Sistem Pendukung Keputusan.
