# Interactive DataViz: HCI & Data Visualization Dashboard

Repository ini berisi studi kasus dan implementasi dashboard visualisasi data interaktif yang menerapkan prinsip Human-Computer Interaction (HCI) dan User-Centered Design. Terinspirasi dari materi kuliah umum oleh Dr. Arafat Febriandirza (Badan Riset dan Inovasi Nasional / BRIN).

## Fitur Proyek
- **Prinsip HCI**: Menerapkan visual yang bersih, intuitif, dan memperhatikan beban kognitif pengguna (mengurangi *chart junk*).
- **Visualisasi Otomatis (`generate_charts.py`)**: Mengolah dataset metrik kota menjadi grafik analitik berbasis Matplotlib.
- **Dashboard Web Interaktif (`app.py`)**: Menyajikan informasi secara real-time menggunakan Flask.

## Cara Menjalankan
1. Install dependensi: `pip install -r requirements.txt`
2. Generate grafik visualisasi: `python generate_charts.py`
3. Jalankan server dashboard: `python app.py`
4. Buka browser di: `http://127.0.0.1:5000`