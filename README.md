# matrix-python-imgprocessing-serial
Matrix Image Proccesing with Python to Serial

**Stable on python version : 3.7**

Required libs:
- opencv2 `cv2`
- numpy
- serial
- keyboard
- opencv-contrib-python

Default Camera Resolution `h : 640 x v : 360`
It can be change with 
```
h_px = 360
w_px = 640
```
Also, it can be replace with extarnal cam within change to `cap = cv2.VideoCapture(1)`

```
# Tracker Types
# tracker = cv2.TrackerBoosting_create()
# tracker = cv2.TrackerMIL_create()
# tracker = cv2.TrackerKCF_create()
# tracker = cv2.TrackerTLD_create()
# tracker = cv2.TrackerMedianFlow_create()
tracker = cv2.TrackerCSRT_create()
# tracker = cv2.TrackerMOSSE_create()
```


This gives output from serial ports by 3 seperated image areas.

**to change COM ports `ser = serial.Serial('COM5', 9600)`**

to change BaudRates : (default) **9600**

>***made by flurex***
