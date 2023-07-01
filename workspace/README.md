Based on the requirements, here are the core classes, functions, and methods that will be necessary for the Snake game:

1. `SnakeGame` class:
   - `__init__(self, width: int, height: int)` - Initializes the Snake game with the specified width and height.
   - `start(self)` - Starts the Snake game.
   - `update(self)` - Updates the game state.
   - `draw(self)` - Draws the game on the screen.
   - `handle_input(self, key: str)` - Handles user input for controlling the snake.
   - `game_over(self)` - Handles the game over condition.

2. `Snake` class:
   - `__init__(self, x: int, y: int)` - Initializes the Snake with the specified starting position.
   - `move(self)` - Moves the snake in the current direction.
   - `change_direction(self, direction: str)` - Changes the direction of the snake.
   - `eat(self)` - Increases the length of the snake when it eats something.
   - `check_collision(self)` - Checks if the snake has collided with itself or the boundaries of the screen.

3. `Food` class:
   - `__init__(self, x: int, y: int)` - Initializes the food with the specified position.
   - `draw(self)` - Draws the food on the screen.

Now, let's proceed with creating the necessary files and writing the code.

**game.py**
