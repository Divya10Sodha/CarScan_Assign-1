from main import image_viz
import os

list = os.listdir('data/') 
number_files = len(list)

for i in range(number_files - 1):
    image_viz(str(i+1) +'.json', str(i+1) +'.jpg')
