# Star Cluster Detection and Classification

Pytorch code for the detection and classification of star clusters from images of the HST. The target galaxies used in this project are listed in 'targets.txt'. 

## Getting started

### Prerequisites

This code runs on Ubuntu.

Install [ImageMagick](http://apt.ubuntu.com/p/imagemagick) to convert pdf files to images.

If ```convert-im6.q16: not authorized `myfile.pdf' @ error/constitute.c/(WriteImage or ReadImage)``` error is encountered, you need to eliminate usage restrictions from the ImageMagick ```policy.xml``` file. To do so run:

```
sudo mv /etc/ImageMagick-6/policy.xml /etc/ImageMagick-6/policy.xmlout
```
To revert to the original situation, just rename back to the original name:
```
sudo mv /etc/ImageMagick-6/policy.xmlout /etc/ImageMagick-6/policy.xml 
```

sudo apt-get install python-pip
```pip Install Pillow```
github repository python-ocr: https://github.com/schollz/python-ocr
install opencv: https://stackoverflow.com/questions/19876079/cannot-find-module-cv2-when-using-opencv
Change ```import Image``` with ```from PIL import Image``` in extract_text.py.
pip install pytesseract

This code was implemented in Python 2.7.*.

### Instructions

Save pdf files in ./pdfs folder. Run run.sh.

### Download dataset

The dataset used is provided by the [Legacy ExtraGalactic UV Survey (LEGUS)](https://archive.stsci.edu/prepds/legus/). To download the dataset run:

```
./download_dataset.sh
```

### Create dataset files

Candidates listed in CAT files of each target are detected using SExtractor. To create dataset of candidate slices run:

```
./create_dataset.sh
```

Slice size, compensate filter gain, and remove background light options are defined in 'create_dataset.sh':

```
SIZE=${1:-32}
GAIN=${2:-0}
BACKLIGHT=${3:-0}

python src/create_object_slices.py \
                   --slice-size $SIZE \
                   --gain-inv $GAIN \
                   --remove-back-light $BACKLIGHT \

python src/create_trainval_db.py \
                   --slice-size $SIZE \
                   --gain-inv $GAIN \
                   --remove-back-light $BACKLIGHT \
                   --split 80 \
```

* inst: identifier for instrument used to acquire data.
* filter: element selected from filter wheel (uv:F275W, u:F336W, b:F438W, v:F555W, i:F814W).
* version: which version of the catalog do you want to use (i.e.: v1 or v2).
* slice-size: 'window size for visualization (slice size: sz x sz).


