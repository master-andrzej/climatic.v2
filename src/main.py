import tkinter as tk
import clock as cl
import pages as pg

App = tk.Tk()

#window settings#

App.geometry('1024x600')
App.resizable(0,0)

App.rowconfigure(0, weight=1)
App.rowconfigure(1, weight=30)

App.columnconfigure(0, weight=1)
App.columnconfigure(1, weight=2)
App.columnconfigure(2, weight=2)

#widgets
clock=cl.Clock(App).clockFrame
clock.grid(row=0, column=1, sticky='news', columnspan=2)

viewer = pg.Viewer()
viewer.grid(row=1, column=0, columnspan=3, sticky='news')

backButton = pg.BackButton(viewer)
backButton.grid(row=0, column=0, sticky='news')


if __name__ == '__main__':
    App.mainloop()