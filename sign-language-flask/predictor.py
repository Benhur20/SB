import cv2
import pickle
import mediapipe as mp

# ✅ Load the model
with open('model_only.p', 'rb') as f:
    model = pickle.load(f)

# ✅ Load the label dictionary
with open('labels.p', 'rb') as f:
    labels_dict = pickle.load(f)

# ✅ Mediapipe setup
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

def start_prediction():
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("❌ Error: Could not open webcam.")
        return "Camera Error"

    with mp_hands.Hands(
        static_image_mode=False,
        max_num_hands=1,
        min_detection_confidence=0.5
    ) as hands:

        while True:
            ret, frame = cap.read()
            if not ret:
                print("❌ Failed to read from camera.")
                break

            h, w, _ = frame.shape
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = hands.process(rgb_frame)

            if results.multi_hand_landmarks:
                print("✅ Hand detected")

                for hand_landmarks in results.multi_hand_landmarks:
                    # ✅ Collect landmark data
                    data = []
                    for landmark in hand_landmarks.landmark:
                        data.extend([landmark.x, landmark.y, landmark.z])

                    # ✅ Ensure correct feature vector length
                    if len(data) != model.n_features_in_:
                        print(f"⚠️ Feature length mismatch: expected {model.n_features_in_}, got {len(data)}")
                        continue

                    # ✅ Predict
                    prediction = model.predict([data])[0]

                    # ✅ Get label from prediction
                    predicted_label = list(labels_dict.keys())[list(labels_dict.values()).index(prediction)]

                    # ✅ Draw landmarks
                    mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                    # ✅ Show prediction label
                    cv2.putText(
                        frame, f"Prediction: {predicted_label}", (10, 50),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2
                    )

            else:
                print("⚠️ No hand detected.")

            # ✅ Show the frame
            cv2.imshow("Prediction", frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    cap.release()
    cv2.destroyAllWindows()
    return predicted_label if 'predicted_label' in locals() else "No Prediction"
