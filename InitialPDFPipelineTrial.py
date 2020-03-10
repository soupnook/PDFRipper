# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 15:11:35 2020

@author: d.krishna
"""

import pytesseract
import pdf2image
from PIL import Image
from pdf2image import convert_from_path
import os
import sys
import fuzzywuzzy


#%%

PDF_File = "Test.pdf"

pages = convert_from_path(PDF_File,500)
count = 1
for page in pages:
    filename = "Test_page"+str(count)+".jpg"
    page.save(filename,"JPEG")
    count+=1
    
filelimit = count - 1

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

outputfile = open("outputfile.txt", "a+")

for i in range(1,filelimit+1):
    filename = "Test_page"+str(i)+".jpg"
    text = str(((pytesseract.image_to_string(Image.open(filename))))) 
    text = text.replace('-\n', '')
    outputfile.write(text)
    print(text)
    



#%%

# UNFINISHED - GETTING THE REQUIRED FIELDS FROM THE CORPUS

file = open("outputfile.txt", "r")
# Getting the field required from the output file


#REDACTED FIELDS LIST - HAD CONTEXTUAL INFORMATION THERE
fieldsdict = {"x": [], "a": [],
              "y": [], "b": [],
              "z": [], "f": [], "c": [], "g": [],
              "w": [], "d": [], "e": []}

for line in file:
    stripped_line = line.strip()
#    print(stripped_line)
    for i in line:
        if i.lower() in fieldsdict.keys():
            print(i)
            print(line)
        if i.lower() in fieldsdict.values():
            print(i)
            print(line)





