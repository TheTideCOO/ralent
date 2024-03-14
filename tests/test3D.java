import javafx.application.Application;
import javafx.scene.Group;
import javafx.scene.PerspectiveCamera;
import javafx.scene.Scene;
import javafx.scene.paint.Color;
import javafx.scene.shape.Box;
import javafx.scene.transform.Rotate;
import javafx.stage.Stage;

public class Ralent3DModel extends Application {

    @Override
    public void start(Stage primaryStage) {
        // Creating a box (3D model)
        Box box = new Box(100, 100, 100);
        box.setTranslateX(200);
        box.setTranslateY(150);
        box.setTranslateZ(50);
        box.setMaterial(new javafx.scene.paint.PhongMaterial(Color.BLUE));

        // Creating a group and adding the box to it
        Group root = new Group(box);

        // Creating a scene
        Scene scene = new Scene(root, 600, 400, true);
        scene.setFill(Color.WHITE);

        // Adding a camera to view the 3D model
        PerspectiveCamera camera = new PerspectiveCamera(true);
        camera.setTranslateX(scene.getWidth() / -2);
        camera.setTranslateY(scene.getHeight() / -2);
        camera.setTranslateZ(-1000);
        scene.setCamera(camera);

        // Handling rotation of the model
        Rotate rotation = new Rotate();
        rotation.setAxis(Rotate.Y_AXIS);
        rotation.setAngle(45);
        box.getTransforms().addAll(rotation);

        // Setting up the stage
        primaryStage.setTitle("Ralent3D");
        primaryStage.setScene(scene);
        primaryStage.show();
    }

    public static void main(String[] args) {
        launch(args);
    }
}
