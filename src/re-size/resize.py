from PIL import Image
import os

source_folder = 'C:/Users/User/Documents/research/c/abbasii'
destination_folder = 'C:/Users/User/Documents/research/anticlinal_wall_classification/resize/a.macrochaetum/'
directory = os.listdir(source_folder)

for item in directory:
    img = Image.open(source_folder + item)
    imgResize = img.resize((150, 150), Image.ANTIALIAS)
    imgResize.save(destination_folder + item[:-4] + '.tif', quality=90)


#
# import cv2
# import glob
# import os
#
# inputFolder = 'C:/Users/User/Documents/research/anticlinal_wall_classification/cropped/a.macrochaetum'
# os.mkdir('C:/Users/User/Documents/research/anticlinal_wall_classification/resize/a.macrochaetum')
#
# i=0
#
# for img in glob.glob(inputFolder + "/*.PNG"):
#     image = cv2.imread(img)
#     imgResized = cv2.resize(image, (150, 150))
#     cv2.imwrite("Resized Folder/image%04i.jpg" %i, imgResized)
#
#     i +=1
#     #cv2.imshow('image', imgResized)
#     #cv2.waitKey(30)
#
# cv2.destroyAllWindos()