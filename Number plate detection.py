import cv2
import easyocr

# Initialize the EasyOCR reader
reader = easyocr.Reader(['en'])

# Function to detect and recognize license plates in a frame
def detect_and_recognize_plate(frame):
    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Perform text detection and recognition using EasyOCR
    results = reader.readtext(gray)
    
    # Loop over the results
    for detection in results:
        # Extract the bounding box and text from the detection
        bbox = detection[0]
        text = detection[1]
        
        # Draw the bounding box and text on the frame
        cv2.rectangle(frame, bbox[0], bbox[2], (0, 255, 0), 2)
        cv2.putText(frame, text, (bbox[0][0], bbox[0][1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
    
    return frame

# Capture video from webcam
cap = cv2.VideoCapture(0)

while True:
    # Read a frame from the video capture
    ret, frame = cap.read()
    if not ret:
        break
    
    # Detect and recognize license plates in the frame
    frame_with_plates = detect_and_recognize_plate(frame)
    
    # Display the frame with detected and recognized license plates
    cv2.imshow('License Plate Detector & Recognizer', frame_with_plates)
    
    # Break the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close all windows
cap.release()
cv2.destroyAllWindows()
