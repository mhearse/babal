#!/usr/bin/env python

import Tkinter as tk
import time

root = tk.Tk()
canvas = tk.Canvas(root)
canvas.pack()

canvas.create_polygon(
    [
        50,50,
        100,50,
        125,200,
        25,200
    ],
    tags = 'babal'
)

for _ in range(50):
    canvas.move('babal', 0, 5)
    canvas.update()
    time.sleep(0.05)

root.mainloop()
