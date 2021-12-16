import cv2
import numpy as np


def color_hist(img):
    mask = np.zeros( img.shape[:2], dtype=np.uint8 )

    # 设置mask，处理中心部分图像
    mask[150:480, 500:940] = 255
    hsv = cv2.cvtColor( img, cv2.COLOR_BGR2HSV )

    # 计算直方图，求最大的分布

    hist_mask = cv2.calcHist( [hsv], [0], mask, [180], [0, 180] )
    object_H = np.where( hist_mask == np.max( hist_mask ) )
    print( object_H[0] )
    return object_H[0]



def color_distinguish(object_H):
    try:
        if object_H > 26 and object_H < 34:
            color = 'yellow'
        elif object_H > 156 and object_H < 180:
            color = 'red'
        elif object_H > 100 and object_H < 124:
            color = 'blue'
        elif object_H > 35 and object_H < 77:
            color = 'green'
        elif object_H > 78 and object_H < 99:
            color = 'cyan-blue'

        elif object_H > 6 and object_H < 15:
            color = 'orange'
        else:
            color = 'None'
        print( color )
        return color

    except:
        pass

if __name__ == '__main__':
    img = cv2.imread('/Users/user/Desktop/OpenCVtest.jpeg')
    img[150:480, 500:940] = [0, 255, 255] #手动增强
    object_H = color_hist( img )
    color_distinguish( object_H )- d    
    cv2.imshow( 'image', img )
    cv2.waitKey( 0 )