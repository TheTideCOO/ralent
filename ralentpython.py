import pyglet
from pyglet.gl import *
import json

class ShapeDrawer(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.shapes = []
        self.selected_shape = None

        # Create menu
        self.menu = pyglet.menu.Menu()
        self.menu.add_command("Add Cube", self.add_cube)
        self.menu.add_command("Add Sphere", self.add_sphere)
        self.menu.add_command("Save Scene", self.save_scene)
        self.menu.add_command("Load Scene", self.load_scene)

    def on_draw(self):
        self.clear()
        for shape in self.shapes:
            shape.draw()

    def on_mouse_drag(self, x, y, dx, dy, buttons, modifiers):
        if self.selected_shape:
            self.selected_shape.position = (self.selected_shape.position[0] + dx, self.selected_shape.position[1] + dy)

    def on_mouse_press(self, x, y, button, modifiers):
        for shape in self.shapes:
            if shape.contains_point(x, y):
                self.selected_shape = shape
                break
        else:
            self.selected_shape = None

    def add_cube(self):
        cube = self.create_cube(100, 100, 100, (100, 100))
        self.shapes.append(cube)

    def add_sphere(self):
        sphere = self.create_sphere(50, (200, 200))
        self.shapes.append(sphere)

    def save_scene(self):
        with open("scene.json", "w") as f:
            json.dump([shape.serialize() for shape in self.shapes], f)

    def load_scene(self):
        with open("scene.json", "r") as f:
            data = json.load(f)
        self.shapes = [self.deserialize_shape(shape_data) for shape_data in data]

    def create_cube(self, width, height, depth, position, color=(255, 0, 0)):
        return Cube(width, height, depth, position, color)

    def create_sphere(self, radius, position, color=(0, 0, 255)):
        return Sphere(radius, position, color)

    def deserialize_shape(self, data):
        if data["type"] == "cube":
            return Cube(data["width"], data["height"], data["depth"], data["position"], data["color"])
        elif data["type"] == "sphere":
            return Sphere(data["radius"], data["position"], data["color"])

class Shape:
    def __init__(self, color):
        self.color = color

    def draw(self):
        pass

    def serialize(self):
        pass

    @staticmethod
    def contains_point(x, y):
        pass

class Cube(Shape):
    def __init__(self, width, height, depth, position, color=(255, 0, 0)):
        super().__init__(color)
        self.width = width
        self.height = height
        self.depth = depth
        self.position = position

    def draw(self):
        glColor3ub(*self.color)
        x, y = self.position
        glBegin(GL_QUADS)
        glVertex2f(x, y)
        glVertex2f(x + self.width, y)
        glVertex2f(x + self.width, y + self.height)
        glVertex2f(x, y + self.height)
        glEnd()

    def serialize(self):
        return {
            "type": "cube",
            "width": self.width,
            "height": self.height,
            "depth": self.depth,
            "position": self.position,
            "color": self.color
        }

    @staticmethod
    def contains_point(x, y):
        return False

class Sphere(Shape):
    def __init__(self, radius, position, color=(0, 0, 255)):
        super().__init__(color)
        self.radius = radius
        self.position = position

    def draw(self):
        glColor3ub(*self.color)
        x, y = self.position
        slices = 20
        stacks = 20
        glPushMatrix()
        glTranslatef(x, y, 0)
        glutSolidSphere(self.radius, slices, stacks)
        glPopMatrix()

    def serialize(self):
        return {
            "type": "sphere",
            "radius": self.radius,
            "position": self.position,
            "color": self.color
        }

    @staticmethod
    def contains_point(x, y):
        return False

if __name__ == "__main__":
    window = ShapeDrawer(800, 600, "Shape Drawer")
    pyglet.app.run()
