import cv2                                            # importing cv2 module to code

img_file = 'car1.jpeg'                               
classifier = "car_classifier.xml"                     # pre-trained car-classifier algorithm

img = cv2.imread(img_file)
print('Hello world')
