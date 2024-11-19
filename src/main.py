import cv2
import time
import threading
from pynput.keyboard import Controller
from ultralytics import YOLO

model = YOLO('glasses_v2_640.pt', task='detect')

keyboard = Controller()

REDUCED_GAS_PERCENTAGE = 0.7  
FULL_GAS_PERCENTAGE = 1.0  
FULL_CYCLE_TIME = 1.0 

stop_flag = False
glasses_status = 'face_without_glasses'

def give_reduced_gas():
    global glasses_status
    while not stop_flag:
        if glasses_status == 'face_with_glasses':
            print("Brille erkannt, reduziere Gas.")
            keyboard.press('w')
            time.sleep(REDUCED_GAS_PERCENTAGE * FULL_CYCLE_TIME)
            keyboard.release('w')
            time.sleep((1 - REDUCED_GAS_PERCENTAGE) * FULL_CYCLE_TIME)
        else:
            print("Keine Brille erkannt - Volles Gas.")
            keyboard.press('w')  # 100 % Gas geben
            time.sleep(FULL_GAS_PERCENTAGE * FULL_CYCLE_TIME)
            keyboard.release('w')


def detect_glasses(frame):
    results = model(frame, conf=0.4)
    detected_objects = results[0].boxes

    if len(detected_objects) == 0:
        return 'no_detection'
    else:
        closest_object = None
        max_area = 0

        for detected_object in detected_objects:
            box = detected_object.xyxy[0]
            area = (box[2] - box[0]) * (box[3] - box[1])
            if area > max_area:
                max_area = area
                closest_object = detected_object

        if closest_object:
            if closest_object.cls.item() == 0:
                return 'face_with_glasses'
            elif closest_object.cls.item() == 1:
                return 'face_without_glasses'
            else:
                return 'no_object'
        else:
            return 'no_object'


def process_frame():
    global glasses_status
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Fehler beim Öffnen der Kamera")
        return

    while not stop_flag:
        ret, frame = cap.read()
        if not ret:
            print("Fehler beim Erfassen des Frames")
            break

        glasses_status = detect_glasses(frame)

        cv2.imshow('Kameraansicht', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()


def main():
    global stop_flag
    
    time.sleep(5)

    frame_thread = threading.Thread(target=process_frame)
    frame_thread.daemon = True
    frame_thread.start()

    gas_thread = threading.Thread(target=give_reduced_gas)
    gas_thread.daemon = True
    gas_thread.start()
    
    print("Gassteuerung und Brillenerkennung gestartet...")
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Beende das Programm durch Strg + C...")
        stop_flag = True
        frame_thread.join()
        gas_thread.join()

if __name__ == "__main__":
    main()