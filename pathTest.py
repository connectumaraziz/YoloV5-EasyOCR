import glob
import os
import cv2
import easyocr
import csv

files = glob.glob('yolov5/runs/detect/exp/crops/**/*.jpg')
reader = easyocr.Reader(['en'], gpu=False)
OCR = []
DIR = []
for f in files:
    img = cv2.imread(f)
    result = reader.readtext(img, detail=0)
    dir_path = os.path.dirname(os.path.abspath(f))
    b = os.path.basename(dir_path)
    # print(b, ' is: ', result)
    OCR.append(result)
    DIR.append(b)
print(DIR)
print(OCR)
with open('GFG.csv', 'w') as f:
    # using csv.writer method from CSV package
    write = csv.writer(f)
    write.writerow(DIR)
    write.writerow(OCR)


# Directory name
directory = "exp"

# Parent Directory
parent = "yolov5/runs/detect/"

# Path
path = os.path.join(parent, directory)
import shutil

shutil.rmtree(path)
# try:
#     os.rmdir(path)
print("Directory '% s' has been removed successfully" % directory)
# except OSError as error:
#     print(error)
#     print("Directory '% s' can not be removed" % directory)


