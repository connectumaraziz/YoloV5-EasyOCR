# YoloV5-EasyOCR
![YoloV5+OCR](https://github.com/connectumaraziz/YoloV5-EasyOCR/blob/main/Untitled%20design.png?raw=true)<br>
In this project the model is built in order to get detect ID card and scrap required information into Excel, CSV, or JSON file formate.<br>
## Step: 1
Create detection model with specified labels that required to scrap.
For more visit and clone [YoloV5 Official Repo](https://github.com/ultralytics/yolov5)
## Step: 2
After Training the model, weight file "best.pt" should save locally.
## Step:3
Give the input image path and weight file path in "runALL.py" in source section and weight section respectively.<br>
like
```
os.system('python yolov5/detect.py --weights best.pt --source [Path to input Image] --conf 0.5 --save-crop')
```

## Step:4
run "runALL.py" <br>
# Note <br>
> This project use only 100 images to train and have medium accuracy. you can use 1000 images per class in order to get better accuracy,
> The blur images in exp folder is credential data of person.
