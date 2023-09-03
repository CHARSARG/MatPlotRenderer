import GetPolyData as GetPoly
import PolygonModifiers as MovePoly
import CreateObj as SetPoly


InputFile = 'monkey.obj'
OutputFile = 'test.obj'
transform = (0,0,50)


polygons = GetPoly.extract_polygons_from_obj(InputFile)

polygons = MovePoly.TransformPolygons(polygons,transform)

vertices,faces = SetPoly.FormatPolygons(polygons)
data = SetPoly.CreateObjData(vertices,faces)
content = "".join(data)

with open(OutputFile,'w') as obj_file:
    obj_file.write(content)


