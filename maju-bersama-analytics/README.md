# PT Maju Bersama: Financial Data Analytics & Late Payment Prediction AI

Repository ini berisi studi kasus dan implementasi analisis data serta pemodelan Machine Learning untuk mendiagnosis masalah keuangan perusahaan dan memprediksi risiko keterlambatan pembayaran (*late payment*) pelanggan.
Terinspirasi dari materi kuliah umum *'Make Sense of Data with Analysis and AI'* oleh **Andria Arisal, M.Eng.** (Senior Researcher / Principal Administrator HPC BRIN).

## Fitur & Modul Proyek
- **Data Preparation & Cleaning (`data_preprocessing.py`)**: Menangani data kotor, validasi tipe data, serta *feature engineering* untuk mencegah kebocoran data (*data leakage*).
- **Model Training & Machine Learning (`train_model.py`)**: Melatih model klasifikasi (*Random Forest & Logistic Regression*) untuk memprediksi risiko piutang macet.
- **Evaluasi & Prediksi (`predict.py`)**: Menguji model terhadap data transaksi baru.

## Cara Menjalankan
1. Install dependensi: `pip install -r requirements.txt`
2. Jalankan preprocessing: `python data_preprocessing.py`
3. Latih model Machine Learning: `python train_model.py`
4. Lakukan prediksi: `python predict.py`