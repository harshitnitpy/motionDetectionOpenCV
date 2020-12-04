import cv2, time

video = cv2.VideoCapture(1)
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

a = 1
while True:
    a = a+1
    check, frame = video.read()
    print(check)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.05, 5)
    print(faces)

    for x, y, w, h in faces:
        gray = cv2.rectangle(gray, (x, y), (x + w, y + h), (0, 255, 0), 3)

    cv2.imshow("Gray", gray)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break


print(a)
video.release()
cv2.destroyAllWindows()



