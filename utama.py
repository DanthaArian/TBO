import cv2
from HandDetection import HandDetection
from recognize_gesture import count_raised_fingers, recognize_gesture

cap = cv2.VideoCapture(0)
detector = HandDetection()

while True:
    success, img = cap.read()
    
    # Membalikkan gambar (mirror)
    img = cv2.flip(img, 1)
    
    # Deteksi dan gambar landmark tangan
    landMarkList = detector.findHandLandMarks(img, draw=True)
    
    if len(landMarkList) != 0:
        finger_count = count_raised_fingers(landMarkList)
        gesture = recognize_gesture(finger_count)

        if gesture:
            cv2.putText(img, gesture, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
