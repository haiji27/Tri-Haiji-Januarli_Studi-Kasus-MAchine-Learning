import pandas as pd
import matplotlib.pyplot as plt
import os

print("📊 Menghasilkan grafik analitik berdasarkan prinsip HCI...")
# Simulasi dataset metrik infrastruktur kota
data = {
    'Bulan': ['Jan', 'Feb', 'Mar', 'Apr', 'Mei', 'Jun'],
    'Laporan_Masuk': [120, 145, 130, 160, 190, 210],
    'Penyelesaian_Selesai': [110, 140, 125, 150, 185, 205]
}
df = pd.DataFrame(data)
os.makedirs('dataset', exist_ok=True)
os.makedirs('static/images', exist_ok=True)
df.to_csv('dataset/city_metrics.csv', index=False)

# Membuat Grafik Bersih (Tanpa Chart Junk)
plt.figure(figsize=(8, 4))
plt.plot(df['Bulan'], df['Laporan_Masuk'], marker='o', color='#007BFF', linewidth=2, label='Laporan Masuk')
plt.plot(df['Bulan'], df['Penyelesaian_Selesai'], marker='s', color='#28A745', linewidth=2, label='Diselesaikan')
plt.title('Tren Penanganan Laporan Fasilitas Publik', fontsize=12, fontweight='bold', pad=15)
plt.xlabel('Bulan', fontsize=10)
plt.ylabel('Jumlah Kasus', fontsize=10)
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend()
plt.tight_layout()

plt.savefig('static/images/trend_chart.png', dpi=300)
plt.close()
print("✅ Grafik 'trend_chart.png' berhasil dibuat!")
