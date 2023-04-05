import cv2
from cvzone.FaceDetectionModule import FaceDetector
from cvzone.HandTrackingModule import HandDetector
import os
import cvzone
fps = cvzone.FPS()
import time

 
wCam, hCam = 640, 480
 
cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)
###############
import pyttsx3
from playsound import playsound

# Create an instance of the pyttsx3 engine
engine = pyttsx3.init()

# Set the voice properties (optional)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # change index to change voice

text = "Application is started"

# Speak the text
engine.say(text)
engine.runAndWait()
##############

hd = HandDetector(detectionCon=0.5)


overlaylist=[]
folderpath = 'F'
list = os.listdir(folderpath)
print(folderpath)
for imgpath in list:
    image = cv2.imread(f'{folderpath}/{imgpath}')
    overlaylist.append(image)

check = []
a,b,c,d,e,f,g= True,True,True,True,True,True,True
while True:
    _, img = cap.read()
    #fps.update(img,pos=(490,40),scale=2,color=(0,0,255))
    hand,imgs = hd.findHands(img)
    if hand:
        lefthand = hand[0]
        bbox = lefthand["bbox"]
        lmlist = lefthand['lmList']
        handtype = lefthand['type']
        fingersup = hd.fingersUp(lefthand)
        totalfingers = fingersup.count(1)
        h, w, c = overlaylist[totalfingers - 1].shape
        img[0:h, 0:w] = overlaylist[totalfingers - 1]
        
        
        #cv2.rectangle(img, (0, 200), (170, 425), (0, 0, 255), cv2.FILLED)
        #cv2.putText(img, str(totalfingers), (45, 375), cv2.FONT_HERSHEY_PLAIN, 9, (255, 0, 0), 24)
        
        if totalfingers==0 and g==True:
            check.append(totalfingers)
            if len(check)>20:
                g=False
                
                text = "I need to talk"

                # Speak the text
                # engine.say(text)
                # engine.runAndWait()
                audio_file = "6.mp3"

                # Play the audio file
                playsound(audio_file)
                time.sleep(0.2)
                check.clear()
        if totalfingers==1 and a==True:
            check.append(totalfingers)
            if len(check)>20:
                a=False
                
                text = "Hello"

                # Speak the text
                audio_file = "1.mp3"

                # Play the audio file
                playsound(audio_file)
                time.sleep(0.2)
                check.clear()
        if totalfingers==2 and b==True:
            check.append(totalfingers)
            if len(check)>20:
                b=False
                
                text = "pingo"

                # Speak the text
                audio_file = "2.mp3"

                # Play the audio file
                playsound(audio_file)
                time.sleep(0.2)
                check.clear()
        if totalfingers==4 and d==True:
            check.append(totalfingers)
            if len(check)>20:
                d=False
                
                text = "GOOO gOOOOO"

                audio_file = "4.mp3"

                # Play the audio file
                playsound(audio_file)
                time.sleep(0.2)
                check.clear()
        if totalfingers==5 and e==True:
            check.append(totalfingers)
            if len(check)>20:
                e=False
                
                text = "PONKAAAAAA"

                audio_file = "5.mp3"

                # Play the audio file
                playsound(audio_file)
                time.sleep(0.2)
                check.clear()
        if totalfingers==6 and f==True:
            check.append(totalfingers)
            if len(check)>20:
                f=False
                
                text = "GARAAAKK"

                audio_file = "6.mp3"

                # Play the audio file
                playsound(audio_file)
                time.sleep(0.2)
                check.clear()
        if totalfingers==3 and g==True:
            check.append(totalfingers)
            if len(check)>20:
                g=False
                
                text = "JAJAlaAAAAAA"

                audio_file = "3.mp3"

                # Play the audio file
                playsound(audio_file)
                time.sleep(0.2)
                check.clear()
        # if totalfingers==1 and a==True:
        #     a=False
            
        #     text = "I am feeling hungry"

        #     # Speak the text
        #     engine.say(text)
        #     engine.runAndWait()
        # if totalfingers==2 and b==True:
        #     b=False
            
        #     text = "I need help"

        #     # Speak the text
        #     engine.say(text)
        #     engine.runAndWait()
        # if totalfingers==3 and c==True:
        #     c=False
            
        #     text = "I want water"

        #     # Speak the text
        #     engine.say(text)
        #     engine.runAndWait()
        # if totalfingers==4 and d==True:
        #     d=False
            
        #     text = "I am not feeling well"

        #     # Speak the text
        #     engine.say(text)
        #     engine.runAndWait()
        # if totalfingers==5 and e==True:
        #     e=False
            
        #     text = "I have to rest"

        #     # Speak the text
        #     engine.say(text)
        #     engine.runAndWait()
        # if totalfingers==6 and f==True:
        #     f=False
            
        #     text = "I need to talk"

        #     # Speak the text
        #     engine.say(text)
        #     engine.runAndWait()
       
        print(totalfingers)




    cv2.imshow('FRAME',img)
    key = cv2.waitKey(1)
    if key == 27:
        break
cap.release()
cv2.destroyAllWindows()