from tkinter import *

from state import State

SIZE = 4

def color(value):
    result = {'bg': 'white', 'fg': 'black'}
    if value == '':
        result['fg'] = 'black'
    elif value == 2:
        result['bg'] = 'yellow'
    elif value == 4:
        result['bg'] = 'green'
    elif value == 8:
        result['bg'] = 'blue'
    elif value == 16:
        result['bg'] = 'purple'
    else:
        result['bg'] = 'red'
    return result


if __name__ == '__main__':
    root = Tk()

    state = State(start=True)
    labels = []

    scores = Label(root, width=16, height=2, text=int(state.scores), font="Arial 32")
    scores.pack()

    def draw():
        for row in state.data:
            frame = Frame(root)
            labels_row = []
            for value in row:
                value = int(value) if value else ''
                label = Label(frame, width=4, height=2, **color(value), text=value, font="Arial 32")
                label.pack(side=LEFT)
                labels_row.append(label)
            frame.pack()
            labels.append(labels_row)

    draw()

    counter = 0

    def redraw():
        scores.config(text=int(state.scores))

        for row in range(SIZE):
            for col in range(SIZE):
                value = state.data[row][col]
                value = int(value) if value else ''
                labels[row][col].config(text=value, **color(value))


    def up(event):
        state.up()
        redraw()


    def down(event):
        state.down()
        redraw()


    def left(event):
        state.left()
        redraw()


    def right(event):
        state.right()
        redraw()


    root.bind('<Up>', up)
    root.bind('<Down>', down)
    root.bind('<Left>', left)
    root.bind('<Right>', right)

    root.mainloop()
