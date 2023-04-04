from easydict import EasyDict as edict

cfg = edict()
cfg.MODEL_NAME = "yolox-s"
cfg.MODEL_WEIGHTS = "pretrained_models/yolox/yolox_x.pth"
cfg.INP_DIM = 640
cfg.CONF_THRES = 0.1
cfg.NMS_THRES = 0.6
