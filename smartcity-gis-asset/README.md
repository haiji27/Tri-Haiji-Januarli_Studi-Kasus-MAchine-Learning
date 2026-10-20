# SmartCity-GIS: Cloud-Based Asset Management & Public Reporting System

Repository ini berisi studi kasus dan implementasi sistem berbasis WebGIS untuk pengelolaan aset kota dan pelaporan fasilitas publik secara *seamless* berbasis *cloud*. Terinspirasi dari materi kuliah umum *Career and Competition in Industrial Era with GIS* oleh Widi Primadepa (Asset Management GIS Analyst di City Care Property, Selandia Baru / Alumni Teknik Informatika UNIB).

## Fitur Proyek
- **Peta Web Interaktif**: Dibangun menggunakan *Leaflet.js* dan *OpenStreetMap* untuk navigasi spasial.
- **Integrasi Cloud Database**: Menyimpan titik koordinat fasilitas publik dan laporan infrastruktur secara terpusat menggunakan Flask & SQLite.
- **Input Lapangan Real-Time**: Memungkinkan petugas/warga mengambil titik koordinat langsung dari antarmuka peta tanpa proses manual yang rumit.

## Cara Menjalankan
1. Install dependensi: `pip install -r requirements.txt`
2. Jalankan server backend: `python app.py`
3. Buka browser dan akses: `http://127.0.0.1:5000`