import javafx.application.Application;
import javafx.scene.Group;
import javafx.scene.Scene;
import javafx.scene.paint.Color;
import javafx.scene.shape.Rectangle;
import javafx.stage.Stage;

public class Main extends Application {
    @Override
    public void start(Stage primaryStage) throws Exception {
        Rectangle cube = new Rectangle(100, 100);
        cube.setFill(Color.RED);
        cube.setLayoutX(350);
        cube.setLayoutY(250);

        Group root = new Group();
        root.getChildren().add(cube);
        Scene scene = new Scene(root, 800, 600);

        primaryStage.setTitle("JavaFX Cube");
        primaryStage.setScene(scene);
        primaryStage.show();
    }

    public static void main(String[] args) {
        launch(args);
    }
}
