import pandas as pd
import numpy as np
import os

print("📊 Menghasilkan dataset spasial titik evakuasi warga...")
np.random.seed(42)
n_agents = 500

data = {
    'agent_id': range(1, n_agents + 1),
    'coord_x': np.random.uniform(0, 100, n_agents),
    'coord_y': np.random.uniform(0, 100, n_agents),
    'zone_risk_level': np.random.choice(['Low', 'Medium', 'High'], n_agents, p=[0.5, 0.3, 0.2]),
    'distance_to_shelter_km': np.random.uniform(0.5, 12.0, n_agents)
}

df = pd.DataFrame(data)
os.makedirs('dataset', exist_ok=True)
df.to_csv('dataset/evacuation_zones.csv', index=False)
print("✅ Dataset spasial berhasil disimpan ke 'dataset/evacuation_zones.csv'!")
