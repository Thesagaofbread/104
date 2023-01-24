import cv2

pic = cv2.imread('c:/Users/livcr/OneDrive/Pictures/projects/104/solar-system.jpg')

d = ['mercury', 'venus', 'earth','mars', 'jupiter','saturn', 'uranus', 'neptune' ]
x = 0

cv2.putText( pic, "sun", (0,300), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0,255,255))
cv2.putText( pic, "mercury", (100,300), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,0,255))
cv2.putText( pic, "venus", (200,300), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,0,255))
cv2.putText( pic, "earth", (300,300), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,0,255))
cv2.putText( pic, "mars", (400,300), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,0,255))
cv2.putText( pic, "jupiter", (550,300), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,0,255))
cv2.putText( pic, "saturn", (850,300), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,0,255))
cv2.putText( pic, "uranus", (1000,300), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,0,255))
cv2.putText( pic, "neptune", (1100,300), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,0,255))

cv2.imshow('output',pic)

cv2.waitKey(0)











