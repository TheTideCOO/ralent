import javafx.application.Application;
import javafx.event.ActionEvent;
import javafx.geometry.Insets;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Menu;
import javafx.scene.control.MenuBar;
import javafx.scene.control.MenuItem;
import javafx.scene.layout.BorderPane;
import javafx.scene.paint.Color;
import javafx.scene.shape.Box;
import javafx.scene.shape.Shape3D;
import javafx.stage.Stage;

public class Main extends Application {

    @Override
    public void start(Stage primaryStage) {
        BorderPane root = new BorderPane();

        MenuBar menuBar = new MenuBar();
        Menu shapesMenu = new Menu("Add Shapes");
        MenuItem cubeItem = new MenuItem("Add Cube");
        MenuItem sphereItem = new MenuItem("Add Sphere");

        shapesMenu.getItems().addAll(cubeItem, sphereItem);
        menuBar.getMenus().add(shapesMenu);

        cubeItem.setOnAction((ActionEvent event) -> {
            Shape3D cube = createCube();
            root.getChildren().add(cube);
        });

        sphereItem.setOnAction((ActionEvent event) -> {
            Shape3D sphere = createSphere();
            root.getChildren().add(sphere);
        });

        root.setTop(menuBar);

        Scene scene = new Scene(root, 800, 600);
        primaryStage.setTitle("Shape Drawer");
        primaryStage.setScene(scene);
        primaryStage.show();
    }

    private Shape3D createCube() {
        Box cube = new Box(100, 100, 100);
        cube.setTranslateX(100);
        cube.setTranslateY(100);
        cube.setTranslateZ(100);
        cube.setMaterial(new javafx.scene.paint.PhongMaterial(Color.RED));
        return cube;
    }

    private Shape3D createSphere() {
        javafx.scene.shape.Sphere sphere = new javafx.scene.shape.Sphere(50);
        sphere.setTranslateX(200);
        sphere.setTranslateY(200);
        sphere.setTranslateZ(200);
        sphere.setMaterial(new javafx.scene.paint.PhongMaterial(Color.BLUE));
        return sphere;
    }

    public static void main(String[] args) {
        launch(args);
    }
}
