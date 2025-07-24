# train_model.py
import pickle
from sklearn.ensemble import RandomForestClassifier

# Load your preprocessed data
with open("data.pickle", "rb") as f:
    data_dict = pickle.load(f)

X = data_dict["data"]
y = data_dict["labels"]

# Train the model
model = RandomForestClassifier()
lengths = [len(sample) for sample in X]
print("Sample feature lengths summary:")
print("Min:", min(lengths), "Max:", max(lengths), "Unique lengths:", set(lengths))

model.fit(X, y)

# Save model separately
with open("model.p", "wb") as f:
    pickle.dump(model, f)

# Save labels_dict separately
labels_dict = {i: chr(65 + i) for i in range(26)}  # A-Z
with open("labels.p", "wb") as f:
    pickle.dump(labels_dict, f)

print("✅ Model saved to model.p")
print("✅ Labels dictionary saved to labels.p")
