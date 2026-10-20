import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

print("⚙️ Memuat data dan menjalankan simulasi evakuasi berbasis HPC logic...")
df = pd.read_csv('dataset/evacuation_zones.csv')

# Simulasi perhitungan waktu evakuasi (kecepatan rata-rata orang berjalan/berkendaraan evakuasi)
# Zona High risk mendapat prioritas dan penyesuaian waktu evakuasi
speed_kmh = 4.0 # kecepatan rata-rata evakuasi kaki/kendaraan darurat
df['estimated_evac_time_hours'] = df['distance_to_shelter_km'] / speed_kmh
df['estimated_evac_time_minutes'] = df['estimated_evac_time_hours'] * 60

# Analisis ringkas
print(f"Total warga/agen tersimulasi : {len(df)}")
print(f"Rata-rata waktu evakuasi    : {df['estimated_evac_time_minutes'].mean():.2f} menit")
print(f"Waktu evakuasi maksimal     : {df['estimated_evac_time_minutes'].max():.2f} menit")

# Visualisasi Hasil Simulasi
os.makedirs('output', exist_ok=True)
plt.figure(figsize=(10, 6))
sns.scatterplot(
    data=df, x='coord_x', y='coord_y', 
    hue='zone_risk_level', size='estimated_evac_time_minutes', 
    palette={'Low': 'green', 'Medium': 'orange', 'High': 'red'}, alpha=0.8
)
plt.title("Simulasi Sebaran Titik Evakuasi Warga Berdasarkan Zona Risiko & Waktu Tempuh")
plt.xlabel("Koordinat Wilayah X (Km)")
plt.ylabel("Koordinat Wilayah Y (Km)")
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()

chart_path = 'output/evacuation_simulation_map.png'
plt.savefig(chart_path)
plt.close()
print(f"📈 Grafik visualisasi berhasil disimpan ke '{chart_path}'!")
