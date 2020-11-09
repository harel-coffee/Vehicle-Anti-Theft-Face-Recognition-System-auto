import sys
import os
import math
import cv2


label = "Feier_Zhang"
num_cap = 20

path = sys.path[0]+'/Facial_images/face_rec/train/'+label


folder = os.path.exists(path)

if not folder:
	os.makedirs(path)


cap = cv2.VideoCapture(1)
c=0                        
while(c < num_cap):
    
    ret, frame = cap.read()
   
    cv2.imshow("capture", frame)

    cv2.imwrite(path+'/'+str(c) + '.jpg', frame) 

    c=c+1
    cv2.waitKey(500)

cap.release()
cv2.destroyAllWindows()