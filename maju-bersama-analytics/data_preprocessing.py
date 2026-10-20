import pandas as pd
import numpy as np
import os

print("📂 Mensimulasikan dan membersihkan data transaksi PT Maju Bersama...")

np.random.seed(42)
n_samples = 1000

# Simulasi data transaksi pelanggan
data = {
    'customer_id': np.random.randint(101, 220, n_samples),
    'order_amount': np.random.uniform(500, 15000, n_samples),
    'discount_given': np.random.choice([0, 5, 10, 25], n_samples, p=[0.6, 0.2, 0.1, 0.1]),
    'credit_score': np.random.randint(500, 850, n_samples),
    'avg_delay_days': np.random.randint(0, 45, n_samples),
    # Target: 1 jika terlambat bayar (>30 hari), 0 jika lancar
    'is_late_payment': np.random.choice([0, 1], n_samples, p=[0.75, 0.25])
}

df = pd.DataFrame(data)

# Data Preparation & Cleaning (Menghilangkan anomali / data kotor)
df = df.dropna()
df = df[df['order_amount'] > 0] # Mencegah impossible order

os.makedirs('dataset', exist_ok=True)
df.to_csv('dataset/cleaned_transactions.csv', index=False)
print("✅ Data berhasil dibersihkan dan disimpan ke 'dataset/cleaned_transactions.csv'!")
