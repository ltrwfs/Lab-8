import numpy as np
import cv2

# Вариант №3

def video_processing():
    cap = cv2.VideoCapture(0)
    fly = cv2.imread('fly64.png', cv2.IMREAD_UNCHANGED)
    fly = cv2.resize(fly, (50, 50))
    fly_colors = cv2.split(fly)
    alpha = fly_colors[3] / 255.0

    while True:
        no_errors, frame = cap.read()
        if not no_errors:
            break
        height, width = frame.shape[:2] 
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
        gray = cv2.GaussianBlur(gray, (15, 15), 0)
        
        cv2.rectangle(frame, (width//2 - 100, height//2 - 100),
                      (width//2 + 100, height//2 + 100), (255, 0, 0), 1)
        
        circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT_ALT, 1.5, 100,
                                   param1=300, param2=0.8,
                                   minRadius=0, maxRadius=0)
        if circles is not None:
            circles = np.uint16(np.around(circles)) 
            x, y, r = circles[0, 0] 
            cv2.circle(frame, (x, y), r, (0, 0, 255), 3)
            cv2.circle(frame, (x, y), 2, (0, 255, 0), 3)
            
            # Проверка условия попадания центра метки в квадрат 200х200
            if (width/2-100<x<width/2+100) & (height/2-100<y<height/2+100):
                print(f'Попадание метки: True')
            else:
                print(f'Попадание метки: False')

            # Размещение мухи
            fly_zone = frame[(y-25):(y+25), (x-25):(x+25)]
            for c in range(3):
                fly_zone[:, :, c] = (alpha * fly_colors[c]
                                     + (1 - alpha) * fly_zone[:, :, c])
        
        cv2.imshow('', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    video_processing()