
# Define the file name for the output .obj file
output_file = "shape.obj"


def FormatPolygons(polygons):
    faces = []
    vertices = []
    for polygon in polygons:
        for vertex in polygon:
            vertices.append(vertex)
    i = 0
    for p in range(len(polygons)):
        face = []
        for o in range(len(polygons[p])):
            i+=1
            face.append(i)
        faces.append(face)
    return vertices,faces
            

def CreateObjData(vertices,faces):
    output = []
    for vertex in vertices:
        output.append(f"v {' '.join(map(str, vertex))}\n")
        #obj_file.write(f"v {' '.join(map(str, vertex))}\n")
    
    for face in faces:
        output.append(f"f {' '.join(map(str, face))}\n")
        #obj_file.write(f"f {' '.join(map(str, face))}\n")
    return output


if __name__ == '__main__':
    # Define the vertices of the object
    vertices = [
        (0.0, 0.0, 0.0),
        (1.0, 0.0, 0.0),
        (1.0, 1.0, 0.0),
        (0.0, 1.0, 0.0),
        (0.0, 0.0, 1.0),
        (1.0, 0.0, 1.0),
        (1.0, 1.0, 1.0),
        (0.0, 1.0, 1.0)
    ]

    # Define the faces of the object
    faces = [
        (1, 2, 3, 4),
        (5, 6, 7, 8),
        (1, 2, 6, 5),
        (2, 3, 7, 6),
        (3, 4, 8, 7),
        (4, 1, 5, 8)
    ]

    # Define the file name for the output .obj file
    output_file = "shape.obj"
    # Write the vertices and faces to the .obj file
    with open(output_file, "w") as obj_file:
        data = "".join(CreateObjData(vertices,faces))
        obj_file.write(data)

    print(f".obj file '{output_file}' has been created.")
