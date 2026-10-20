import pandas as pd
import joblib

print("🔍 Memuat model AI terlatih untuk prediksi pelanggan...")
model = joblib.load('model/late_payment_model.pkl')

# Simulasi data invoice / pelanggan baru yang masuk
new_invoices = pd.DataFrame({
    'order_amount': [3500, 12000, 800],
    'discount_given': [0, 10, 25],
    'credit_score': [780, 520, 610],
    'avg_delay_days': [2, 35, 12]
})

predictions = model.predict(new_invoices)
probabilities = model.predict_proba(new_invoices)

print("\n🎯 Hasil Prediksi Risiko Keterlambatan Pembayaran (Late Payment):")
for i, (pred, prob) in enumerate(zip(predictions, probabilities)):
    status = "⚠️ BERISIKO TELAT" (*"Late"*)" if pred == 1 else "✅ LANCAR" (*"Not Late"*)"
    confidence = max(prob) * 100
    print(f" - Invoice #{i+1}: Status -> {status} (Keyakinan AI: {confidence:.1f}%)")
