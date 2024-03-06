if __name__ == "__main__":
    window = ShapeDrawer(800, 600, "Shape Drawer")

    cube = Cube(100, 100, 100, (100, 100))
    window.shapes.append(cube)

    sphere = Sphere(50, (400, 300))
    window.shapes.append(sphere)

    pyglet.app.run()

