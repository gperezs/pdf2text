# PDF to TXT conversion

Pytorch code for the conversion of news PDF files to TXT files. PDF files are converted to images, pre-processed, and then converted to text using [tesseract](https://github.com/tesseract-ocr).  

## Getting started

### Prerequisites

This code runs on Linux. The code was implemented in Python 2.7.*.

#### PDF to image conversion:
Install [ImageMagick](http://apt.ubuntu.com/p/imagemagick) to convert pdf files to images.

If ```convert-im6.q16: not authorized `myfile.pdf' @ error/constitute.c/(WriteImage or ReadImage)``` error is encountered, you need to eliminate usage restrictions from the ImageMagick ```policy.xml``` file. To do so run:

```
sudo mv /etc/ImageMagick-6/policy.xml /etc/ImageMagick-6/policy.xmlout
```
To revert to the original situation, just rename back to the original name:
```
sudo mv /etc/ImageMagick-6/policy.xmlout /etc/ImageMagick-6/policy.xml 
```

#### Image to text conversion:
Install pip ```sudo apt-get install python-pip```.
Install Pillow ```pip Install Pillow```.
Install OpenCV with pip ```pip install opencv-python``` or with conda ```conda install opencv```.
If ```ImportError: No module named cv2``` is encountered here is a [fix](install opencv: https://stackoverflow.com/questions/19876079/cannot-find-module-cv2-when-using-opencv).
Install pytesseract ```pip install pytesseract```.

### Instructions

To run this software save all PDF files to be converted in "pdfs" folder and run:

```
bash run.sh
```

