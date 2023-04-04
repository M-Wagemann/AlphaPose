## Installation

### Requirements
* Nvidia device with CUDA, [example for Ubuntu 20.04](https://linuxconfig.org/how-to-install-cuda-on-ubuntu-20-04-focal-fossa-linux)
(if you have no nvidia device, delete [this line](https://github.com/MVIG-SJTU/AlphaPose/blob/master/setup.py#L211) from setup.py
* Python 3.7+
* Cython
* PyTorch 1.11+, for users who want to use 1.5 < PyTorch < 1.11, please switch to the `pytorch<1.11` branch by:
  `git checkout "pytorch<1.11"`; for users who want to use PyTorch < 1.5, please switch to the `pytorch<1.5` branch by: `git checkout "pytorch<1.5"`
* torchvision 0.12.0+
* numpy 
* python-package setuptools >= 40.0, reported by [this issue](https://github.com/MVIG-SJTU/AlphaPose/issues/838)
* Linux

### Code installation


#### Install with pip
```shell

# 0. Create install directory
mkdir install
export PYTHONUSERBASE=`pwd`/install

# 1. Install Cuda 11
wget https://developer.download.nvidia.com/compute/cuda/11.6.2/local_installers/cuda_11.6.2_510.47.03_linux.run -O cuda.run
chmod +x cuda.run
./cuda.run --silent --toolkitpath=${PYTHONUSERBASE} --toolkit --override --defaultroot=${PYTHONUSERBASE} --no-man-page 

# 2. Install PyTorch
mkdir build
pip3 install torch torchvision --extra-index-url https://download.pytorch.org/whl/cu116

# 3. Get AlphaPose
git clone https://github.com/MVIG-SJTU/AlphaPose.git
cd AlphaPose

# 4. Install
export PATH=${PYTHONUSERBASE}/bin/:$PATH
export LD_LIBRARY_PATH=${PYTHONUSERBASE}/lib64/:$LD_LIBRARY_PATH
pip install cython
pip install .

```

### Models
1. Download the object detection model manually: **yolov3-spp.weights**([Google Drive](https://drive.google.com/open?id=1D47msNOOiJKvPOXlnpyzdKA3k6E97NTC) | [Baidu pan](https://pan.baidu.com/s/1Zb2REEIk8tcahDa8KacPNA)). Place it into `pretrained_models/yolo/`.
2. (Optional) If you want to use [YOLOX](https://github.com/Megvii-BaseDetection/YOLOX) as the detector, you can download the weights [here](https://github.com/Megvii-BaseDetection/YOLOX), and place them into `pretrained_models/yolox`. We recommend [yolox-l](https://github.com/Megvii-BaseDetection/YOLOX/releases/download/0.1.1rc0/yolox_l.pth) and [yolox-x](https://github.com/Megvii-BaseDetection/YOLOX/releases/download/0.1.1rc0/yolox_x.pth).
3. Download our pose models. Place them into `pretrained_models`. All models and details are available in our [Model Zoo](./MODEL_ZOO.md).
2. For pose tracking, please refer to our [tracking docments](../alphapose/trackers) for model download



### Prepare dataset (optional)

#### MSCOCO
If you want to train the model by yourself, please download data from [MSCOCO](http://cocodataset.org/#download) (train2017 and val2017). Download and extract them under `./data`, and make them look like this:
```
|-- json
|-- exp
|-- alphapose
|-- configs
|-- test
|-- data
`-- |-- coco
    `-- |-- annotations
        |   |-- person_keypoints_train2017.json
        |   `-- person_keypoints_val2017.json
        |-- train2017
        |   |-- 000000000009.jpg
        |   |-- 000000000025.jpg
        |   |-- 000000000030.jpg
        |   |-- ... 
        `-- val2017
            |-- 000000000139.jpg
            |-- 000000000285.jpg
            |-- 000000000632.jpg
            |-- ... 
```

#### MPII
Please download images from [MPII](http://human-pose.mpi-inf.mpg.de/#download). We also provide the annotations in json format [[annot_mpii.zip](https://drive.google.com/open?id=1HC6znReBeg-TMPZbmoldtYrMGlrEFamh)]. 
Download and extract them under `./data`, and make them look like this:
```
|-- data
`-- |-- mpii
    `-- |-- annot_mpii.json
        `-- images
            |-- 027457270.jpg
            |-- 036645665.jpg
            |-- 045572740.jpg
            |-- ... 
```

#### Halpe-FullBody
If you want to train the model by yourself, please download data from [Halpe-FullBody](https://github.com/Fang-Haoshu/Halpe-FullBody). Download and extract them under `./data`, and make them look like this:
```
|-- json
|-- exp
|-- alphapose
|-- configs
|-- test
|-- data
`-- |-- halpe
    `-- |-- annotations
        |   |-- halpe_train_v1.json
        |   `-- halpe_val_v1.json
        |-- images
        `-- |-- train2015
             |   |-- HICO_train2015_00000001.jpg
             |   |-- HICO_train2015_00000002.jpg
             |   |-- HICO_train2015_00000003.jpg
             |   |-- ... 
             `-- val2017
                 |-- 000000000139.jpg
                 |-- 000000000285.jpg
                 |-- 000000000632.jpg
                 |-- ... 
```
