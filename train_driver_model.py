import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
import joblib
import os

print("📂 Menyiapkan dataset fitur gabungan Satelit Optik (Sentinel-2) & Radar (Sentinel-1)...")

# Simulasi data ektraksi piksel satelit pada area alert deforestasi
np.random.seed(42)
n_samples = 200

# Fitur Sentinel-2 (Optik: NDVI, B8-NIR, B11-SWIR)
s2_ndvi = np.random.uniform(0.1, 0.8, n_samples)
s2_swir = np.random.uniform(1000, 4000, n_samples)

# Fitur Sentinel-1 (Radar Backscatter: VV, VH dB)
s1_vh = np.random.uniform(-20, -5, n_samples)
s1_vv = np.random.uniform(-15, 0, n_samples)

# Kategori Pendorong Langsung (Direct Drivers)
drivers = ['Large-scale Agriculture', 'Smallholder Agriculture', 'Selective Logging', 'Mining', 'Wildfire']
labels = np.random.choice(drivers, n_samples)

df = pd.DataFrame({
    's2_ndvi': s2_ndvi,
    's2_swir': s2_swir,
    's1_vh_db': s1_vh,
    's1_vv_db': s1_vv,
    'driver_class': labels
})

os.makedirs('dataset', exist_ok=True)
df.to_csv('dataset/satellite_deforestation_features.csv', index=False)

X = df[['s2_ndvi', 's2_swir', 's1_vh_db', 's1_vv_db']]
y = df['driver_class']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

print("🌲 Melatih model klasifikasi atribusi driver deforestasi...")
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print(f"✅ Akurasi Model Atribusi Satelit: {accuracy_score(y_test, y_pred) * 100:.2f}%\n")
print(classification_report(y_test, y_pred))

os.makedirs('model', exist_ok=True)
joblib.dump(model, 'model/deforestation_driver_model.pkl')
print("💾 Model AI berhasil disimpan ke 'model/deforestation_driver_model.pkl'!")
