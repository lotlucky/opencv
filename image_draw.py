#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    : image_draw.py
# @Date    : 2019-03-14
# @Author  : wudan
import cv2
import numpy as np

#creat a black image
img = np.zeros((512,512,3), dtype=np.uint8)

#draw a diagonal blue line with thickness of 5 px
cv2.line(img, (0,0) ,(511,511),(255,0,0) ,5)

# draw a rectangle
cv2.rectangle(img,(384,0),(510,128),(0,255,0),3)

# draw a  circle
cv2.circle(img,(447,63),63,(0,0,255), 4)

# draw an ellipse
cv2.ellipse(img, (256,256),(100,50),0,0,1360,255,-1)

#draw a polygen
pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
pts = pts.reshape((-1,1,2))

# add a text
font  = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'OpenCV', (10,500),font,4,(255,255,255) ,3)

winname = 'example'
cv2.namedWindow(winname)
cv2.imshow(winname, img)
cv2.imwrite('example.jpg')
cv2.waitKey(0)

