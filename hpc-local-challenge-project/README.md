# Bridging Global Infrastructure to Address Local Challenges with HPC

Repository ini berisi implementasi studi kasus pemodelan dan simulasi komputasi untuk mitigasi bencana lokal (simulasi evakuasi berbasis grid spasial).
Terinspirasi dari materi kuliah umum oleh **Asst. Prof. Dr. Warawan Diaz Carbalo** (Thammasat University, Thailand) dalam *Informatics Practitioner Lecture Series*.

## 🌍 Deskripsi Proyek
Bagaimana infrastruktur komputasi berkinerja tinggi (*High Performance Computing* / HPC) dapat menjembatani penyelesaian masalah lokal seperti evakuasi bencana, manajemen kota cerdas, dan mitigasi risiko lingkungan.

## 🛠️ Struktur Modul
- **`simulation_model.py`**: Skrip inti untuk memodelkan koordinat agen/warga dan menghitung waktu evakuasi tercepat menuju zona aman.
- **`data_generator.py`**: Menghasilkan data spasial sintetis (koordinat area rawan dan titik kumpul).
- **`dataset/`**: Menyimpan data log simulasi.
- **`output/`**: Menyimpan grafik visualisasi hasil simulasi.

## 🚀 Cara Menjalankan
1. Install dependensi: `pip install -r requirements.txt`
2. Jalankan generator data: `python data_generator.py`
3. Jalankan model simulasi: `python simulation_model.py`