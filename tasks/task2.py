import turtle
import math

def draw_tree(t, branch_length, depth):
    if depth > 0:
        t.forward(branch_length)
        t.left(45)
        draw_tree(t, branch_length * math.sqrt(2)/2, depth - 1)
        t.right(90)
        draw_tree(t, branch_length * math.sqrt(2)/2, depth - 1)
        t.left(45)
        t.backward(branch_length)

def main():
    turtle_speed = 10  
    initial_length = 80  
    depth = int(input("Введіть рівень рекурсії для дерева Піфагора: "))
    
    print(f"Малюємо для глибини рекурсії {depth}")
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.speed(turtle_speed)
    draw_tree(t, initial_length, depth)
    myWin.exitonclick()

if __name__ == "__main__":
    main()