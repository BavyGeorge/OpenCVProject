import cv2
import Face_Recognition_Main as Fr

# Reading image from Resources directory
test_img = cv2.imread("Resources/ram1.jpg")
faces_detected, gray_img = Fr.DetectingFaces(test_img)
print("Face detected: ", faces_detected)

# faces,faceID = Fr.trainingDataFolders("Resources/Images")
# face_recognizer=Fr.train_Classifier(faces,faceID)
# face_recognizer.save('Resources/Trainedfile/trainingData.yml')

face_recognizer = cv2.face.LBPHFaceRecognizer_create()
face_recognizer.read("Resources/Trainedfile/trainingData.yml")

name = {0: "Bavy", 1: "Rambabu"}

# x,y,w,h represents dimensions of Image to x,y axis and w,h as width and height
for face in faces_detected:
    (x, y, w, h) = face
    roi_gray = gray_img[y:y + h, x:x + h]
    label, confidence = face_recognizer.predict(roi_gray)
    print("confidence:", confidence)
    print("label:", name[label])
    Fr.draw_Rectangle(test_img, face)
    predicted_name = name[label]
    Fr.text_Overlay(test_img, predicted_name, x, y)
    resized_img = cv2.resize(test_img, (1000, 700))
    cv2.imshow("Face Detection App", resized_img)
    if cv2.waitKey(0) & 0xFF == ord('s'):
        break
cv2.destroyAllWindows()
