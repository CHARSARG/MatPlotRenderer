def extract_polygons_from_obj(obj_file):
    # Initialize lists to store vertex coordinates and polygons
    vertices = []
    polygons = []

    # Open and read the OBJ file
    with open(obj_file, 'r') as file:
        for line in file:
            parts = line.strip().split()
            if not parts:
                continue
            if parts[0] == 'v':
                # Vertex coordinates
                x, y, z = map(float, parts[1:])
                vertices.append((x, y, z))
            elif parts[0] == 'f':
                # Face (polygon) definition
                polygon = [int(vertex.split('/')[0]) - 1 for vertex in parts[1:]]
                polygons.append(polygon)

    # Convert the polygon data to the desired format
    formatted_polygons = []
    for polygon in polygons:
        formatted_polygon = [(vertices[vertex_index][0], vertices[vertex_index][1], vertices[vertex_index][2]) for vertex_index in polygon]
        formatted_polygons.append(formatted_polygon)

    return formatted_polygons


"""
# Replace 'path_to_your_3d_model.obj' with the path to your 3D model file
model_file = 'monkey.obj'

# Call the function and get the polygons
polygons = extract_polygons_from_obj(model_file)
"""
