import arcade
import Const as C


class Ship(arcade.Sprite):

    def __init__(self, x, y, rotation, sprite, boardLen):
        self.x = x
        self.y = y
        self.rotation = rotation
        x_centre = C.GRID_SIZE * x
        y_centre = C.GRID_SIZE * y
        if rotation == 1:
            x_centre += boardLen / 2 * C.GRID_SIZE
            y_centre += C.GRID_SIZE / 2
        if rotation == 2:
            y_centre += boardLen / 2 * C.GRID_SIZE
            x_centre += C.GRID_SIZE / 2
        super().__init__(sprite, center_x=x_centre, center_y=y_centre, scale=0.5)

class Single_master(Ship):
    pass

class Two_master(Ship):
    pass

class Three_master(Ship):
    pass
class Four_master(Ship):
    pass
