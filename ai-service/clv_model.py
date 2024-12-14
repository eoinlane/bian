import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

# Load dataset from a CSV file
data_file = "customer_data.csv"
df = pd.read_csv(data_file)

# Define features and target variable
X = df[["total_purchases", "avg_purchase_value"]]
y = df["lifetime_value"]

# Train model
model = LinearRegression().fit(X, y)

# Save the model
with open("clv_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model trained and saved as clv_model.pkl")
