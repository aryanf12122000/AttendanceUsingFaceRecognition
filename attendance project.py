import cv2
import os
import numpy as np
import face_recognition as fr
from datetime import datetime

path =r'C:\Users\AryanFernandes\Desktop\aryan\project-1\FR_PYCHARM\FR_PYCHARM\ImagesAttendance' #path where the images are stored
stdImages=[]
classNames=[]
myList=os.listdir(path)
print(myList)
for cl in myList:
    curImg=cv2.imread(f'{path}/{cl}')
    stdImages.append(curImg)
    classNames.append(os.path.splitext(cl)[0])
print(classNames)

def findEncodings(stdImages):
    encodeList=[]
    for img in stdImages:
        img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        encode=fr.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList

def markAttendance(name):
    with open(r'C:\Users\AryanFernandes\Desktop\aryan\project-1\FR_PYCHARM\FR_PYCHARM/Attendance.csv','r+') as f: #path for csv file
        myDataList=f.readlines()
        nameList= []
        for line in myDataList:
            entry=line.split(",")
            nameList.append(entry[0])
        if name not in nameList:
            now=datetime.now()
            tmString=now.strftime('%H:%M:%S')
            dtString = now.strftime('%d:%m:%Y')
            f.writelines(f'\n,{name},{tmString},{dtString}')


encodeListKnown=findEncodings(stdImages)
#print(len(encodeListKnown))
print('encoding complete')

video=cv2.VideoCapture(0)

while True:
    check,img=video.read()
    imgS=cv2.resize(img,(0,0),None,0.25,0.25)
    imgS=cv2.cvtColor(imgS,cv2.COLOR_BGR2RGB)

    facesCurFrame = fr.face_locations(imgS)
    encodeCurFrame = fr.face_encodings(imgS,facesCurFrame)

    for encodeFace,faceLoc in zip( encodeCurFrame, facesCurFrame):
        matches=fr.compare_faces(encodeListKnown,encodeFace)
        faceDis=fr.face_distance(encodeListKnown,encodeFace)
        #print(faceDis)
        matchIndex=np.argmin(faceDis)

        if matches[matchIndex]:
            name=classNames[matchIndex].upper()
            #print(name)
            y1,x2,y2,x1=faceLoc
            y1,x2,y2,x1= y1*4,x2*4,y2*4,x1*4
            cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
            cv2.rectangle(img,(x1,y2-20),(x2,y2),(0,255,0),cv2.FILLED)
            cv2.putText(img,name,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,0.55,(255,255,255),2)

            markAttendance(name)


    cv2.imshow('webcam',img)
    if cv2.waitKey(1)==ord('x'):
       break