import cv2
import numpy as np


def detect_shapes(image_path):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    edges = cv2.Canny(blurred, 50, 150)
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        epsilon = 0.02 * cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, epsilon, True)
        vertices = len(approx)
        shape = "unknown"
        if vertices == 3:
            shape = "triangle"
        elif vertices == 4:
            x, y, w, h = cv2.boundingRect(approx)
            aspect_ratio = float(w) / h
            shape = "square" if 0.95 <= aspect_ratio <= 1.05 else "rectangle"
        elif vertices == 5:
            shape = "pentagon"
        elif vertices == 6:
            shape = "hexagon"
        elif vertices == 7:
            shape = "heptagon"
        elif vertices == 8:
            shape = "octagon"
        elif vertices == 9:
            shape = "nonagon"
        elif vertices == 10:
            shape = "decaagon"
        else:
            area = cv2.contourArea(contour)
            perimeter = cv2.arcLength(contour, True)
            if area < 100:
                continue
            circularity = (4 * np.pi * area) / (perimeter * perimeter)
            if circularity > 0.05:
                shape = "circle"
        M = cv2.moments(contour)
        if M["m00"] != 0:
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
            cv2.drawContours(image, [approx], 0, (0, 255, 0), 1)
            cv2.putText(image, shape, (cX, cY), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
    cv2.imshow("Shape Detection", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


image_path = input("Enter the path of the input image: ")
detect_shapes(image_path)
