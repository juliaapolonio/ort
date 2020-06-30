import math 
import cv2
import numpy as np
import os
import sys
import subprocess

FREECADPATH = '/home/julia/miniconda3/envs/flask-env/lib' 
sys.path.append(FREECADPATH)

import FreeCAD as App
import Mesh as ms

ALLOWED_EXTENSIONS = {'png', 'jpeg', 'jpg'}


# Function to see if file format is valid
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Function to detect circle and give its center and radius at image
def crl(path):

    # Load the image, clone it for output, and then convert it to grayscale
	image = cv2.imread(path,1)
	output = image.copy()
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect circles in the image
	circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1.2, 100)
	
    # Ensure at least some circles were found
	if circles is not None:
		
    # Convert the (x, y) coordinates and radius of the circles to integers
		circles = np.round(circles[0, :]).astype("int")

    # Return values
		for (x,y,r) in circles:
			return (x,y,r)

# Function to calculate distance between points
def img_click(path, x1, y1, x2, y2):
    x1=int(x1)
    x2=int(x2)
    y1=int(y1)
    y2=int(y2)
    
    # Calls real scale ratio function to a variable
    object_scale = ratio(path)

    # Calculate Euclidean distance between points
    dp = math.sqrt(pow((x1-x2),2)+pow((y1-y2),2))
    # Multiply by 2 is necessary beause image is shown with 50% width
    d = dp*object_scale*2

    # Return real Euclidean distance between points
    return d

# Function that calculates the real distance conversion ratio
def ratio(path):

    # Calls function circle 
	(x,y,r) = crl(path)
    # Calculate ratio using 50 centavos-real (modify this with radius of the spot you're using)
	rt = 11.5/r
    #Return conversion ratio
	return rt

    # Function to run CAD Module

# Function to run CAD Module
def script(heightSize, widthSize):

    # Constraint values of variable quota
    heightQuota = 46
    widthQuota = 7

    # Open file
    App.openDocument(r"app/static/data/ortese_mao_freecad.FCStd")

    # Open sketch
    ActiveSketch = App.ActiveDocument.getObject('Sketch')

    # Changes height
    App.ActiveDocument.Sketch.setDatum(heightQuota, App.Units.Quantity(str(heightSize) + ' mm'))

    # Changes width
    App.ActiveDocument.Sketch.setDatum(widthQuota, App.Units.Quantity(str(widthSize) + ' mm'))

    # Refresh
    print("Running Refresh")
    App.getDocument('ortese_mao_freecad').recompute()

    # Saves .stl
    __objs__= []
    __objs__.append(App.getDocument("ortese_mao_freecad").getObject("Body"))
    ms.export(__objs__,u"app/static/data/outputCAD.stl")


# Function for running CAM module
def runSlicer():

    # Bash code for slicing stl model
    subprocess.call("app/Slic3r/perl-local -I app/Slic3r/local-lib/lib/perl5 app/Slic3r/slic3r.pl" + 
    " app/static/data/outputCAD.stl --load app/static/data/myconfig.ini --output app/static/data/saida.gcode", shell = True)
