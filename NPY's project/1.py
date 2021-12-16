import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(1):
    # 截取图像
    ret,frame = cap.read()

    #转换到HSV
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    #设定阀值
    #需要调参数来判断
    lower = np.array( [0, 0, 0] )
    upper = np.array( [180, 255, 255] )
    lower_y = np.array([11,43,46])
    upper_y = np.array([16,255,255])
    lower_g = np.array( [35, 43, 46] )
    upper_g = np.array( [77, 255, 255] )
    lower_b = np.array( [100, 43, 46] )
    upper_b = np.array( [124, 255, 255] )


    #构建mask
    mask = cv2.inRange( hsv, lower, upper )
    mask1 = cv2.inRange(hsv,lower_y,upper_y)
    mask2 = cv2.inRange( hsv, lower_g, upper_g )
    mask3 = cv2.inRange( hsv, lower_b, upper_b )

    #对原图和掩模进行位运算
    res = cv2.bitwise_and(frame,frame,mask=mask)
    res1 = cv2.bitwise_and(frame,frame,mask=mask1)
    res2 = cv2.bitwise_and(frame,frame,mask=mask2)
    res3 = cv2.bitwise_and( frame, frame, mask=mask3 )

    # 图像叠加 alpha =0。5
    temp_result = cv2.addWeighted( res1, 1, res3, 1, 0 ) # 蓝色和橘色
    result = cv2.addWeighted( res2, 1, temp_result, 1, 0 ) #绿蓝黄
    # cv2.namedWindow("merge")
    # cv2.imshow("merge", imdst)

    #显示图像
    cv2.imshow('frame',frame) #窗口

    cv2.imshow('result',result) #处理完的图像

    k = cv2.waitKey(5)&0xFF
    if k == 27:
        break

cv2.destroyAllWindows()