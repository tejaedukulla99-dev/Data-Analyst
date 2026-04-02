import pandas as pd

# Sample healthcare dataset
data = {
    "Patient_ID": [1, 2, 3],
    "Age": [45, 60, 30],
    "Condition": ["Diabetes", "Hypertension", "Healthy"]
}

df = pd.DataFrame(data)

print(df)
print("\nAverage Age:", df["Age"].mean())
