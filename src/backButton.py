import tkinter as tk




class BackButton:
    def __init__(self, master, ifMainPage):
        font='Heveltica 20'
        self.backButton = tk.Button(master, text = 'test', font=font)

        self.ifMainPage = ifMainPage

        self.updateFunction()

    def updateFunction(self):
        if self.ifMainPage ==True:
            self.backButton.config(command = self.powerOff)

        if self.ifMainPage ==False:
            self.backButton.config(command = self.goBack)

    def powerOff(self):
        print('poweroff')

    def goBack(self):
        print('goback')



'''

    def powerOffFunction(self):
        print('poweroff')

    def goBackFunction(self):
        print('goback')

    def updateBackButtonSymbol(self):
        #backbuttonsymbol needs to be update after every change of displayed page
        pass


'''




if __name__ == '__main__':
    testApp = tk.Tk()
    testApp.geometry('500x100')
    backButton = BackButton(testApp, False)
    backButton.backButton.pack()
    testApp.mainloop()