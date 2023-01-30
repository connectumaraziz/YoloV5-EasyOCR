import os

os.system('python yolov5/detect.py --weights best.pt --source [Path to input Image] --conf 0.5 --save-crop')
os.system('python pathTest.py')
