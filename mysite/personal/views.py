from django.shortcuts import render
import cv2
import os

def index(request):
	sourcepath = os.path.abspath("personal/static/personal/img/Groot.png")
	graypath = os.path.abspath("personal/static/personal/img/out.png")
	image = cv2.imread(sourcepath)
	cv2.imwrite(graypath, image)
	return render(request, 'personal/home.html')

def grey(request):
	sourcepath = os.path.abspath("personal/static/personal/img/Groot.png")
	graypath = os.path.abspath("personal/static/personal/img/out.png")
	image = cv2.imread(sourcepath)
	gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	cv2.imwrite(graypath, gray_image)
	return render(request, 'personal/home.html')

def edge(request):
	sourcepath = os.path.abspath("personal/static/personal/img/Groot.png")
	edgepath = os.path.abspath("personal/static/personal/img/out.png")
	image = cv2.imread(sourcepath)
	edge_image = cv2.Canny(image,100,200)
	cv2.imwrite(edgepath, edge_image)
	return render(request, 'personal/home.html')

def eyedetect(request):
	eye_cascade_path = os.path.abspath("personal/static/personal/haarcascade_eye.xml")
	sourcepath = os.path.abspath("personal/static/personal/img/Groot.png")
	eyepath = os.path.abspath("personal/static/personal/img/out.png")
	eye_cascade = cv2.CascadeClassifier(eye_cascade_path)
	image = cv2.imread(sourcepath)
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	eyes = eye_cascade.detectMultiScale(gray, 1.2, 2)
	for (x,y,w,h) in eyes:
		cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),2)
		cv2.imwrite(eyepath, image)
	return render(request, 'personal/home.html')

def contact(request):
    return render(request, 'personal/basic.html',{'content':['If you would like to contact me, please email me.','arv.2050@gmail.com']})

def details(request):
    return render(request, 'personal/basic.html',{'content':['This is my first Django app.', 'I intend to build an interactive AI app.']})
