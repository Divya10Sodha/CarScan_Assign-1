# CarScan_Assign-1

Task 1.1 - Data Visualization


Here we have to visualize the results on the images. In the folder "Assign_1", there are three folders, out of which first two are related to datasets:- 

1) **images** - Contains images named as 1.jpg, 2.jpg and so on

2) **data** - Contains metadata in form of JSON file named as 1.json, 2.json and so on

3) **output** - Contains two type of folders - 
    1) **type_1** contains just the images with visualization where only transparnt polygons are drawn
    2) **type_2** contains the images with visualization where bounding boxes are drawn around the transparent polygons and class of polygon displayed. (In this case, at upper-left corner) 

Exactly how these images are generated is in main.py file.

There are three python files:-
1) **util.py** - Contains all helper functions and code

2) **main.py** - Contains four parameters, out of which **json_fileName** and **image_fileName** are mandatory. The other two parameters **opacity** and **thickness** are optional.
Opacity relates to transparency factor and Thickness relates to thickness of border of polygons. The default values of optional parameters are set in the **util.py** file. 

3) **demo.py** - Contains demo code to call **main.py** file. On running, it generate two images in output folder for each image, of **type 1**  and **type 2** in their respective folders. Note - The output images have same shape as of input image.


Additionally with, **Assign_1 folder**, we have a notebook with name **Carscan_Assign1.ipynb**, which helps us to also see the legends on side of each output image, for better visualization. Also, it has optional code to copy the data and images from https://github.com/PushpakBhoge512/Assignment.git github repo, in case new data and images are added there.  
