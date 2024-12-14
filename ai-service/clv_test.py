import pandas as pd
import pickle

# Load the model
with open("clv_model.pkl", "rb") as f:
    model = pickle.load(f)

# Test data
test_data = pd.DataFrame([[250, 65]], columns=["total_purchases", "avg_purchase_value"])

# Predict CLV
predicted_clv = model.predict(test_data)[0]
print(f"Predicted Customer Lifetime Value: {round(predicted_clv, 2)}")

# Optional: Debug coefficients and intercept
print("Coefficients:", model.coef_)
print("Intercept:", model.intercept_)

# Manual calculation for verification
manual_clv = (
    model.coef_[0] * test_data.iloc[0]["total_purchases"]
    + model.coef_[1] * test_data.iloc[0]["avg_purchase_value"]
    + model.intercept_
)
print(f"Manually Calculated CLV: {round(manual_clv, 2)}")
