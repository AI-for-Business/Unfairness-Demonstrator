import cv2
import time
import threading
from pynput.keyboard import Controller
from ultralytics import YOLO
import mediapipe as mp

# Initialize the model
model = YOLO('models/glasses_v2_640.pt', task='detect')
keyboard = Controller()

# Configuration values
REDUCED_GAS_PERCENTAGE = 0.7
FULL_GAS_PERCENTAGE = 1.0  
FULL_CYCLE_TIME = 1.0  

# Global variables
stop_flag = False
blink_status = 'not_blinking'
no_frame_detected_time = None
blink_count = 0
last_blink_time = time.time()
last_glasses_check_time = time.time()
glasses_check_interval = 5
treshhold = 0.15

# Mediapipe face detection
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(
    max_num_faces=1,
    refine_landmarks=True,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)

LEFT_EYE = [33, 160, 158, 133, 153, 144]
RIGHT_EYE = [362, 385, 387, 263, 373, 380]

# Open camera
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error opening camera")
    exit()

# Calculate EAR (Eye Aspect Ratio)
def calculate_ear(eye_landmarks):
    A = ((eye_landmarks[1][0] - eye_landmarks[5][0]) ** 2 + (eye_landmarks[1][1] - eye_landmarks[5][1]) ** 2) ** 0.5
    B = ((eye_landmarks[2][0] - eye_landmarks[4][0]) ** 2 + (eye_landmarks[2][1] - eye_landmarks[4][1]) ** 2) ** 0.5
    C = ((eye_landmarks[0][0] - eye_landmarks[3][0]) ** 2 + (eye_landmarks[0][1] - eye_landmarks[3][1]) ** 2) ** 0.5
    return (A + B) / (2.0 * C)

# Glasses detection
def detect_glasses(frame):
    results = model(frame, conf=0.4)
    detected_objects = results[0].boxes
    
    if len(detected_objects) == 0:
        return 'no_detection'
    
    closest_object = max(detected_objects, key=lambda obj: (obj.xyxy[0][2] - obj.xyxy[0][0]) * (obj.xyxy[0][3] - obj.xyxy[0][1]), default=None)
    
    if closest_object:
        return 'face_with_glasses' if closest_object.cls.item() == 0 else 'face_without_glasses'
    
    return 'no_object'

# Blink detection
def detect_blinks(frame):
    global blink_count, last_blink_time, treshhold, blink_status
    
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(rgb_frame)
    
    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:
            left_eye_landmarks = [(face_landmarks.landmark[idx].x * frame.shape[1], face_landmarks.landmark[idx].y * frame.shape[0]) for idx in LEFT_EYE]
            right_eye_landmarks = [(face_landmarks.landmark[idx].x * frame.shape[1], face_landmarks.landmark[idx].y * frame.shape[0]) for idx in RIGHT_EYE]
            
            ear = (calculate_ear(left_eye_landmarks) + calculate_ear(right_eye_landmarks)) / 2.0
            
            if ear < treshhold:
                cv2.putText(frame, "Blinking", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                blink_count += 1
                last_blink_time = time.time()
    
    blink_status = 'not_blinking' if time.time() - last_blink_time > 10 else 'blinking'

# Frame processing
def process_frame():
    global last_glasses_check_time, treshhold, no_frame_detected_time, stop_flag
    
    while not stop_flag:
        ret, frame = cap.read()
        if not ret:
            if no_frame_detected_time is None:
                no_frame_detected_time = time.time()
            elif time.time() - no_frame_detected_time > 20:
                print("No frame detected, terminating program.")
                stop_flag = True
                break
            continue
        else:
            no_frame_detected_time = None

        detect_blinks(frame)
        
        if time.time() - last_glasses_check_time > glasses_check_interval:
            print("Glasses Detection")
            last_glasses_check_time = time.time()
            
            glasses_status = detect_glasses(frame)
            treshhold = 0.05 if glasses_status == 'face_with_glasses' else 0.20
        
        cv2.imshow('YOLOv8 Predictions and Eye Landmarks', frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            stop_flag = True
            break

# Reduce gas if driver is tired
def give_reduced_gas():
    global blink_status
    while not stop_flag:
        if blink_status == 'not_blinking':
            print("Fatigue detected, reducing gas.")
            keyboard.press(" ")
            time.sleep(REDUCED_GAS_PERCENTAGE * FULL_CYCLE_TIME)
            keyboard.release(" ")
            time.sleep((1 - REDUCED_GAS_PERCENTAGE) * FULL_CYCLE_TIME) 
        else:
            print("No fatigue detected - full gas.")
            time.sleep(1)

# Start threads
processing_thread = threading.Thread(target=process_frame)
gas_thread = threading.Thread(target=give_reduced_gas)

processing_thread.start()
gas_thread.start()

processing_thread.join()
gas_thread.join()

cap.release()
cv2.destroyAllWindows()
