## Introduction

This repo covers almost all the most promising `OCR technologies` out there in Data Science community that can be leveraged to perform `bounding box detection` and `text recognition` around the text objects identified by OCR algorithmns. Some of them are capable enough to handle 
`handwritten digits` based image documents while others can also work with `image URLs`. In general, there is `no standard means or metrics` to perform comparative or direct evaluation of all OCR algorithms covered in his post. However, this repo experiments and explores by working on case studies to critically analyze all these OCR algorithmns together `side by side` to better visualize the detected results when overlayed on actual image of scanned documents.



## Different types of OCR Algorithmns

In particular, we have considered 4 types of OCR algorithmns. These are as follows:

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

In this repo, we present `three separate notebooks` which serves three different purpose in `Document Image Analysis` or `DIA`.

#### Notebook 1: `OCR_detection_extraction_algorithms`
This notebook takes into account all the 4 `OCR` algorithmns one by one and performs bounding box detection around text object and further recognizes it to extract
the desired text into either `list of list` or `dictionary` object format.

You may simply follow the provided sequence and instructions in notebook to achieve the desired results.

#### Notebook 2: `PaddleOCRDemo`
This notebook explores the `PaddleOCR` algorithm in detail by performing detection and recognition across `5` different sample images of various types.
It tries to test various edge cases by considered Document images having both `computer generated` and `handwritten texts`.

#### Notebook 3: `bbox_coordinates_analysis`
This notebook performs deep analysis of OCR results overlay on actual images by placing and drawing the coordinates of bounding boxes using a given extracted 
JSON file. It takes into account the bounding box coordinates and saves the box overlayed images. It helps to analyse the best algorithmn for obtaining an almost perfect bounding boxes obeying the layout and structure of provided image document.



## If you decide for Citation 

```code
cff-version: 1.0.0
message: "If you use this software by referencing my notebook, please cite it as below."
authors:
- family-names: "Sahoo"
  given-names: "Shashank"
title: "OCR all in one Software"
version: 1.0.4
date-released: 2023-08-08
url: "https://github.com/Shashank545/OCR_all_in_one"

```

#### If you like this work, you may also like my blogs

Do not forget to follow me at, [Shashank's Medium Profile](https://medium.com/@Immaculate_sha2nk)

Also, consider to share your valuable comments and feedback by [BUYINGmePIZZA](https://www.buymeacoffee.com/mrtensorllm)

You can post me your business enquiries and suggestions at >>>   `mr.tensorflow@gmail.com`