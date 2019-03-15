#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    : image_mouse_draw.py
# @Date    : 2019-03-14
# @Author  : wudan

import cv2
import numpy as np


# 鼠标按下时变为true
drawing = False
# 如果mode为True 绘制矩形，mode为false 绘制曲线
# 按下‘m’ 键，mode为False
mode  = True
ix, iy = -1, -1

# 创建回调函数
def draw_circle(event,x,y,flags,param):
    global ix,iy,drawing,mode
# 当按下左键 返回起始位置坐标, 捕获第一次按下左键的坐标
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y
# 鼠标左键长安并且移动 为绘制，按键‘m’用来切换绘制矩形或者直线
    elif event == cv2.EVENT_MOUSEMOVE and flags == cv2.EVENT_FLAG_LBUTTON:
        if drawing is True:
            if mode is True:
                cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
            else:
                cv2.circle(img,(x,y),3,(0,0,255),-1)
# 鼠标左键放开，则认为绘制结束
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False


img = np.zeros((512, 512, 3), np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_circle)
while True :
    cv2.imshow('image', img)
    k = cv2.waitKey(1)&0xFF
    if k == ord('m'):
        mode = not mode
    elif k == 27:
        break



