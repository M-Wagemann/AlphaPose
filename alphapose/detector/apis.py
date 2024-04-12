# -----------------------------------------------------
# Copyright (c) Shanghai Jiao Tong University. All rights reserved.
# Written by Chao Xu (xuchao.19962007@sjtu.edu.cn)
# -----------------------------------------------------

"""API of detector"""
from abc import ABC, abstractmethod

default_yolocfg= {'CONFIG': 'configs/yolo/cfg/yolov3-spp.cfg', 'WEIGHTS': 'pretrained_models/yolo/yolov3-spp.weights', 
                  'INP_DIM': 608, 'NMS_THRES': 0.6, 'CONFIDENCE': 0.1, 'NUM_CLASSES': 80}

def get_detector(opt=None, yolocfg=default_yolocfg):
    if opt.detector == 'yolo':
        from alphapose.detector.yolo_api import YOLODetector
        return YOLODetector(yolocfg, opt)
    elif 'yolox' in opt.detector:
        from alphapose.detector.yolox_api import YOLOXDetector
        from alphapose.detector.yolox_cfg import cfg
        if opt.detector.lower() == 'yolox':
            opt.detector = 'yolox-x'
        cfg.MODEL_NAME = opt.detector.lower()
        cfg.MODEL_WEIGHTS = f'pretrained_models/yolox/{opt.detector.lower().replace("-", "_")}.pth'
        return YOLOXDetector(yolocfg, opt)
    elif opt.detector == 'tracker':
        from alphapose.detector.tracker_api import Tracker
        from alphapose.detector.tracker_cfg import cfg
        return Tracker(cfg, opt)
    elif opt.detector.startswith('efficientdet_d'):
        from alphapose.detector.effdet_api import EffDetDetector
        from alphapose.detector.effdet_cfg import cfg
        return EffDetDetector(cfg, opt)
    else:
        raise NotImplementedError


class BaseDetector(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def image_preprocess(self, img_name):
        pass

    @abstractmethod
    def images_detection(self, imgs, orig_dim_list):
        pass

    @abstractmethod
    def detect_one_img(self, img_name):
        pass
