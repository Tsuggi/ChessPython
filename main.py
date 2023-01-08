from tkinter import *
from tkinter import ttk


root = Tk()
root.title("Chess Game")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)


blue_case = ttk.Style().configure('couleurBlue.TFrame', background='#4B7399', borderwidth=5, relief='raised')
white_case = ttk.Style().configure('couleurWhite.TFrame', background='#EAE9D2', borderwidth=5, relief='raised')


chess_board = []

for col in range(8):
    tab = []
    
    for row in range(8):
        if (row % 2) == 0: 
            tab.append(ttk.Frame(mainframe, width=100, height=100, style='couleurWhite.TFrame').grid(column=col, row=row))
        else:
            tab.append(ttk.Frame(mainframe, width=100, height=100, style='couleurBlue.TFrame').grid(column=col, row=row))
    
    chess_board.append(tab)
    
           

root.mainloop()
