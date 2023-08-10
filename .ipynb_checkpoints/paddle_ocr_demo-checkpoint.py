import pdf2image
from PIL import Image
import layoutparser as lp
import cv2
import numpy as np
import io
import pandas as pd
import matplotlib.pyplot as plt

def pdf_to_image_save():
    doc = pdf2image.convert_from_path("12561694_Sanitized.pdf")

    print(len(doc)) #<-- check num pages
    # print(doc[0])   #<-- visualize a page
    print(type(doc[0]))

    # for count, page in enumerate(doc):
    #     page.save(f'out{count}.jpg', 'JPEG')
    #     im = Image.open(f'out{count}.jpg')
    #     im.show()
    return doc


def dlc_detection(doc):
    ## load pre-trained model
    model = lp.Detectron2LayoutModel("lp://PubLayNet/mask_rcnn_X_101_32x8d_FPN_3x/config",
                extra_config=["MODEL.ROI_HEADS.SCORE_THRESH_TEST", 0.8],
                label_map={0:"Text", 1:"Title", 2:"List", 3:"Table", 4:"Figure"})
    ## turn img into array
    i = 5
    img = np.asarray(doc[i])
    ## predict
    detected = model.detect(img)
    
    ## plot
    lp.draw_box(img, detected, box_width=5, box_alpha=0.2, 
                show_element_type=True).show()


if __name__ == "__main__":

    doc = pdf_to_image_save()
    dlc_detection(doc)

