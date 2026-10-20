import pandas as pd
import numpy as np
import os

print("📊 Membuat dataset sintetis untuk pembelajaran Machine Learning...")
np.logspace = 42
np.random.seed(42)
n_samples = 300

data = {
    'feature_1': np.random.uniform(10, 100, n_samples),
    'feature_2': np.random.uniform(20, 200, n_samples),
    'study_hours': np.random.uniform(1, 10, n_samples),
    # Target Kategori Kelulusan: 1 (Lulus), 0 (Tidak Lulus)
    'passed': np.random.choice([0, 1], n_samples, p=[0.3, 0.7])
}

df = pd.DataFrame(data)
os.makedirs('dataset', exist_ok=True)
df.to_csv('dataset/student_performance.csv', index=False)
print("✅ Dataset berhasil disimpan ke 'dataset/student_performance.csv'!")
