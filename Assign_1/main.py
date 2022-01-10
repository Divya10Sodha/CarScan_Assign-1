import cv2
import numpy as np
from google.colab.patches import cv2_imshow
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import json
from util import *

def image_viz(json_fileName, image_fileName, opacity = alpha, thickness = thickness):
    # read file
    with open('data/'+ json_fileName, 'r') as myfile:
        data=myfile.read()
    jsn = json.loads(data)

    img_path = 'images/' + image_fileName 
    img = cv2.imread(img_path) 
    img2 = cv2.imread(img_path) 
    lst2= []

    for i in jsn:
      if(i['type'] == 'polygonlabels'):
          lst2.append(i['value']['polygonlabels'][0])

          original_width = i['original_width']
          original_height = i['original_height']

          # img = cv2.resize(img, (i['original_width'], i['original_height'])) 
      
          pts = np.array(recur(i['value']['points'], -1, width=i['original_width']/100, height=i['original_height']/100))
          
          min_x = min([p1[0] for p1 in pts]) 
          max_x = max([p1[0] for p1 in pts]) 
          min_y = min([p1[1] for p1 in pts]) 
          max_y = max([p1[1] for p1 in pts]) 
      
          #Type 1
          cv2.polylines(img, [pts], isClosed, dct[i['value']['polygonlabels'][0]], thickness)
          overlay = img.copy()
          cv2.fillPoly(overlay, [pts], dct[i['value']['polygonlabels'][0]])     
          img = cv2.addWeighted(overlay, alpha, img, 1 - alpha, 0)

          #Type 2
          cv2.polylines(img2, [pts], isClosed, dct[i['value']['polygonlabels'][0]], thickness)
          overlay = img2.copy()
          cv2.rectangle(img2, (min_x-gap, min_y -gap + 10), (min_x-gap + 130, min_y - gap), (0,0,0), cv2.FILLED)
          cv2.putText(img2, i['value']['polygonlabels'][0], (min_x+gap, min_y+gap), 0, 0.4, dct[i['value']['polygonlabels'][0]], 1)
          cv2.rectangle(img2, (min_x-gap, min_y-gap), (max_x+gap, max_y+gap), dct[i['value']['polygonlabels'][0]], 2)
          cv2.fillPoly(overlay, [pts], dct[i['value']['polygonlabels'][0]])     
          img2 = cv2.addWeighted(overlay, alpha, img2, 1 - alpha, 0)
    # cv2_imshow(img_resize)
    lst=[]

   
    # Creating legend with color box
    for k, v in dct.items():
      if k in lst2:
        lst.append(mpatches.Patch(color=rgb2hex(v[0], v[1], v[2]), label=k))

    plt.figure(figsize = (16, 10))
    plt.imshow(img)
    plt.legend(handles=lst,  bbox_to_anchor = (1.2, 1.0))
    
    plt.figure(figsize = (16, 10))
    plt.imshow(img2)
    plt.legend(handles=lst,  bbox_to_anchor = (1.2, 1.0))

    cv2.imwrite('output/type_1/output_' + image_fileName, img)
    cv2.imwrite('output/type_2/output_' + image_fileName, img2)
    cv2.waitKey(0)
cv2.destroyAllWindows()