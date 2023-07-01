import pygame
from pygame.locals import *
from snake import Snake
from food import Food
import tkinter as tk
from tkinter import messagebox

def popup_message():
        root = tk.Tk()
        root.withdraw()
        messagebox.showinfo("Game Over", "You died!")
        return messagebox.askyesno("Play Again", "Do you want to play again?")

class SnakeGame:
    def __init__(self, width: int, height: int):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()
        self.snake = Snake(width // 2, height // 2)
        self.food = Food()
        self.is_running = False
        self.score = 0


    def start(self):
        self.is_running = True
        while self.is_running:
            self.update()
            self.draw()
            self.handle_events()
            self.clock.tick(10)

    def handle_events(self):
       for event in pygame.event.get():
           if event.type == pygame.KEYDOWN:
              self.handle_input(event.key)
           if self.snake.check_collision():
              self.game_over()


    def update(self):
        self.snake.move()
        if self.snake.check_collision():
            self.game_over()
        if self.snake.eat(self.food):
            self.food = Food()
            self.score += 1  # Increase score when the snake eats food
        

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.snake.draw(self.screen)
        self.food.draw(self.screen)
        pygame.display.flip()

    def handle_input(self, key: int):
        if key == pygame.K_UP:
            self.snake.change_direction("UP")
        elif key == pygame.K_DOWN:
            self.snake.change_direction("DOWN")
        elif key == pygame.K_LEFT:
            self.snake.change_direction("LEFT")
        elif key == pygame.K_RIGHT:
            self.snake.change_direction("RIGHT")


    def game_over(self):
        if popup_message():
            self.snake = Snake(self.width // 2, self.height // 2)
            self.food = Food()
            self.score = 0  # Reset score when starting a new game
        else:
            self.is_running = False

            # Rest of the code...
            high_scores = []  # List to store high scores
            with open("high_scores.txt", "a") as file:
                file.write(str(self.score) + "\n")  # Append the score to a file
            with open("high_scores.txt", "r") as file:
                for line in file:
                    high_scores.append(int(line.strip()))  # Read scores from the file
            high_scores.sort(reverse=True)  # Sort scores in descending order
            top_scores = high_scores[:10]  # Get the top 10 scores
            print("High Scores:")
            for i, score in enumerate(top_scores, start=1):
                print(f"{i}. {score}")

            pygame.quit()  # Quit the game
        

if __name__ == "__main__":
    game = SnakeGame(800, 600)
    game.start()
    pygame.quit()
