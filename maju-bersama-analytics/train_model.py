import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
import joblib
import os

print("🤖 Memuat data bersih untuk pelatihan model Machine Learning...")
df = pd.read_csv('dataset/cleaned_transactions.csv')

# Memisahkan fitur (X) dan target (y). Menghindari data leakage.
X = df[['order_amount', 'discount_given', 'credit_score', 'avg_delay_days']]
y = df['is_late_payment']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("🌲 Melatih model Random Forest Classifier...")
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print(f"✅ Akurasi Model: {accuracy_score(y_test, y_pred) * 100:.2f}%\n")
print(classification_report(y_test, y_pred))

os.makedirs('model', exist_ok=True)
joblib.dump(model, 'model/late_payment_model.pkl')
print("💾 Model AI berhasil disimpan ke 'model/late_payment_model.pkl'!")
