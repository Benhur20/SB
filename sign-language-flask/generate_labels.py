import pickle

# Create a dictionary: 0 -> 'A', 1 -> 'B', ..., 25 -> 'Z'
labels_dict = {i: chr(65 + i) for i in range(26)}

# Save it to labels.p
with open("labels.p", "wb") as f:
    pickle.dump(labels_dict, f)

print("✅ labels.p created successfully with A-Z mapping.")
