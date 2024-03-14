import pyglet
from pyglet.gl import *
import json

class Ralent (pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.shapes = []
        self.selected_shape = None
        self.menu_opened = False
        self.undo_stack = []
        self.redo_stack = []

    def on_draw(self):
        self.clear()
        self.draw_menu()
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

        if self.menu_opened:
            if x >= 100 and x <= 200 and y >= 400 and y <= 450:
                self.add_cube()
            elif x >= 100 and x <= 200 and y >= 350 and y <= 400:
                self.add_sphere()
            self.menu_opened = False

    def on_key_press(self, symbol, modifiers):
        if symbol == pyglet.window.key.M:
            self.menu_opened = not self.menu_opened
        elif symbol == pyglet.window.key.S:
            self.save_scene()
        elif symbol == pyglet.window.key.L:
            self.load_scene()
        elif symbol == pyglet.window.key.U:
            self.undo()
        elif symbol == pyglet.window.key.R:
            self.redo()

    def draw_menu(self):
        if self.menu_opened:
            glColor3f(0.5, 0.5, 0.5)
            glBegin(GL_QUADS)
            glVertex2f(0, 0)
            glVertex2f(self.width, 0)
            glVertex2f(self.width, self.height)
            glVertex2f(0, self.height)
            glEnd()

            pyglet.text.Label("Menu", font_size=20, x=10, y=self.height - 20).draw()

            pyglet.text.Label("Add Cube", font_size=16, x=10, y=self.height - 50).draw()
            pyglet.text.Label("Add Sphere", font_size=16, x=10, y=self.height - 100).draw()

    def add_cube(self):
        cube = self.create_cube(100, 100, 100, (100, 100))
        self.shapes.append(cube)
        self.undo_stack.append(("add", cube))

    def add_sphere(self):
        sphere = self.create_sphere(50, (200, 200))
        self.shapes.append(sphere)
        self.undo_stack.append(("add", sphere))

    def save_scene(self):
        with open("scene.json", "w") as f:
            json.dump([shape.serialize() for shape in self.shapes], f)

    def load_scene(self):
        with open("scene.json", "r") as f:
            data = json.load(f)
        self.shapes = [self.deserialize_shape(shape_data) for shape_data in data]

    def undo(self):
        if self.undo_stack:
            action, shape = self.undo_stack.pop()
            if action == "add":
                self.shapes.remove(shape)
                self.redo_stack.append(("add", shape))
            elif action == "remove":
                self.shapes.append(shape)
                self.redo_stack.append(("remove", shape))

    def redo(self):
        if self.redo_stack:
            action, shape = self.redo_stack.pop()
            if action == "add":
                self.shapes.append(shape)
                self.undo_stack.append(("add", shape))
            elif action == "remove":
                self.shapes.remove(shape)
                self.undo_stack.append(("remove", shape))

    def create_cube(self, width, height, depth, position, color=(255, 0, 0)):
        return Cube(width, height, depth, position, color)

    def create_sphere(self, radius, position, color=(0, 0, 255)):
        return Sphere(radius, position, color)

class Shape:
    def __init__(self, color):
        self.color = color

    def draw(self):
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
        glutSolidSphere(self.radius, slices, stacks

if __name__ == "__main__":
    window = ShapeDrawer(800, 600, "Ralent v0.12")
    pyglet.app.run()

