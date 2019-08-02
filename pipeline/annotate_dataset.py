
from imutils import paths
import argparse
import imutils
import os
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", required=True,
    help="path to input directory of images")
ap.add_argument("-l", "--labels", required=True,
    help="path to input text file of labels")
ap.add_argument("-o", "--output", required=True,
    help="path to output directory of sorted images")
args = vars(ap.parse_args())

imagePaths = list(paths.list_images(args["input"]))
f = open(args["labels"], "r")

counts = {}

line = f.readline()
while(line):
    label = line.split()[1]
    imagePath = line.split()[0]
    [x1, y1, x2, y2] = line.split()[3:]
        
    image = cv2.imread(os.path.sep.join([args["input"], imagePath]))

    roi = image[int(y1): int(y2), int(x1) : int(x2)]    
    
    dirPath = os.path.sep.join([args["output"], label])
    
    if not os.path.exists(dirPath):
		os.makedirs(dirPath)
    
    count = counts.get(label, 0)  
    counts[label] = count + 1   

    p = os.path.sep.join([dirPath, "{}.jpg".format(str(counts[label]).zfill(5))])
    cv2.imwrite(p, roi)

    line = f.readline()

    
        
