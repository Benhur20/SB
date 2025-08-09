import pickle
from collections import Counter

with open('model_only.p', 'rb') as f:
    model = pickle.load(f)

# Get all classes the model knows
print("✅ Classes in the model:", model.classes_)
print("🧠 Total classes:", len(model.classes_))
