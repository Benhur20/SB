# train_model.py
import pickle
from sklearn.ensemble import RandomForestClassifier

with open("data.pickle", "rb") as f:
    data_dict = pickle.load(f)

X = data_dict["data"]
y = data_dict["labels"]

model = RandomForestClassifier()
lengths = [len(sample) for sample in X]
print("Sample feature lengths summary:")
print("Min:", min(lengths), "Max:", max(lengths), "Unique lengths:", set(lengths))

model.fit(X, y)

# Save the model in a format Flask expects
model_dict = {
    'model': model,
    'labels_dict': {i: chr(65 + i) for i in range(26)}  # 0 -> A, 1 -> B, ...
}

with open("model.p", "wb") as f:
    pickle.dump(model_dict, f)

print("✅ Model trained and saved to model.p")
