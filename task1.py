import cv2
from matplotlib import pyplot as plt

file = 'variant-3.jpeg'


def image_processing(file):
    img = cv2.imread(file)
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    plt.imshow(img_hsv)
    plt.axis('off')  
    plt.show()


if __name__ == '__main__':
    image_processing(file)

cv2.destroyAllWindows()