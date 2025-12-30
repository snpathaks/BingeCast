import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import joblib  

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error


try:
    df = pd.read_csv('bingecast_dataset.csv')
    print("✅ Dataset loaded successfully.")
except FileNotFoundError:
    print("❌ Dataset not found. Please run 'generate_data.py' first.")
    exit()


X = df[['Age', 'Mood', 'Preferred Genre', 'Time of Day']]
y = df['Episodes']


categorical_features = ['Mood', 'Preferred Genre', 'Time of Day']

# Create preprocessor
preprocessor = ColumnTransformer(
    transformers=[
        ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_features)
    ],
    remainder='passthrough'
)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


print("\nTraining Model...")
model_pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('regressor', RandomForestRegressor(n_estimators=100, random_state=42))
])

model_pipeline.fit(X_train, y_train)

# 4. Evaluation
y_pred = model_pipeline.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
print(f"✅ Model Trained. Mean Absolute Error: {mae:.2f} episodes")


joblib.dump(model_pipeline, 'bingecast_model.pkl')
print("💾 Model saved to 'bingecast_model.pkl'")


plt.figure(figsize=(8, 6))
sns.scatterplot(x=y_test, y= y_pred, alpha=0.6)
plt.plot([y.min(), y.max()], [y.min(), y.max()], 'r--')
plt.xlabel("Actual Episodes")
plt.ylabel("Predicted Episodes")
plt.title("Actual vs Predicted Binge-Watching")
plt.savefig('model_performance.png')
print("📊 Performance plot saved to 'model_performance.png'")
