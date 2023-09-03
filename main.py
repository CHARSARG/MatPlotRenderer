import matplotlib.pyplot as plt
import numpy as np
import math
import GetPolyData as poly
import PolygonModifiers as PolyMove

def is_point_visible(point):
    # Check if the point is behind the camera (negative z-coordinate)
    if point[2] < 0:
        return False
    else:
        return True
def Polygon_Behind_Camera(polygon):
    visible = 0
    for pos in polygon:
        if is_point_visible(pos):
            visible+=1
    return not visible == 3

def rotate_point(x1, y1, x2, y2, theta_degrees):
    # Convert theta from degrees to radians
    theta_radians = math.radians(theta_degrees)

    # Calculate the new coordinates after rotation
    x_new = x2 + (x1 - x2) * math.cos(theta_radians) - (y1 - y2) * math.sin(theta_radians)
    y_new = y2 + (x1 - x2) * math.sin(theta_radians) + (y1 - y2) * math.cos(theta_radians)

    return x_new, y_new

def rotate_3d_point(point,origin,angle):
    temp_point = [0,0,0]
    temp_x,temp_y = rotate_point(point[0],point[1],origin[0],origin[1],angle[1])
    temp_point = [temp_x,temp_y,point[2]]
    temp_x,temp_z = rotate_point(temp_point[0],temp_point[2],origin[0],origin[2],angle[0])
    temp_point = [temp_x,temp_point[1],temp_z]
    return temp_point

def rotate_polygons(polygons,origin,angle):
    temp_polygons = []
    for polygon in polygons:
        temp_polygon = []
        for point in polygon:
            temp_point = rotate_3d_point(point,origin,angle)
            temp_polygon.append(temp_point)
        temp_polygons.append(temp_polygon)
    return temp_polygons
            


def update(x,y):
    display.set_xdata(x)
    display.set_ydata(y)
    fig.canvas.draw()
    fig.canvas.flush_events()


def project_3d_to_2d(x, y, z, d):
    # Calculate the angle of projection
    theta = math.atan2(z, d)

    # Calculate the projected x and y coordinates
    projected_x = x * math.cos(theta) - y * math.sin(theta)
    projected_y = x * math.sin(theta) + y * math.cos(theta)

    return projected_x, projected_y

def Project_Polygon(polygon,d,cam):
    CamX = cam[0]
    CamY = cam[1]
    CamZ = cam[2]
    X = []
    Y = []
    for point in polygon:
        x = (point[0]+CamX)
        y = (point[1]+CamY)
        z = (point[2]+CamZ)
        X1,Y1=(project_3d_to_2d(x,y,z,d))
        #print(X1,Y1)
        X.append(X1)
        Y.append(Y1)
    return X,Y

def Render(polygons,d,cam):
    x=[]
    y=[]
    for polygon in polygons:
        if not Polygon_Behind_Camera:
            pass
        else:
            X,Y = Project_Polygon(polygon,d,cam)
            #print(x,y)
            for item in X:
                x.append(item)
            for item in Y:
                y.append(item)
    return x,y

    

# Initial render:
model_name = 'cube.obj'
polygons = poly.extract_polygons_from_obj(model_name)
d = 100
cam = [0,0,0,0,0]
x,y = Render(polygons,d,cam)

# Start display:
plt.ion()
fig = plt.figure()
ax = fig.add_subplot(111)
display, = ax.plot(x, y, 'b-')

# Main loop:
phase = 0
while True:
    phase +=1
    print(phase)
    #cam[2] = phase
    angle = (cam[3],cam[4])
    temp_polygons = polygons
    temp_polygons = PolyMove.TransformPolygons(polygons,(0,0,phase))
    #temp_polygons = rotate_polygons(polygons,cam,angle)

    #Prject 3d to 2d
    x,y = Render(temp_polygons,d,cam)

    #Add the last verticie 1 to the end of every 3 verticies.
    tempX = []
    tempY = []
    for i1 in range(int(len(x)/3)):
        for i2 in range(3):
            i = i1+i2
            item = x[i]
            tempX.append(item)
        tempX.append(x[i1])
    for i1 in range(int(len(y)/3)):
        for i2 in range(3):
            i = i1+i2
            item = y[i]
            tempY.append(item)
        tempY.append(y[i1])
    update(tempX,tempY)
