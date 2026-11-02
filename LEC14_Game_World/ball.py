from pico2d import get_canvas_width, load_image

import game_world


class Ball:
    image = None
    SPEED = 10  # Pixels per update.
    RADIUS = 20.5

    def __init__(self, x, y, direction):
        if Ball.image is None:
            Ball.image = load_image('ball41x41.png')
        self.x, self.y = x, y
        self.dir = direction

    def update(self):
        self.x += self.dir * self.SPEED
        if self.x < -self.RADIUS or self.x > get_canvas_width() + self.RADIUS:
            game_world.remove_object(self)

    def draw(self):
        self.image.draw(self.x, self.y)
