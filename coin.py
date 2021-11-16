import numpy as np
import cv2

def run_main():

        img = cv2.imread('forint.jpg')
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        gray_blur = cv2.GaussianBlur(gray, (15, 15), 0)
            
        circles = cv2.HoughCircles(gray_blur,cv2.HOUGH_GRADIENT,1,50, param1=100,param2=50,minRadius=50,maxRadius=120)
        circles = np.uint16(np.around(circles))
        largestRadius = 0
        for i in circles[0,:]:
            if largestRadius < i[2]:
                largestRadius = i[2]
        #print(largestRadius)
        print("Érmék:")
        change = 0
        for i in circles[0,:]:
                cv2.circle(img,(i[0],i[1]),i[2],(0,255,0),2)
                cv2.circle(img, (i[0], i[1]),2, (0,0,255), 3)
                radius = i[2]
                ratio = ((radius*radius) / (largestRadius*largestRadius))
                tolerance=0.09
                if(ratio >= (27.4/28.3)):
                    change = change + 200
                    print(200)
                elif((ratio >=(26.3/28.3)) and (ratio<=(27.4/28.3))):
                    change = change + 50
                    print(50)
                elif((ratio >= (24.8/28.3)-tolerance) and (ratio<(26.3/28.3))):
                    change = change + 20
                    print(20)
                elif((ratio >= (23.8/28.3)-tolerance) and (ratio<(24.8/28.3)-tolerance)):
                    change = change + 10
                    print(10)
                elif((ratio >= (21.5/28.3)-tolerance) and (ratio<(23.8/28.3)-tolerance)):
                    change = change + 100
                    print(100)
                elif(ratio < (21.5/28.3)-tolerance):
                    change = change + 5
                    print(5)
        print("Összeg :", change, " Ft")
        font = cv2.FONT_HERSHEY_SIMPLEX
        text = "Total value: " + str("%.2f" % round(change,2)) + " forint"
        cv2.putText(img, text, (0,400), font, 0.5, (0, 0, 255), 2, cv2.LINE_AA)
        cv2.imshow('Detected coins',img)
        cv2.waitKey()


if __name__ == "__main__":
    run_main()