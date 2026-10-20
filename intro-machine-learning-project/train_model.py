import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, accuracy_score
import joblib
import os

print("🤖 Melatih model Decision Tree Classifier...")
df = pd.read_csv('dataset/student_performance.csv')

X = df[['feature_1', 'feature_2', 'study_hours']]
y = df['passed']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
acc = accuracy_score(y_test, y_pred) * 100

print(f"✅ Akurasi Model Decision Tree: {acc:.2f}%\n")
print(classification_report(y_test, y_pred))

os.makedirs('model', exist_ok=True)
joblib.dump(model, 'model/decision_tree_model.pkl')
print("💾 Model berhasil disimpan ke 'model/decision_tree_model.pkl'!")
