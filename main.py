import tkinter as tk
#Main Tkinter file (will have main GUI functionality, button presses will use Functions created in other files ex. ping.py)

root = tk.Tk()
root.title("HelpDesk Toolkit")
root.geometry("800x500")

quit_button = tk.Button(root, text = "Quit", command = root.destroy)
quit_button.place(x=700,y=425)
root.mainloop()
