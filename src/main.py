#웹캠 읽고 감정 저장
#사람 등록 버튼(누군지)
#위치, 누구인지, 감정   
#
#
#
#
#
##구동부

#무엇이 문제인가
import time
# import tkinter
import pickle

def face_position():
    file = open("WebcamOutput", "rb")
    content = pickle.load(file)
    

def face_tracking():
    
    return 0

def moving():
    
    return 0

def facial_expression():
    return 0

def main():
    while True:
        print("hello")
        #랜덤 난수 생성
        #행동 패턴 리스트로 저장
        pattern = ('angry', 'disgust', 'fear', 'happy', 'sad', 'surprise', 'neutral')
        
        #angry -> (화냄, 시선 회피, 울음)
        #disgust -> (궁금, 회피, 화냄)
        #fear -> (위로)
        #happy -> (웃음, 장난, 춤)
        #sad -> (위로, 울음)
        #surprise -> (궁금, 놀람)
        #neutral -> (장난, 심심, 졸음)
        #혼자 장난치는 패턴 여러개
        # webcam.webcam()
        face_position()
        
        
        time.sleep(0.1)
main()

