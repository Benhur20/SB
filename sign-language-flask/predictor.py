import cv2
import pickle
import mediapipe as mp

# ✅ Load the trained model (trained with string number labels like '0', '1', ..., '25')
with open('model_only.p', 'rb') as f:
    model = pickle.load(f)

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

                    # ✅ Adjust feature length to match model
                    if len(data) < model.n_features_in_:
                        print(f"⚠️ Feature length too short: expected {model.n_features_in_}, got {len(data)} → padding")
                        data.extend([0] * (model.n_features_in_ - len(data)))
                    elif len(data) > model.n_features_in_:
                        print(f"⚠️ Feature length too long: expected {model.n_features_in_}, got {len(data)} → trimming")
                        data = data[:model.n_features_in_]

                    # ✅ Predict using the model
                    prediction = model.predict([data])[0]  # prediction like '24', '20', etc.

                    # ✅ Convert prediction (e.g. '24') to letter (e.g. 'Y')
                    if isinstance(prediction, str) and prediction.isdigit():
                        predicted_label = chr(65 + int(prediction))  # 65 = 'A'
                    else:
                        predicted_label = prediction  # fallback if already a letter

                    # ✅ Draw landmarks
                    mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                    # ✅ Show prediction
                    cv2.putText(
                        frame, f"Prediction: {predicted_label}", (10, 50),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2
                    )

            else:
                print("⚠️ No hand detected.")

            cv2.imshow("Prediction", frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    cap.release()
    cv2.destroyAllWindows()
    return predicted_label if 'predicted_label' in locals() else "No Prediction"
