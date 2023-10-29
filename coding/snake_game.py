import curses
import random

s = curses.initscr()
curses.curs_set(0)
sh, sw = s.getmaxyx()
w = curses.newwin(sh, sw, 0, 0)
w.keypad(1)
w.timeout(100)

snk_x = sw // 4
snk_y = sh // 2
snake = [[snk_y, snk_x], [snk_y, snk_x - 1], [snk_y, snk_x - 2]]

foods = [[sh // 2, sw // 2]]
w.addch(int(foods[0][0]), int(foods[0][1]), curses.ACS_PI)

super_fruit = [sh // 4, sw // 4]
w.addch(
    int(super_fruit[0]), int(super_fruit[1]), curses.ACS_DIAMOND
)  # super fruit is represented by a diamond

score = 0

key = curses.KEY_RIGHT

while True:
    next_key = w.getch()
    key = key if next_key == -1 else next_key

    if snake[0][0] in [0, sh] or snake[0][1] in [0, sw] or snake[0] in snake[1:]:
        curses.endwin()
        quit()

    new_head = [snake[0][0], snake[0][1]]

    if key == curses.KEY_DOWN:
        new_head[0] += 1
    if key == curses.KEY_UP:
        new_head[0] -= 1
    if key == curses.KEY_LEFT:
        new_head[1] -= 1
    if key == curses.KEY_RIGHT:
        new_head[1] += 1

    snake.insert(0, new_head)

    # Regular fruit intake
    if snake[0] in foods:
        score += 1
        foods.remove(snake[0])
        foods.append(
            [random.randint(1, sh - 1), random.randint(1, sw - 1)]
        )  # respawning the eaten food
        for food in foods:
            w.addch(int(food[0]), int(food[1]), curses.ACS_PI)
    # Super fruit intake
    elif snake[0] == super_fruit:
        score += 5
        super_fruit = []
        for _ in range(10):  # to grow the snake by 10 points
            tail = snake.pop()
            snake.insert(0, [tail[0], tail[1]])
        super_fruit = [random.randint(1, sh - 1), random.randint(1, sw - 1)]
        w.addch(
            int(super_fruit[0]), int(super_fruit[1]), curses.ACS_DIAMOND
        )  # respawn the super fruit
    else:
        tail = snake.pop()
        w.addch(int(tail[0]), int(tail[1]), " ")
    w.addch(int(snake[0][0]), int(snake[0][1]), curses.ACS_CKBOARD)
    w.addstr(0, sw - 10, "Score: " + str(score))  # shows the score
