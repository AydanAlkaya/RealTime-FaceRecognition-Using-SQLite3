import cv2
import numpy as np
import sqlite3

faceDetect=cv2.CascadeClassifier('haarcascade_frontalface_default.xml');
cam=cv2.VideoCapture(0);

def insertOrUpdate(Id,Name,Age):
    conn=sqlite3.connect("sqlite.db")
    cmd="SELECT * FROM STUDENTS WHERE ID="+str(Id);
    cursor=conn.execute(cmd);
    isRecordExist=0;
    if (isRecordExist == 1):
        conn.execute("UPDATE STUDENTS SET Name=? WHERE id=?", (Name, Id,))
        conn.execute("UPDATE STUDENTS SET Age=? WHERE id=?", (Age, Id))
    else:
        conn.execute("INSERT INTO STUDENTS(id,Name,Age) Values(?,?,?)", (Id, Name, Age))
    conn.commit()
    conn.close()
Id=input('Enter User Id:')
Name=input('Enter User Name:')
Age=input('Enter User Age:')

insertOrUpdate(Id,Name,Age)
sampleNum=0
while(True):
    ret,img=cam.read();
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=faceDetect.detectMultiScale(gray,1.3,5);
    for(x,y,w,h) in faces:
        sampleNum=sampleNum+1;
        cv2.imwrite("dataset/User."+str(Id)+"."+str(sampleNum)+".jpg",gray[y:y+h,x:x+w])
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        cv2.waitKey(100);
    cv2.imshow("Face",img);
    cv2.waitKey(1);
    if(sampleNum>30):
        break;
cam.release()
cv2.destroyAllWindows()