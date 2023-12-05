# Tennis Court Detector with Yolov8

## Background
Inspired by https://github.com/yastrebksv/TennisCourtDetector. Dataset can be found at this github. The goal is to see the performance of YoloV8 at the same task.

![](images/output3.png)

## Environment
```
Python 3.11.
torch 2.1.1
```

Training was done on Tesla V100-PCIE-16GB GPU for the upload `model.py`.

## Running
1. First download dataset and move to `datasets/` folder.
2. Run `convert_to_yolo.ipynb` to convert to coco8, the format supported by YOLOv8 ultralytics.
3. Run `python train.py`.


## Performance
We trained with `yolov8s-pose.pt` base model. The training results and visualizing methods of the dataset can be found in `evaluate.ipynb`.

### Epoch 10, Batch Size 16, Imgsz 640
```
Training time: 695.83 seconds




```



## Extra
![](images/output1.png)