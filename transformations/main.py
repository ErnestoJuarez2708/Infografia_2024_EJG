import arcade
import numpy as np
import random
from game_object import Object3D

# Definicion de constantes
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Proyeccion 3D"

def get_random_color():
    return (
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255),
    )

class App(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.BLACK)

        # Definir la pirámide principal (cuerpo)
        self.body = Object3D(
            [
                (1, 1, 0),    # Vértice 0
                (1, -1, 0),   # Vértice 1
                (-1, -1, 0),  # Vértice 2
                (-1, 1, 0),   # Vértice 3
                (0, 0, 1),    # Vértice 4 (vértice superior)
            ],
            [
                (0, 1),
                (1, 2),
                (2, 3),
                (3, 0),
                (0, 4),
                (1, 4),
                (2, 4),
                (3, 4)
            ],
            arcade.color.ORANGE
        )
        self.body.translate(399, 399, 0)
        self.body.scale(100, 100, 100)
        
        # Definir la pirámide izquierda (oreja izquierda)
        self.ear_left = Object3D(
            [
                (0.5, 0.5, 0),    # Vértice 0
                (0.5, -0.5, 0),   # Vértice 1
                (-0.5, -0.5, 0),  # Vértice 2
                (-0.5, 0.5, 0),   # Vértice 3
                (0, 0, 1),        # Vértice 4 (vértice superior)
            ],
            [
                (0, 1),
                (1, 2),
                (2, 3),
                (3, 0),
                (0, 4),
                (1, 4),
                (2, 4),
                (3, 4)
            ],
            arcade.color.ORANGE
        )
        self.ear_left.translate(323, 525, 0)  # Ajustar la posición y escala
        self.ear_left.scale(50, 50, 50)
        
        # Definir la pirámide derecha (oreja derecha)
        self.ear_right = Object3D(
            [
                (0.5, 0.5, 0),    # Vértice 0
                (0.5, -0.5, 0),   # Vértice 1
                (-0.5, -0.5, 0),  # Vértice 2
                (-0.5, 0.5, 0),   # Vértice 3
                (0, 0, 1),        # Vértice 4 (vértice superior)
            ],
            [
                (0, 1),
                (1, 2),
                (2, 3),
                (3, 0),
                (0, 4),
                (1, 4),
                (2, 4),
                (3, 4)
            ],
            arcade.color.ORANGE
        )
        self.ear_right.translate(475, 525, 0)  # Ajustar la posición y escala
        self.ear_right.scale(50, 50, 50)

    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
    # Calcular el ángulo entre el centro de la pantalla y la posición del mouse
        center_x, center_y = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2
        dx = x - center_x
        dy = y - center_y

    # Factor de escala para reducir la velocidad de rotación
        scale_factor = 0.001  # Ajusta este valor para controlar la sensibilidad

    # Calcular los ángulos de rotación en radianes
        angle_y = np.arctan2(dx, center_x) * 180 / np.pi * scale_factor  # Rotación en el eje Y (Horizontal)
        angle_x = np.arctan2(dy, center_y) * 180 / np.pi * scale_factor  # Rotación en el eje X (Vertical)

    # Limitar la rotación a 180 grados
        angle_x = np.clip(angle_x, -90, 90)
        angle_y = np.clip(angle_y, -90, 90)

    # Rotar el cuerpo y las orejas
        self.body.rotate(angle_x, "x")
        self.body.rotate(angle_y, "y")
        self.ear_left.rotate(angle_x, "x")
        self.ear_left.rotate(angle_y, "y")
        self.ear_right.rotate(angle_x, "x")
        self.ear_right.rotate(angle_y, "y")


    def on_draw(self):
        arcade.start_render()
        self.body.draw()
        self.ear_left.draw()
        self.ear_right.draw()

if __name__ == "__main__":
    app = App()
    arcade.run()
