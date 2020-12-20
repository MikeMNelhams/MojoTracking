# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 20:57:55 2020

@author: Shane
"""
import cv2
import json
import numpy as np

#Load data (change path to json files)
with open(r"C:\Users\Shane\Desktop\Year 3\Mathematical and Data Modelling\Phase B\mojo_sperm_tracking_data_bristol\mojo_sperm_tracking_data_bristol\tp57\cover1_1_YOLO_NO_TRACKING_output\centroids_with_meta.json", "r") as read_file:
    data = json.load(read_file)
    
#Load video (change path to video)    
cap = cv2.VideoCapture(r"C:\Users\Shane\Desktop\Year 3\Mathematical and Data Modelling\Phase B\mojo_sperm_tracking_data_bristol\mojo_sperm_tracking_data_bristol\tp57\cover1_1.avi")


success,img = cap.read()

#Formatting and scaling bounding boxes
def drawBox(img,i):
    for j in range(0,len(data["centroids"][i])):
        bbox = tuple([x*data["extra_information"]["resize_factor"] for x in data["centroids"][i][j]["bbox"]])
        cv2.rectangle(img,(np.float32(bbox[0]),np.float32(bbox[1])),((np.float32(bbox[0]+bbox[2])),np.float32(bbox[1]+bbox[3])),(255,0,255),3,1)


i = 0 
#Displaying bounding box according to video frame       
while True:
    
    success,img = cap.read()
    drawBox(img,i)
    i +=1
    
    cv2.imshow("Tracking",img)
    
    if cv2.waitKey(1) & 0xff == ord("q"):
        break
    
cv2.destroyAllWindows()