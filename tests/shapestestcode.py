from pyglet.gl import *

class Shape:
    def __init__(self, color):
        self.color = color

    def draw(self):
        pass

    def contains_point(self, x, y):
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

    def contains_point(self, x, y):
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

    def contains_point(self, x, y):
        return False
