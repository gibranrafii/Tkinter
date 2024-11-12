#Example:
import tkinter as tk

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()
bottomframe = tk.Frame(root)
bottomframe.pack(side=tk.BOTTOM)
redbutton = tk.Button(frame, text="Red", fg="red")
redbutton.pack(side=tk.LEFT)
greenbutton = tk.Button(frame, text="Brown", fg="brown")
greenbutton.pack(side=tk.LEFT)
bluebutton = tk.Button(frame, text="Blue", fg="blue")
bluebutton.pack(side=tk.LEFT)
blackbutton = tk.Button(bottomframe, text="Black", fg="black")
blackbutton.pack(side=tk.BOTTOM)
root.mainloop()
