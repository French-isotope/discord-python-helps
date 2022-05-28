import cv2
import numpy as np

def blueBGR(B,G,R):
    def inR(var, lB, rB):
        if var > lB and var <= rB:
            return True
        else:
            return False
    if inR(B, 150,255) and inR(G,70,170) and inR(R, 70,120):
        return True
    else:
        return False

def getCrop(mask,frame):
    # Eroding frame so there won't be any noise
    mask_Erode = cv2.erode(mask, (3,3), 1)

    #Creating bounding rectangle
        #Findig contours
    ret, thresh_img = cv2.threshold(mask_Erode, 100, 255, cv2.THRESH_BINARY)
    cont,_ = cv2.findContours(mask_Erode,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    p_Cont = min(cont, key=cv2.contourArea)
    x,y,width, height = cv2.boundingRect(p_Cont)

    #going left until hits the QR label

    counter = 0
    distance = 0
    x -= 100
    while True:
        cv2.circle(frame, (x, 5), 3, (0, 0, 255), 7)
        (b, g, r) = frame[40, x]
        if blueBGR(b, g, r) == False:
            x += 40
            break
        elif distance >= (1000-width)/2:
            break
        print("iter")
        x -= 30
        distance += 30
        counter += 1

    imCropped = frame[0: 775, int(x): int(x + 1000)]

    cv2.imshow("TEST", frame)
    cv2.imshow("TEST2", imCropped)
    cv2.waitKey(3500)

    #imCropped = cv2.resize(imCropped, (1000, 775))
    return imCropped


def cropPlants(path):                                       #outer function that returns tuple: (row_top_left, col_top_left, row_bottom_right, col_bottom_right)
    def getCrop(mask, frame):                               #inner function that does all the job
        # Eroding frame so there won't be any noise
        mask_Erode = cv2.erode(mask, (3, 3), 1)

        # finding most-left extremum point
        corners = cv2.goodFeaturesToTrack(mask_Erode, 50, 0.01, 10)
#        print(f'{corners}')
        cornerns = np.int0(corners)
        min_X = float("inf")
        for i in corners:
            x, y = i.ravel()
            # cv2.circle(frame, (int(x), int(y)), 3, (130, 70, 255), 7)
            if min_X > x:
                min_X = x

        # Moving x left until it hits QR label or iterates 11 times 11*30(330)px
        counter = 0
        distance = 0
        min_X -= 100
        while True:
            # cv2.circle(frame, (int(min_X), 40), 3, (0, 0, 255), 7)
            (b, g, r) = frame[40, int(min_X)]
            if r >= 140:                        # r > 140 if min_X reaches the label, since it contains only red and white colours
                # print("RRRstop")
                min_X += 40
                break
            elif distance >= 500:
                # print("DDDiststop")
                break
            elif counter == 11:
                # print("CCCounterstop")
                break
            else:
                min_X -= 30
                distance += 30
                counter += 1
        cv2.imshow("res", mask_Erode)

#        img = frame[0:775, int(min_X):int(min_X + 1000)]
#        cv2.imshow("res", img)
        return 0, int(min_X), int(0 + 775), int(min_X + 1000)

    video = cv2.VideoCapture(path)
    bgs = cv2.createBackgroundSubtractorMOG2(detectShadows=False)                    # Background Subtraction
    s_Frame = 7                                               # The frame I'm passing into 'getCrop()' function, it equals 7, because few first frames are not clearly detected
    for i in range(s_Frame + 1):
        ret,frame = video.read()
        if frame is None:
            return 0
        bgs_Mask = bgs.apply(frame)
        if i == s_Frame:
            return getCrop(bgs_Mask, frame)
    video.release()


if __name__ == '__main__':
    path = "Resources/2.MOV"
    cv2.imshow("T", cropPlants(path))
    # for i in range(7):
    #     path = "Resources/" + str(i + 1) + ".MOV"
    #     print(path, " ")
    #     cv2.imshow(str(i + 1),cropPlants(path))
    #     cv2.waitKey(1000)
    cv2.waitKey(0)