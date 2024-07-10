import turtle


def koch_segment(t, length, level):
    if level == 0:
        t.forward(length)
    else:
        length /= 3.0
        koch_segment(t, length, level-1)
        t.left(60)
        koch_segment(t, length, level-1)
        t.right(120)
        koch_segment(t, length, level-1)
        t.left(60)
        koch_segment(t, length, level-1)

def koch_snowflake(t, length, level):
    for _ in range(3):
        koch_segment(t, length, level)
        t.right(120)

def main():
    level = int(input("Input recursion level: "))

    screen = turtle.Screen()
    screen.setup(width=800, height=800)
    screen.title("Koch Snowflake")
    screen.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)
    t.color("black")
    t.pensize(2)

    length = 300

    t.penup()
    t.goto(-length / 2, length / 2)
    t.pendown()

    koch_snowflake(t, length, level)

    t.hideturtle()
    screen.mainloop()

if __name__ == "__main__":
    main()