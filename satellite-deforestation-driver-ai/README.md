# Satellite-AI-Forest Watch: Attributing Direct Drivers to Deforestation Alerts

Repository ini berisi studi kasus dan implementasi model kecerdasan buatan (AI) berbasis penginderaan jauh (Remote Sensing) untuk mengatribusikan pendorong utama deforestasi (Pertanian Skala Besar/Kecil, Logging, Tambang, Kebakaran) menggunakan data multi-sensor satelit. Terinspirasi dari materi kuliah umum oleh Dr. Bart Slagter (Wageningen University & Research, Belanda).

## Fitur Proyek
- **Integrasi Multi-Sensor (Optik & Radar)**: Menggabungkan nilai reflektansi optik (Sentinel-2) dan backscatter radar (Sentinel-1) untuk mengatasi kendala tutupan awan tropis.
- **Klasifikasi Atribusi AI (`train_driver_model.py`)**: Melatih model Machine/Deep Learning untuk mengklasifikasikan pendorong langsung deforestasi.
- **Prediksi Peringatan Deforestasi (`predict_driver.py`)**: Menganalisis titik alert baru dan menentukan penyebab utamanya secara presisi.

## Cara Menjalankan
1. Install dependensi: `pip install -r requirements.txt`
2. Jalankan pelatihan model atribusi: `python train_driver_model.py`
3. Jalankan pengujian atribusi alert: `python predict_driver.py`