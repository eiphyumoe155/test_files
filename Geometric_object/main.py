import numpy as np
import pandas as pd
from flask import Flask, request
from rectangle import Rectangle
from circle import Circle
from triangle import Triangle
import json


app = Flask(__name__)

@app.get("/")
def homePage():
    return "hello this is homepage"

@app.post("/find_rectangle_area")
def find_rectangle_area():
    request_data = request.json
    rectangle = Rectangle(request_data["width"], request_data["height"])
    area = rectangle.area()
    return json.dumps({"The area of rectangle is ": area})

@app.post("/find_circle_area")
def find_circle_area():
    request_data = request.json
    circle = Circle(request_data["diameter"])
    radius = circle.find_radius()
    area = circle.area(radius=radius)
    return json.dumps({"The area of the circle is ":area})

@app.post("/find_perimeter")
def find_perimeter():
    request_data = request.json
    triangle = Triangle(request_data["side1"], request_data["side2"], request_data["side3"])
    perimeter = triangle.perimeter()
    return json.dumps({"The perimeter of the triangle is ":perimeter})

    

app.run(debug=False, host="0.0.0.0",port = 8080)