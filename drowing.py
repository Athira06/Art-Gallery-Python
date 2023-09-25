import cv2
import matplotlib.pyplot as plt
p=input("upload your image")
def drow():
        plt.style.use('seaborn')
        img = cv2.imread(p)
        img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        # plt.figure(figsize=(8,8))
        # plt.imshow(img)
        # plt.axis("off")
        # plt.title("Original Image")
        # # plt.show()
        #
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # plt.figure(figsize=(8,8))
        # plt.imshow(img_gray,cmap="gray")
        # plt.axis("off")
        # plt.title("GrayScale Image")
        # # plt.show()
        #
        img_invert = cv2.bitwise_not(img_gray)
        # # plt.figure(figsize=(8,8))
        # # plt.imshow(img_invert,cmap="gray")
        # # plt.axis("off")
        # # plt.title("Inverted Image")
        # # plt.show()
        # #
        img_smoothing = cv2.GaussianBlur(img_invert, (21, 21),sigmaX=0, sigmaY=0)
        # # plt.figure(figsize=(8,8))
        # # plt.imshow(img_smoothing,cmap="gray")
        # # plt.axis("off")
        # # plt.title("Smoothen Image")
        # # plt.show()

        final = cv2.divide(img_gray, 255 - img_smoothing, scale=255)
        plt.figure(figsize=(8,8))
        plt.imshow(final,cmap="gray")
        plt.axis("off")
        plt.title("Final Sketch Image")
        # plt.show()

        plt.figure(figsize=(20,20))
        plt.subplot(1,3,1)
        plt.imshow(img)
        plt.axis("off")
        plt.title("Original Image")

        plt.subplot(1,3,2)
        plt.imshow(img_gray,cmap="gray")
        plt.axis("off")
        plt.title("GrayScale Image")

        # plt.subplot(1,5,3)
        # plt.imshow(img_invert,cmap="gray")
        # plt.axis("off")
        # plt.title("Inverted Image")
        #
        # plt.subplot(1,5,4)
        # plt.imshow(img_smoothing,cmap="gray")
        # plt.axis("off")
        # plt.title("Smoothen Image")

        plt.subplot(1,3,3)
        plt.imshow(final,cmap="gray")
        plt.axis("off")
        plt.title("Final Sketch Image")
        plt.show()



drow()
x = input("press space and enter button to go home page")
from frnd import f
f()