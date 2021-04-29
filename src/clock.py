from datetime import datetime
import tkinter as tk

class Clock:
    def __init__(self, master):
        self.clockFrame = tk.Frame(master)

        self.clockFrame.rowconfigure(0, weight=1)
        self.clockFrame.columnconfigure(0, weight=1)
        self.clockFrame.columnconfigure(1, weight=1)

        font16 = 'Heveltica 16'
        font24 = 'Heveltica 24'

#hours
        self.timeLabel = tk.LabelFrame(self.clockFrame, text = 'Bieżąca godzina:', font = font16, bg = 'green', fg='black')
        self.timeLabel.grid(row=0, column=0, sticky = 'news')

        self.currentTime = datetime.now().strftime('%H:%M:%S')
        self.currentTimeLabel = tk.Label(self.timeLabel, text=self.currentTime, font=font24,  bg = 'green', fg='black')
        self.currentTimeLabel.pack()

#date
        self.dataLabel = tk.LabelFrame(self.clockFrame, text = 'Bieżąca data:', font = font16, bg = 'green', fg='black')
        self.dataLabel.grid(row=0, column=1, sticky='news')

        self.currentDate = datetime.today().strftime('%d-%m-%Y')
        self.currentDateLabel = tk.Label(self.dataLabel, text = self.currentDate, font=font24,  bg = 'green', fg='black')
        self.currentDateLabel.pack()

        self.update()


    def update(self):

        self.currentTime = datetime.now().strftime('%H:%M:%S')
        self.currentTimeLabel.config(text = self.currentTime)

        self.currentDate = datetime.today().strftime('%d-%m-%Y')
        self.currentDateLabel.config(text = self.currentDate)

        self.clockFrame.after(1000, self.update)


if __name__ == '__main__':
    testApp = tk.Tk()
    testApp.geometry('500x100')
    clock = Clock(testApp)
    clock.clockFrame.pack(expand=1, fill='both')
    testApp.mainloop()