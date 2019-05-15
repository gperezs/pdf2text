import os
import time
import numpy as np
#from matplotlib import pyplot as plt
import matplotlib.image as mpimg
from skimage.filters import threshold_otsu
from skimage.morphology import closing
from skimage.morphology import square
from skimage import measure
from scipy.ndimage.morphology import binary_fill_holes
from scipy import ndimage
from PIL import Image
import pytesseract

bb_size = 100000 # bounding box size
imdir = 'pdfs/images/' # complete images dir
outdir = 'converted_text/' # converted text dir
files = sorted(os.listdir(imdir))

f_all = open('all_text.txt','w')
for i in range(len(files)):
    ti = time.time()
    im = mpimg.imread(os.path.join(imdir,files[i]))
    imB = im[:,:,2]
    
    # image text patches extraction
    thresh = threshold_otsu(imB)
    binary = imB > thresh # image thresholding
    dil = closing(1-binary, square(15)) # morphological closing
    fill = binary_fill_holes(dil).astype(int) # fill holes
    cc_labels = measure.label(fill, background=0) # connected components
    
    cont = 0
    f = open(os.path.join(outdir,files[i][:-4]+'.txt'), 'w')
    for j in range(1,cc_labels.max()+1):
        slice_x, slice_y = ndimage.find_objects(cc_labels==j)[0]
        roi = im[slice_x, slice_y] # image patch
        if roi.shape[0]*roi.shape[1] > bb_size: # validate patchsize
            roi = (roi - roi.min())/(roi.max() - roi.min()) # normalize image from 0 to 1
            roi = Image.fromarray(np.uint8(roi*255)) # conver image to PIL
            roi_text = pytesseract.image_to_string(roi) # OCR function
            roi_text = roi_text.replace(u'-\n','') # remove -\n for incomplete words
            roi_text = roi_text.replace(u'\n',' ') # replace \n with a space
            f.write(roi_text.encode('utf8')) # write converted text to txt file
            f_all.write(roi_text.encode('utf8'))
    print('file %d/%d converted (%.3fs)'%(i+1,len(files),time.time()-ti))
    f.close()
f_all.close()
    
