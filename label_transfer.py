#!/usr/bin/env python
# coding: utf-8

# In[2]:


import json
import numpy as np
import matplotlib.pyplot as plt
import cv2
import matplotlib.image as mpimg


# In[3]:


def openjson(json_path):
    obj = open(json_path)
    return json.load(obj)


# In[5]:


def transform_cor(json_dict,scale=None):
    ans = []
    for data in json_dict:
        res = []
        points = data['points']
        i = 0
        while(i < len(points)-1):
            temp = []
            if scale is not None:
                temp.append(int(points[i]/scale))
                temp.append(int(points[i+1]/scale))
            else:
                temp.append(points[i])
                temp.append(points[i+1])
            temp = np.array(temp)
            res.append(temp)
            i = i + 2
        res.append(temp)
        res = np.array(res)
        ans.append(res)
    return ans        


# In[6]:


def get_box(ans):
    boxes = []
    for box in ans:
#         print(type(box))
#         print (box.shape)
          kuang = []
          x_min = np.min(box,axis=0)[0]
          y_min = np.min(box,axis=0)[1]
          x_max = np.max(box,axis=0)[0]
          y_max = np.max(box,axis=0)[1]
          x_min = int(x_min)
          y_min = int(y_min)
          w = x_max - x_min
          h = y_max - y_min
          kuang.append(x_min)
          kuang.append(y_min)
          kuang.append(x_max)
          kuang.append(y_max)
          boxes.append(kuang)
    return boxes


# In[7]:


def main():
    input_path = ('/home/bnc/tool/HistomicsML/yourproject/json/51457004.json')
    img_path = ('/home/bnc/tool/HistomicsML/yourproject/level3/51457004.tif')
    img = cv2.imread(img_path) 
    plt.imshow(img)
    plt.show()
    info = openjson(input_path)
    cor = transform_cor(info,128)
    boxes = get_box(cor)
    for box in boxes:
        cv2.rectangle(img, (box[0], box[1]), (box[2], box[3]), (0, 255, 0), thickness=2)
        #cv2.putText(img, objectname, (box[0], box[0]), cv.FONT_HERSHEY_COMPLEX, 0.7, (0, 255, 0),thickness=2)
        plt.imshow(img)
        plt.show()
    print(len(box))
    print(len(cor))
    cv2.imwrite('./box.png',img)


# In[18]:


if __name__ == "__main__":
    main()

