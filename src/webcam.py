import cv2
import face_recognition
import pickle

HEIGHT = 240
WIDTH = 320 

capture = cv2.VideoCapture(-1)
capture.set(3, WIDTH)
capture.set(4, HEIGHT)
capture.set(5, 10)

#직전 값과, 지금까지의 누적 값
def face_tracking(x_pos, y_pos):
    if x_pos > 0.1: #카메라 입장에서 오른쪽
        print('move head rightward')
        #speed 를 x_pos의 절대값에 비례하도록
    elif x_pos < -0.1:
        print('move head leftward')
    if y_pos > 0.1:
        print('move head upward')
    elif y_pos < -0.1:
        print('move head downward')
    #얼마나 떨어져 있는지에 따라서 속도 다르게? PID 제어?


while True:
    ret, frame = capture.read()
    if not ret: break

    rgb_for_face = frame[::]
    gray_for_emotion = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    #rgb 이미지 피클로 저장, 얼굴인식
    with open("pkl/rgb_for_face.pkl", "wb") as file:
        pickle.dump(rgb_for_face, file) 

    #gray 이미지 피클로 저장, 표정
    with open("pkl/gray_for_emotion.pkl", "wb") as file:
        pickle.dump(gray_for_emotion, file)

    face_locations = face_recognition.face_locations(rgb_for_face)
    ######################################
    #얼굴 위치 피클로 저장, 한명만 저장인데 먼저 인식된? 
    print("number of people: ", len(face_locations))
    

    ##########################################3
    #추가해야할 것, 얼굴 큰 사람이 인식되게끔!!!!!!!!!!!!!!!!!!!!!!!!!!!
    if len(face_locations)==0:
        face_locations=[0,]
    elif len(face_locations)>1:
        face_locations=[face_locations[0]]
    with open("pkl/face_locations.pkl", "wb") as file:
        pickle.dump(face_locations, file)
    #########################################

    for (top, right, bottom, left) in face_locations:
        x_pos = (right+left)/2
        y_pos = (top+bottom)/2

        x_pos = (x_pos - (WIDTH/2)) / WIDTH *2 +0.1
        y_pos = -(y_pos - (HEIGHT/2)) / HEIGHT *2

        #두명이 인식되면, 먼저 인식된 사람 순으로?
        #아니면 더 큰 쪽으로 인식이 가능한가?
        print("x", x_pos," y:", y_pos)

        ##파일로 쏘지 말고 여기서 모터 구동을 제어하자!
        face_tracking(x_pos, y_pos)

        cv2.rectangle(frame, (left, top), (right, bottom), (0,0,255), 2)

    cv2.imshow('frame', frame)
    if cv2.waitKey(1) == ord('q'): break

capture.release()
cv2.destroyAllWindows()
