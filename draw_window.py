import PIL
from PIL import ImageTk, Image, ImageDraw
from tkinter import *
import main

width = 210
height = 242
center = height//2
white = 255

def save():
    path_to_file = "C:/python_files/saved_images/image.png"
    image1.save(path_to_file)
    cv1.create_text((105, 20), text='Walrus!')
    #root.quit()

def reset():
    cv.delete('line')
    cv1.delete('number')
    draw.rectangle([(0, 0), (210, 242)], fill='white')

def paint(event):
    # python_green = "#476042"
    x1, y1 = (event.x - 1), (event.y - 1)
    x2, y2 = (event.x + 1), (event.y + 1)
    cv.create_line(x1, y1, x2, y2, 
        fill="black", width=15, capstyle=ROUND, smooth=TRUE, splinesteps=36, tags='line')
    draw.ellipse([x1-10, y1-10, x2+10, y2+10], fill="black")

root = Tk()

reset_button = Button(root, text='reset', command=reset)
reset_button.grid(row=0, column=0)

save_button = Button(root, text='save', command=main.save)
save_button.grid(row=0, column=1)

# Tkinter create a canvas to draw on
cv = Canvas(root, width=width, height=height, bg='white')
cv1 = Canvas(bg='grey', highlightthickness=2)

# PIL create an empty image and draw object to draw on
# memory only, not visible
image1 = PIL.Image.new("L", (width, height), white)
draw = ImageDraw.Draw(image1)


# do the Tkinter canvas drawings (visible)
# cv.create_line([0, center, width, center], fill='green')

cv.grid(row=1, columnspan=2)
cv.bind("<B1-Motion>", paint)
cv1.bind("<B1-Motion>", paint)

# do the PIL image/draw (in memory) drawings
# draw.line([0, center, width, center], green)

# PIL image can be saved as .png .jpg .gif or .bmp file (among others)
# filename = "my_drawing.png"
cv.create_window((107, 224), height=40, width=214, window=cv1)

root.mainloop()
