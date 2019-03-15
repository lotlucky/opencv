#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    : image_read.py
# @Date    : 2019-03-11
# @Author  : wudan
import cv2

img = cv2.imread('zhuzhu.jpg',1)
cv2.imshow('image',img)
k = cv2.waitKey(0)

if k ==27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('zhuzhu_best.png',img)







