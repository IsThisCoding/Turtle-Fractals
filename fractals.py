def levy_c_curve(t: turtle.Turtle, length: float, level: int) -> None:
    if level == 0:
        t.forward(length)
    else:
        t.right(45)
        levy_c_curve(t, length / math.sqrt(2), level - 1)
        t.left(90)
        levy_c_curve(t, length / math.sqrt(2), level - 1)
        t.right(45)
