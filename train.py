import pandas as pd
import numpy as np
import os
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_absolute_error, r2_score

# 1. Dataset Load
data_path = os.path.join('dataset', 'benchmark_data.csv')

if not os.path.exists(data_path):
    print("Error: dataset/benchmark_data.csv file nahi mili!")
    exit()

df = pd.read_csv(data_path)

# 2. Features (X) aur Target (y) Separate Karein
X = df[['gpu_score', 'cpu_cores', 'ram_gb', 'resolution', 'game']]
y = df['fps']

# 3. Categorical Variables Ko Preprocess Karne Ka Pipeline
categorical_features = ['resolution', 'game']
preprocessor = ColumnTransformer(
    transformers=[
        ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_features)
    ],
    remainder='passthrough'
)

# 4. ML Model Pipeline (Random Forest Regressor)
model_pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('regressor', RandomForestRegressor(n_estimators=100, random_state=42))
])

# 5. Train / Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 6. Model Training
model_pipeline.fit(X_train, y_train)

# 7. Model Evaluation
y_pred = model_pipeline.predict(X_test)
print(f"Model Training Complete!")
print(f"Mean Absolute Error (MAE): {mean_absolute_error(y_test, y_pred):.2f} FPS")
print(f"R2 Score: {r2_score(y_test, y_pred):.2f}")

# 8. Model Save
joblib.dump(model_pipeline, 'model.pkl')
print("Model pipeline successfully saved as 'model.pkl'!")