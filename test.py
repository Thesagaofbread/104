import cv2
from operator import itemgetter

s= [('mercury',0), ('venus',1), ('earth',2) ,('mars',3), ('jupiter',4), ('saturn',5), ('uranus',6), ('neptune',7) ]

#itemgetter(0,7)(s)
getcount = itemgetter(1)
list(map(getcount, s))
sorted(s, key=getcount)
#[j for i in items for j in (i if isinstance(i, list) else [i])]

#can't figure out this part
