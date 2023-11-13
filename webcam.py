import cv2


url = 'http://admin:root@1234@10.0.0.47:88/cgi-bin/guest/Video.cgi?media=JPEG'
cap = cv2.VideoCapture(url)
while True:
    ret, frame = cap.read()
    cv2.imshow('Webcam', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()