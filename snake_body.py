

class Snake_Body:
    def __init__(self, x_axis, y_axis, snake_width, snake_height):
        self.color = (255,0,0)
        self.x_axis = x_axis
        self.y_axis = y_axis
        self.snake_width = snake_width
        self.snake_height = snake_height

    def get_snake_body(self):
        return self.color,(self.x_axis, self.y_axis, self.snake_width, self.snake_width)
