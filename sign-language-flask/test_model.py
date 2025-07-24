import pickle
import numpy as np

try:
    # Load model and labels separately
    with open("model_only.p", "rb") as f:
        model = pickle.load(f)

    with open("labels.p", "rb") as f:
        labels_dict = pickle.load(f)

    print("✅ Model and labels loaded successfully!")

    # Dummy input (make sure it matches model.n_features_in_)
    dummy_input = [0] * model.n_features_in_
    prediction = model.predict([dummy_input])[0]
    print("✅ Prediction:", prediction)

    # Optionally show predicted label
    if prediction in labels_dict.values():
        predicted_char = list(labels_dict.keys())[list(labels_dict.values()).index(prediction)]
        print("✅ Predicted character:", predicted_char)
    else:
        print("⚠️ Predicted label not found in labels_dict.")

except Exception as e:
    print("❌ Error:", str(e))
