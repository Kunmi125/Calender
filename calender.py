from tkinter import *
import calender

def show_calender():
    new_window = Tk()
    window.geometry("500x600")
    window.configure(background = "green")

    fetch_year = int(e1.get())
    cal = calender.calender(fetch_year)
    year = Text(new_window, font = "consolas 10 bold")
    year.insert(END, cal)
    year.grid(row = 5, columns = 1, padx = 20)

    new_window.mainloop()




if __name__ == "__main__":
    window = Tk()

    window.geometry("400x400")
    window.configure(background = "Orange")

    l1 = Label(window, text = "Calender")

    l2 = Label(window, text = "Enter year")

    b1 = Button(window, text = "Show calender", command = show_calender)

    b2 = Button(window, text = "Exit", command = exit)

    e1 = Entry(window)

    #positions
    l1.grid(rows = 1, columns = 1)
    l2.grid(rows = 2, columns = 1)

    b1.grid(rows = 3, columns = 1)
    b2.grid(rows = 4, columns = 1)

    e1.grid(rows = 5, columns = 1)

    window.mainloop()