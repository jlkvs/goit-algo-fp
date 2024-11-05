import turtle
import math

def draw_pythagoras_tree(t, branch_length, level, angle=45):
    if level == 0:
        return
    
    t.forward(branch_length)

    t.left(angle)
    draw_pythagoras_tree(t, branch_length * math.sqrt(2) / 2, level - 1, angle)

    t.right(2 * angle)
    draw_pythagoras_tree(t, branch_length * math.sqrt(2) / 2, level - 1, angle)

    t.left(angle)
    t.backward(branch_length)

def setup_pythagoras_tree(level, initial_length=100):
    screen = turtle.Screen()
    screen.title("Pythagoras Tree Fractal")
    screen.bgcolor("white")

    t = turtle.Turtle()
    t.speed("fastest")  #
    t.left(90)          
    t.penup()
    t.goto(0, -200)     
    t.pendown()
    
    draw_pythagoras_tree(t, initial_length, level)
    
    screen.mainloop()

if __name__ == "__main__":
    level = int(input("Введіть рівень рекурсії для дерева Піфагора: "))
    setup_pythagoras_tree(level)
