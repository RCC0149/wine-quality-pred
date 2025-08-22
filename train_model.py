import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
import joblib

# Load datasets
df_red = pd.read_csv('winequality-red.csv', sep=';')
df_white = pd.read_csv('winequality-white.csv', sep=';')

# Combine datasets
df = pd.concat([df_red, df_white], axis=0)

# Features and target (all 11 original features)
X = df.drop('quality', axis=1)
y = df['quality']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# Scale features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Save scaler for inference
joblib.dump(scaler, 'scaler.pkl')

# Define model with best parameters
model = RandomForestClassifier(
    n_estimators=180,
    max_depth=None,
    min_samples_split=2,
    min_samples_leaf=1,
    class_weight='balanced',
    random_state=42
)

# Train model
model.fit(X_train_scaled, y_train)

# Evaluate on test set
predictions = model.predict(X_test_scaled)
print(f'Test Accuracy: {accuracy_score(y_test, predictions):.4f}')

# Print feature importance
feature_names = X.columns
importances = model.feature_importances_
for name, importance in zip(feature_names, importances):
    print(f'Feature: {name}, Importance: {importance:.4f}')

# Save model
joblib.dump(model, 'wine_model.pkl', compress=3)