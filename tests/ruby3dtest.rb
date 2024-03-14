require 'ralent'

# Create a new Ralent model
model = Ralent::Model.new

# Add vertices
v1 = model.add_vertex(0, 0, 0)
v2 = model.add_vertex(1, 0, 0)
v3 = model.add_vertex(1, 1, 0)
v4 = model.add_vertex(0, 1, 0)
v5 = model.add_vertex(0.5, 0.5, 1)

# Add faces using previously defined vertices
model.add_face(v1, v2, v3)
model.add_face(v1, v3, v4)
model.add_face(v1, v2, v5)
model.add_face(v2, v3, v5)
model.add_face(v3, v4, v5)
model.add_face(v4, v1, v5)

# Export the model to an .obj file
model.export('cube.obj')
