import pygame

class Snake:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        self.length = 1
        self.direction = "RIGHT"
        self.body = [(x, y)]

    def move(self):
        if self.direction == "UP":
            self.y -= 10
        elif self.direction == "DOWN":
            self.y += 10
        elif self.direction == "LEFT":
            self.x -= 10
        elif self.direction == "RIGHT":
            self.x += 10
        self.body.append((self.x, self.y))
        if len(self.body) > self.length:
            del self.body[0]

    def change_direction(self, direction: str):
        if direction == "UP" and self.direction != "DOWN":
            self.direction = direction
        elif direction == "DOWN" and self.direction != "UP":
            self.direction = direction
        elif direction == "LEFT" and self.direction != "RIGHT":
            self.direction = direction
        elif direction == "RIGHT" and self.direction != "LEFT":
            self.direction = direction

    def eat(self, food):
        if self.x == food.x and self.y == food.y:
            self.length += 1  # Increment the length by 1 when the snake eats the food
            return True
        return False

    def check_collision(self):
        if (self.x, self.y) in self.body[:-1]:
            return True

        # Wrap around to the opposite side of the frame
        if self.x < 0:
            self.x = 800  # Assuming frame width is 800
        elif self.x >= 800:
            self.x = 0
        elif self.y < 0:
            self.y = 600  # Assuming frame height is 600
        elif self.y >= 600:
            self.y = 0

        return False
    
    def draw(self, screen):
        for segment in self.body:
            pygame.draw.rect(screen, (0, 255, 0), (segment[0], segment[1], 10, 10))
