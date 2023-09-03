def TransformPolygons(polygons,transform):
    temp_polygons = []
    for polygon in polygons:
        temp_polygon = []
        for vertex in polygon:
            temp_vertex = []
            for i in range(3):
                item = vertex[i]
                move = transform[i]
                temp_vertex.append(item+move)
            temp_polygon.append(temp_vertex)
        temp_polygons.append(temp_polygon)
    return temp_polygons
