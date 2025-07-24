import pickle

# Load dictionary that contains 'model' and optionally 'labels_dict'
with open("model.p", "rb") as f:
    model_dict = pickle.load(f)

# Extract and save only the model
model = model_dict['model']
with open("model_only.p", "wb") as f:
    pickle.dump(model, f)

# (Optional) If labels_dict exists, save that too
if 'labels_dict' in model_dict:
    with open("labels.p", "wb") as f:
        pickle.dump(model_dict['labels_dict'], f)

print("✅ Model and labels saved separately.")
