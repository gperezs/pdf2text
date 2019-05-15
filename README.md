# PDF to TXT conversion

Pytorch code for the conversion of news PDF files to TXT files. PDF files are converted to images, pre-processed, and then converted to text using [tesseract](https://github.com/tesseract-ocr).  

## Getting started

### Prerequisites

This code runs on Linux. The code was implemented in Python 2.7.*.

#### Working with Anaconda virtual environment (Recommended):

**Installing Anaconda:** I recommend using the free [Anaconda Python distribution](https://www.anaconda.com/distribution/).

**Anaconda Virtual Environment:** Once you have Anaconda installed, it makes sense to create a virtual environment before installing all dependencies. To do so run:

```
conda create -n environment_name python=2.7 anaconda
```  

Then, to activate and enter the environment, run:
```
source activate environment_name
```
To exit, simply close the window or run:
```
source deactivate environment_name
``` 

**Note:** If you decide to create the virtual environment, everytime you want to run this you should run ```source activate environment_name``` (change to the name of your virtual env.).

#### PDF to image conversion:

If you decide to use a virtual env., run ```source activate environment_name``` before installing the dependencies.

**Dependencies:**

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

If ```ImportError: No module named cv2``` is encountered here is a [fix](https://stackoverflow.com/questions/19876079/cannot-find-module-cv2-when-using-opencv).

Install pytesseract ```pip install pytesseract```.

### Instructions

To run this software save all PDF files to be converted in "./pdfs" folder and run:

```
bash run.sh
```
This software will create a TXT file for each PDF file and saves them in "./converted_text/" folder. Also, an "all_text.txt" file is created with all the text from all PDF fles in "./pdfs/" folder.
