import cv2
from ultralytics import YOLO

# Load the YOLOv8 model
model = YOLO('best.pt')

# Open the webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    # Get camera center point
    height, width = frame.shape[:2]
    cam_center = (width // 2, height // 2)
    
    # Detection
    results = model(frame)
    
    for result in results:
        boxes = result.boxes
        if boxes is not None:
            for box in boxes:
                # Get coordinates
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                conf = box.conf[0]
                cls = int(box.cls[0])
                
                # Draw bounding box
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 2)
                cv2.putText(frame, f'{model.names[cls]} {conf:.2f}', 
                           (x1, y1-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
                
                # Calculate object center point
                obj_center = (int((x1 + x2) / 2), int((y1 + y2) / 2))
                
                # Draw object center point
                cv2.circle(frame, obj_center, 6, (0, 255, 0), -1)
                
                # Draw line from camera center to object center
                cv2.line(frame, cam_center, obj_center, (255, 255, 0), 2)
    
    # Draw camera center point (crosshair)
    #cv2.circle(frame, cam_center, 8, (255, 0, 0), -1)  # Blue center
    #cv2.circle(frame, cam_center, 12, (255, 0, 0), 2)
    
    # Draw crosshair lines
    cv2.line(frame, (cam_center[0]-20, cam_center[1]), (cam_center[0]+20, cam_center[1]), (255, 0, 0), 2)
    cv2.line(frame, (cam_center[0], cam_center[1]-20), (cam_center[0], cam_center[1]+20), (255, 0, 0), 2)
    
    cv2.imshow('Detection with Center', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

