require 'jrubyfx'

java_import 'javafx.application.Platform'
java_import 'javafx.scene.Scene'
java_import 'javafx.scene.control.Menu'
java_import 'javafx.scene.control.MenuBar'
java_import 'javafx.scene.control.MenuItem'
java_import 'javafx.scene.layout.BorderPane'
java_import 'javafx.scene.paint.Color'
java_import 'javafx.scene.shape.Box'
java_import 'javafx.scene.shape.Sphere'
java_import 'javafx.scene.shape.Cone'
java_import 'javafx.scene.shape.Cylinder'
java_import 'javafx.scene.transform.Rotate'
java_import 'javafx.animation.RotateTransition'
java_import 'javafx.util.Duration'
java_import 'javafx.animation.Animation'

class ShapeDrawer < JRubyFX::Application
  def start(stage)
    stage.title = "Shape Drawer"
    root = BorderPane.new

    menu_bar = MenuBar.new
    shapes_menu = Menu.new("Add Shapes")
    cube_item = MenuItem.new("Add Cube")
    sphere_item = MenuItem.new("Add Sphere")
    cone_item = MenuItem.new("Add Cone")
    cylinder_item = MenuItem.new("Add Cylinder")

    shapes_menu.items.addAll(cube_item, sphere_item, cone_item, cylinder_item)
    menu_bar.menus.add(shapes_menu)

    cube_item.on_action do
      size = 100
      color = Color::RED
      x = 100
      y = 100
      z = 100
      cube = create_cube(size, color, x, y, z)
      root.children.add(cube)
    end

    sphere_item.on_action do
      radius = 50
      color = Color::BLUE
      x = 200
      y = 200
      z = 200
      sphere = create_sphere(radius, color, x, y, z)
      root.children.add(sphere)
    end

    cone_item.on_action do
      radius = 50
      height = 100
      color = Color::GREEN
      x = 300
      y = 300
      z = 300
      cone = create_cone(radius, height, color, x, y, z)
      root.children.add(cone)
    end

    cylinder_item.on_action do
      radius = 50
      height = 100
      color = Color::YELLOW
      x = 400
      y = 400
      z = 400
      cylinder = create_cylinder(radius, height, color, x, y, z)
      root.children.add(cylinder)
    end

    root.top = menu_bar

    scene = Scene.new(root, 800, 600)
    scene.on_mouse_dragged = -> (event) {
      if @selected_shape
        @selected_shape.translate_x = event.x
        @selected_shape.translate_y = event.y
        @selected_shape.translate_z = event.z
      end
    }

    scene.on_mouse_clicked = -> (event) {
      @selected_shape = scene.pick(event.x, event.y)
    }

    stage.scene = scene
    stage.show
  end

  def create_cube(size, color, x, y, z)
    cube = Box.new(size, size, size)
    cube.translate_x = x
    cube.translate_y = y
    cube.translate_z = z
    cube.material = javafx.scene.paint.PhongMaterial.new(color)
    cube
  end

  def create_sphere(radius, color, x, y, z)
    sphere = Sphere.new(radius)
    sphere.translate_x = x
    sphere.translate_y = y
    sphere.translate_z = z
    sphere.material = javafx.scene.paint.PhongMaterial.new(color)
    sphere
  end

  def create_cone(radius, height, color, x, y, z)
    cone = Cone.new(radius, height)
    cone.translate_x = x
    cone.translate_y = y
    cone.translate_z = z
    cone.material = javafx.scene.paint.PhongMaterial.new(color)
    cone
  end

  def create_cylinder(radius, height, color, x, y, z)
    cylinder = Cylinder.new(radius, height)
    cylinder.translate_x = x
    cylinder.translate_y = y
    cylinder.translate_z = z
    cylinder.material = javafx.scene.paint.PhongMaterial.new(color)
    cylinder
  end
end

ShapeDrawer.launch
