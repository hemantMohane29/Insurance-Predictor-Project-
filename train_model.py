import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

# Load the dataset
df = pd.read_csv('insurance.csv')

# Use pandas to convert categorical columns into numerical ones
# This is a simple and common way to preprocess data for ML
df_processed = pd.get_dummies(df, columns=['sex', 'smoker', 'region'], drop_first=True)

# Separate features (X) and target (y)
X = df_processed.drop('charges', axis=1)
y = df_processed['charges']

# Create and train the model
model = LinearRegression()
model.fit(X, y)

# Save the trained model
joblib.dump(model, 'linear_regression_model.pkl')

# Save the list of column names (features) to use later
# This is crucial for making sure the form data is in the right order
model_columns = X.columns.tolist()
joblib.dump(model_columns, 'model_columns.pkl')

print("Model training complete and files saved.")