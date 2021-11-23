import numpy as np
import cv2

def sum(kep):

        ermek={"5 HUF": {
            "value": 5,
            "radius": 21.5,
            "ratio": 21.5/28.3,
            "count": 0,
        },
        "10 HUF": {
            "value": 10,
            "radius": 24.8,
            "ratio": 24.8/28.3,
            "count": 0,
        },
        "20 HUF": {
            "value": 20,
            "radius": 26.3,
            "ratio": 26.3/28.3,
            "count": 0,
        },
        "50 HUF": {
            "value": 50,
            "radius": 27.4,
            "ratio": 27.4/28.3,
            "count": 0,
        },
        "100 HUF": {
            "value": 100,
            "radius": 23.8,
            "ratio": 23.8/28.3,
            "count": 0,
        },
        "200 HUF": {
            "value": 200,
            "radius": 28.3,
            "ratio": 28.3/28.3,
            "count": 0,
        }}
        img = cv2.imread(kep)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        gray_blur = cv2.GaussianBlur(gray, (15, 15), 0)
            
        circles = cv2.HoughCircles(gray_blur,cv2.HOUGH_GRADIENT,1,50, param1=100,param2=50,minRadius=50,maxRadius=120)
        circles = np.uint16(np.around(circles))
        largestRadius = 0
        for i in circles[0,:]:
            if largestRadius < i[2]:
                largestRadius = i[2]
        #print(largestRadius)
        change = 0
        for i in circles[0,:]:
                cv2.circle(img,(i[0],i[1]),i[2],(0,255,0),2)
                cv2.circle(img, (i[0], i[1]),2, (0,0,255), 3)
                radius = i[2]
                ratio = ((radius*radius) / (largestRadius*largestRadius))
                tolerance=0.09
                if(ratio >= (ermek["50 HUF"]['ratio'])):
                    change = change + ermek["200 HUF"]['value']
                    ermek["200 HUF"]['count']+=1
                elif((ratio >=(ermek["20 HUF"]['ratio'])) and (ratio<=(ermek["50 HUF"]['ratio']))):
                    change = change + ermek["50 HUF"]['value']
                    ermek["50 HUF"]['count']+=1
                elif((ratio >= (ermek["10 HUF"]['ratio'])-tolerance) and (ratio<(ermek["20 HUF"]['ratio']))):
                    change = change + ermek["20 HUF"]['value']
                    ermek["20 HUF"]['count']+=1
                elif((ratio >= (ermek["100 HUF"]['ratio'])-tolerance) and (ratio<(ermek["10 HUF"]['ratio'])-tolerance)):
                    change = change + ermek["10 HUF"]['value']
                    ermek["10 HUF"]['count']+=1
                elif((ratio >= (ermek["5 HUF"]['ratio'])-tolerance) and (ratio<(ermek["100 HUF"]['ratio'])-tolerance)):
                    change = change + ermek["100 HUF"]['value']
                    ermek["100 HUF"]['count']+=1
                elif(ratio < (ermek["5 HUF"]['ratio'])-tolerance):
                    change = change + ermek["5 HUF"]['value']
                    ermek["5 HUF"]['count']+=1
        print("Összeg :", change, " Ft")
        print("Képen található érmék darabszám szerint:")
        for erme in ermek:
            darabszam = ermek[erme]['count']
            print(f"{erme} = {darabszam} db")
        print()
        font = cv2.FONT_HERSHEY_SIMPLEX
        text = "Osszertek: " + str("%.2f" % round(change,2)) + " forint"
        cv2.putText(img, text, (0,400), font, 1, (255, 255, 255), 2, cv2.LINE_AA)
        cv2.imshow('Detected coins',img)
        cv2.waitKey()

def run_main():
    sum('forint.jpg')
    sum('kep.jpg')
    sum('kep1.jpg')
    sum('kep2.jpg')

if __name__ == "__main__":
    run_main()