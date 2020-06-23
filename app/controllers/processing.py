import numpy as np
import cv2
import FreeCAD as App
import Mesh as ms


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

def img_click(path, orientation):

	right_clicks = list()

	# Calls real scale ratio function to a variable
	object_scale = scale_ob.ratio(path)

	# Obtains the value of desired coordinates, then calculate horizontal or vertical distance between them
	if orientation == 'h':
		# Horizontal
		xa = right_clicks[0][0]
		xb = right_clicks[1][0]
		dp = abs(xa-xb)
		d = dp*object_scale

	elif orientation == 'v':
		# Vertical
		ya = right_clicks[0][1]
		yb = right_clicks[1][1]
		dp = abs(ya-yb)
		d = dp*object_scale

	# Distance obtained is returned by function
	right_clicks.clear()
	return d

def ratio(path):

	(x,y,r) = circle.crl(path)
	rt = 11.5/r

	return rt

def script(heightSize, widthSize):

    # Valores de operação de constraint no solido
    heightQuota = 46
    widthQuota = 7

    # Abre o arquivo
    App.openDocument(r"../data/ortese_mao_freecad.FCStd")

    # Define o sketch
    ActiveSketch = App.ActiveDocument.getObject('Sketch')

    # Altera a altura
    App.ActiveDocument.Sketch.setDatum(heightQuota, App.Units.Quantity(str(heightSize) + ' mm'))

    # Altera a largura
    App.ActiveDocument.Sketch.setDatum(widthQuota, App.Units.Quantity(str(widthSize) + ' mm'))

    # Refresh
    print("Running Refresh")
    App.getDocument('ortese_mao_freecad').recompute()

    # Salva o .stl
    __objs__= []
    __objs__.append(App.getDocument("ortese_mao_freecad").getObject("Body"))
    ms.export(__objs__,u"../data/outputCAD.stl")
