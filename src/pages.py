import tkinter as tk
import os
import sys

class Viewer(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)

        containter = tk.Frame(self)
        containter.rowconfigure(0, weight=1)
        containter.columnconfigure(0, weight=1)
        containter.pack(expand=True, fill='both')

        self.pages={}

        for i in (StartPage,
                  InfoPage,
                  ReportsPage,
                  SettingsPage,
                  PowerPage):
            page = i(containter, self)
            page.grid(row=0, column=0, sticky='news')
            self.pages[i] = page

        self.show(StartPage)

    def show(self, pageName):
        self.pages[pageName].lift()


    def powerOff(self):
        self.destroy()



class BackButton(tk.Button):
    def __init__(self, controller):
        tk.Button.__init__(self, text='BACK',command=lambda: controller.show(StartPage))





class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.LabelFrame.__init__(self, parent, bg = 'lightgrey', text='START PAGE', fg='black')

        for i in range(0,7):
            self.rowconfigure(i, weight=1)

        for i in range(0,6):
            self.columnconfigure(i, weight=1)






        btn1 = tk.Button(self, text='INFO', command=lambda: controller.show(InfoPage))
        btn1.grid(column=1,row=1, sticky='news')

        btn2 = tk.Button(self, text='REPORTS', command=lambda: controller.show(ReportsPage))
        btn2.grid(column=1, row=3, sticky='news')

        btn3 = tk.Button(self, text='SETTINGS', command=lambda: controller.show(SettingsPage))
        btn3.grid(column=1, row=5, sticky='news')

        btn4 = tk.Button(self, text='--------', command=None)
        btn4.grid(column=3, row=1, sticky='news')

        btn5 = tk.Button(self, text='--------', command=None)
        btn5.grid(column=3, row=3, sticky='news')

        btn6 = tk.Button(self, text='POWER', command=lambda : controller.show(PowerPage))
        btn6.grid(column=3, row=5, sticky='news')

class InfoPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.LabelFrame.__init__(self, parent, bg = 'grey', text='INFO')

        #btn1= tk.Button(self, text='go to page2', command = lambda:controller.show(Page2))
        #btn1.pack()


        #label=tk.Label(self, text='page1')sad_but_true

        #label.pack()

class ReportsPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.LabelFrame.__init__(self,parent, bg = 'grey', text='REPORTS')

class SettingsPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.LabelFrame.__init__(self,parent, bg = 'grey', text='SETTINGS')


class PowerPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.LabelFrame.__init__(self,parent, bg = 'grey', text='POWER')

        questionLabel = tk.Label(self, text='Do you want to power off???', font='Heveltica, 26', bg='grey')
        questionLabel.pack(side='top')

        btn1 = tk.Button(self, text='YES', font ='Arial, 30', command=lambda: os.system('poweroff'))
        btn1.pack(side='left', padx=100)

        btn2 = tk.Button(self, text='NO', font='Arial, 30', command=lambda:controller.show(StartPage))
        btn2.pack(side='right', padx=100)










######### test app ######################################################
if __name__ == '__main__':
    App = tk.Tk()
    App.geometry('1000x1000')
    viewer = Viewer()
    viewer.pack(fill='both', expand=True)


    App.mainloop()