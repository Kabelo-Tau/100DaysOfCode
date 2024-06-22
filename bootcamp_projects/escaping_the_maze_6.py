# Day 6 was about practicing functions and while loops.
# Maze project completed using Reeborg's Wolrd.

#Follow the below link to run the code
#https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds/menus/reeborg_intro_en.json&name=Maze&url=worlds/tutorial_en/maze1.json

def turn_right():
    for _ in range(3):
        turn_left()

while front_is_clear():
    move()
turn_left()

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
