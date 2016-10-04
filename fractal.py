import turtle

frac = turtle.Turtle()

def draw_fractal(length, depth):
    

    if depth == 0:        
        frac.forward(length)
    else:
        draw_fractal(length / 3, depth - 1)
        frac.right(60)
        draw_fractal(length / 3, depth - 1)
        frac.left(120)
        draw_fractal(length / 3, depth - 1)
        frac.right(60)
        draw_fractal(length / 3, depth - 1)



draw_fractal(500, 4)
