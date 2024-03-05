import javafx.animation.Animation;
import javafx.animation.RotateTransition;
import javafx.application.Application;
import javafx.scene.Group;
import javafx.scene.PerspectiveCamera;
import javafx.scene.Scene;
import javafx.scene.paint.Color;
import javafx.scene.shape.Box;
import javafx.scene.transform.Rotate;
import javafx.stage.Stage;
import javafx.util.Duration;

public class Main extends Application {
    @Override
    public void start(Stage primaryStage) throws Exception {
        Box box = new Box(100, 100, 100);
        box.setTranslateX(350);
        box.setTranslateY(250);
        box.setTranslateZ(300);
        box.setFill(Color.RED);

        RotateTransition rotateTransition = new RotateTransition(Duration.seconds(4), box);
        rotateTransition.setAxis(Rotate.Y_AXIS);
        rotateTransition.setByAngle(360);
        rotateTransition.setCycleCount(Animation.INDEFINITE);
        rotateTransition.play();

        PerspectiveCamera camera = new PerspectiveCamera();
        camera.setTranslateZ(-500);

        Group root = new Group();
        root.getChildren().addAll(box);
        Scene scene = new Scene(root, 800, 600, true);
        scene.setCamera(camera);

        primaryStage.setTitle("JavaFX 3D Cube");
        primaryStage.setScene(scene);
        primaryStage.show();
    }

    public static void main(String[] args) {
        launch(args);
    }
}
