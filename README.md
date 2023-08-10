## Introduction

This repo covers almost all the most promising `OCR technologies`` out there in Data Science community that can be leveraged to perform
text `bounding box detection` and `recognition` around the text objects identified by OCR algorithmns. Some of them are acapable enough to handle handwritten
digits based image documents while others can also work with URLs. In general, there is no standard means or metrics to perform comparative or direct evaluation of all OCR algorithms covered in his post. However, this repo experiments and explores by working on case studies to critically analyze all these OCR algorithmns together side by side to better visualize the detected results when overlayed on actual image.



## Different types of OCR Algorithmns

In particular, we have considered 4 types of OCR alogorithmns. These are as follows:

1. [Layout Parser Algorithmn](https://pypi.org/project/layoutparser/)
2. [PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR)
3. [EasyOCR](https://github.com/JaidedAI/EasyOCR)
4. [TrOCR](https://huggingface.co/docs/transformers/model_doc/trocr)


## Steps to install all OCRs

#### Layout parsing algorithmn
```code
!pip install -U layoutparser
!pip install 'git+https://github.com/facebookresearch/detectron2.git@v0.4#egg=detectron2' 
!pip install layoutparser[ocr]      
!sudo apt install tesseract-ocr
!sudo apt install libtesseract-dev
```


#### PaddleOCR
```code
!python3 -m pip install paddlepaddle-gpu
!pip install "paddleocr>=2.0.1"
```


#### EasyOCR
```code
!pip install easyocr
```

#### TrOCR
```code
!pip install transformers
```

## Notebook summary

In this repo, we present three separate notebooks which serves three different purpose in `Document Image Analysis` or `DIA``.

#### Notebook 1: `OCR_detection_extraction_algorithms`
This notebook takes into account all the 4 `OCR` algorithmns one by one and performs bounding box detection around text object and further recognizes it to extract
the desired text into either `list of list`` or `dictionary` object.

You may simply follow the provided sequence and instructions in notebook to achieve the desired results.

#### Notebook 2: `PaddleOCRDemo`
This notebook explore the `PaddleOCR` algorithmn in detail by performing detection and recognition across `5` different sample images of various types.
It tries to test edge cases by considered Document images having both `computer generated` and `handwritten texts`.

#### Notebook 3: `bbox_coordinates_analysis`
This notebook performs deep analysis of OCR results overlay on actual images by placing and drawing the coordinates of bounding boxes using a given extracted 
JSON file. It takes into account the bounding box coordinates and saves the box overlayed images. It helps to analyse the best algorithmn for obtained a almost perfect bounding boxes obeying the layout and structure of provided image document.







