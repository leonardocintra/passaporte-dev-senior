from tkinter import Tk, Canvas, mainloop

from gameoflife.core import GameOfLife

W = 480
H = 270
SCALE = 5

def show(canvas, coords):
    canvas.create_rectangle(0, 0, W, H, width=0, fill='white')

    for c in coords:
        x0, y0 = c * SCALE
        x1, y1 = c * SCALE + (SCALE, SCALE)

        canvas.create_rectangle(x0, y0, x1, y1, width=0, fill='black')


def gui():
    gol = GameOfLife(W // SCALE, H // SCALE)

    main_window = Tk()
    canvas = Canvas(main_window, width=480, height=270)
    canvas.pack()

    def run(*args):
        show(canvas, next(gol))
        main_window.after(10, run)

    main_window.after(0, run)
    mainloop()
