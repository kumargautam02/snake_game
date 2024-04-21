import pygame
import random
from snake_body import Snake_Body

pygame.init()
win = pygame.display.set_mode((500, 500))

pygame.display.set_caption("first pygame")



def update_update_new_circle_location():
    return (random.choice(range(450)),random.choice(range(450)))


location = update_update_new_circle_location()
print("this is first location", location)
x = 50
y = 50
width = 8
height = 6
vel = 2
run = True
move_direction = x
snake = Snake_Body(x,y,width,height)
# print(*snake_body.get_snake_body())
snake_color , snake_body= snake.get_snake_body()
print(snake_color,snake_body)

while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        print(event)

    # move_direction += vel * 2
    keys = pygame.key.get_pressed()



    if keys[pygame.K_LEFT] and x >10:
        snake.x_axis -= vel*5
        # move_direction = x
    if keys[pygame.K_RIGHT] and x<450:
        snake.x_axis += vel*5
        # move_direction = x
    if keys[pygame.K_UP] and y > 10:
        snake.y_axis -= vel*5
        # move_direction = y
    if keys[pygame.K_DOWN] and y<450:
        snake.y_axis += vel*5
        # move_direction = y
    win.fill((0,0,0))

    snake_color, snake_body = snake.get_snake_body()
    print(snake_color, snake_body)

    pygame.draw.rect(win, snake_color, snake_body)
    print("here is x", x, y)
    if (abs(snake.x_axis - location[0]) < 6) and (abs(snake.y_axis - location[1]) < 6):
        print("yes##########################################################################################################")
        location = update_update_new_circle_location()
        snake.snake_width += 200
        # snake.snake_height += 20
        snake.color = (random.choice(range(255)), random.choice(range(255)),0)
    pygame.draw.circle(win, (0, 255, 0),location , (5))
    pygame.display.update()

#

pygame.quit()