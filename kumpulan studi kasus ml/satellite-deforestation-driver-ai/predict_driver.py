import pandas as pd
import joblib

print("🔍 Memuat model AI atribusi driver terlatih...")
model = joblib.load('model/deforestation_driver_model.pkl')

# Simulasi data alert deforestasi baru dari citra satelit terkini
new_alerts = pd.DataFrame({
    's2_ndvi': [0.25, 0.15, 0.65, 0.30],
    's2_swir': [3200, 3800, 1500, 2900],
    's1_vh_db': [-18.5, -7.2, -12.0, -16.8],
    's1_vv_db': [-12.1, -2.5, -8.5, -10.4]
})

predictions = model.predict(new_alerts)
probabilities = model.predict_proba(new_alerts)

print("\n🎯 Hasil Atribusi AI pada Alert Deforestasi Terkini:")
for i, (pred, prob) in enumerate(zip(predictions, probabilities)):
    confidence = max(prob) * 100
    print(f" - Deforestation Alert #{i+1}: Atribusi Penyebab -> [{pred}] (Tingkat Keyakinan AI: {confidence:.1f}%)")
