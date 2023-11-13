<!-- PROJECT LOGO -->
<br />
<p align="center">
  <img src="images/main2.png" width="450" height="350">

  <h3 align="center"> AutomatedPCBInspection</h3>

  <p align="center">
    Garrett Bowman's Senior Design Project
    <br />
    <br />
    <a href="#performance-and-results">View Demonstration</a>
    <br />
  </p>
</p>

<br />

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#about-the-project">About The Project</a></li>
    <li><a href="#dependencies">Dependencies</a></li>
    <li><a href="#setup-and-usage">Setup and Usage</a></li>
    <li><a href="#Demonstration">Demonstration</a></li>
    <li><a href="#authors">Authors</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
    <li><a href="#thank-you">Thank You</a></li>
  </ol>
</details>


<!-- ABOUT THE PROJECT -->
## About The Project
Ensure hardware security.

<br />

<br />

<p align="center">
    DFgdfgwlkjgowdfglwfdg
    <br />
    <br />
    <img src=images/eye.png width=432 height=288>
</p>


<!-- (more information and explanation may be added here) -->


<!-- Dependencies -->

## Dependencies

<img src=images/galac.jpg>
 What I used but should work with other ros2 compatible versions.

<br />

<img src=images/ros2.png>
 I used ROS2 by following instructions specifically for Trossen X-series Robotic Arms products on Ubuntu 20.04. https://www.trossenrobotics.com/docs/interbotix_xsarms/ros_interface/software_setup.html

<br />

<img src=images/realsense.png>
Realsense D405 camera was used for eye in hand camera but other models may work similarly.

<br />
  
<img src=images/py3.png width=100 height=100>

<br />

<!-- Setup and Usage -->

## Setup and Usage

First, clone the repo!AutomatedPCBInspection.git
cd AutomatedPCBInspection
```
<br />

Next, ensure execution of the python scripts is allowed
```sh
chmod u+x main.py
```
<br />

Next, copy the training imageset to the root of the project directory. The training imageset can be downloaded from 
[canvas](https://ufl.instructure.com/courses/455012/files/69385213/download) or found in the shared folder when working with HiperGator.

<br />
```sh
git https://github.com/garrettbowman/

To train and create the image classification model, one may run
```sh
python create_model.py <name of training imageset> <name of training imageset labels>
```
<br />

> **Note** **To create a test dataset and its labels from the training set, the --debug flag may be used** <br />
> * Use of the debug flag is not required and is helpful when only a training dataset is provided <br />
> * Use of the --debug flag is seen below
<br />

For example, to create a model with the training images and corrected training labels as well as save a derived test set, one may 
run
```sh
python create_model.py data_train.npy corrected_labels.npy --debug
```
<br />

The script will output an image classification model in the h5 format, "image_model.h5" when it has ran successfully.
<br />
<br />

> **Note** **To use a pre-existing model, simply:**
> * Skip execution of the create_model.sh
> * Copy your model file to the root of the project directory
> * Specify your model file when running "evaluate_model_performance.py" as seen below
<br />

To evaluate the model's performance against a user-specified training or testing image set, one may run
```sh
python evaluate_model_performance.py <filename of dataset> <filename of dataset labels <filename of model.h>
```
<br />

> **Warning** **The evaluate_model_performance.py script EXPECTS that the dataset specified is in following format** <br />
> * 270,000 x M (numpy array, where M is the number of test samples)
<br />

For example, to evaulate the performance of the model with the debug test set generated above, one may run
```sh
python evaluate_model_performance.py debug/X_test_from_training.npy debug/X_test_from_training_labels.npy image_model.h5
```
<br />
<br />

*A jupyter notebook,* 'Final Project - Training and Testing Examples.ipynb' *has also been included in this repo. This 
notebook 
includes example code to run the test and train scripts detailed above.*

<br />

<!-- Performance and Results -->
## Performance and Results

Video Demonstration:

<br />

<p align="center">   
  https://www.youtube.com/watch?v=dQw4w9WgXcQ
</p>

<!-- Authors -->
## Authors

* Garrett Bowman, UF ECE - garrettbowman@ufl.edu

Project Link: [https://github.com/garrettbowman/AutomatedPCBInspection.git](https://github.com/garrettbowman/AutomatedPCBInspection.git)


<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements

* [Dr. Navid Asadi](https://faculty.eng.ufl.edu/catia-silva/) - Faculty Advisor
* [Patrick Craig](https://faculty.eng.ufl.edu/catia-silva/) - Mentor
* [Catia Silva](https://faculty.eng.ufl.edu/catia-silva/) - Created readme template

## Thank you

If you made it this far, thank you for reading!

<br />
<br />
<br />
<br />
This README was proudly written 100% with nano :)

