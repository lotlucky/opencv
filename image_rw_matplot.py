#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    : image_rw_matplot.py
# @Date    : 2019-03-14
# @Author  : wudan
import cv2
import numpy as pd
from matplotlib import pyplot as plt
"""
CV2处理图像使用的是BGR模式，而matplotlib使用的是RGB模式
"""


img = cv2.imread('zhuzhu_1.jpeg',1)
b,g,r = cv2.split(img)
img2 = cv2.merge([r,g,b])

plt.subplot(121),plt.imshow(img)   #颜色有失真
plt.subplot(122),plt.imshow(img2)  #颜色正常
plt.show()


