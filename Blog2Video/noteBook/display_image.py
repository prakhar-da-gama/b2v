import os
import sys
from pycocotools.coco import COCO
import urllib
import zipfile
from google.colab.patches import cv2_imshow
from skimage import io

for x in words:
  img_path = "/content/dataset/"+x+"/Image_1.jpg"
  try:
    image = io.imread(img_path)
    cv2_imshow(image)
  except:
    print("No Image Found")
    
   
  


