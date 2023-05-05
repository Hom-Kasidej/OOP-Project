import tkinter as tk

# Create the main window
root = tk.Tk()

# Create a frame to contain the canvas and scrollbar
frame = tk.Frame(root)
frame.pack(fill=tk.BOTH, expand=1)

# Create a canvas with a scrollbar
canvas = tk.Canvas(frame)
scrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL, command=canvas.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
canvas.configure(yscrollcommand=scrollbar.set)

# Add widgets to the canvas
for i in range(50):
    label = tk.Label(canvas, text=f"Label {i}")
    canvas.create_window((0, i*20), window=label, anchor=tk.NW)

# Configure the canvas to have a fixed size and to expand with the frame
canvas.configure(scrollregion=canvas.bbox("all"), width=200, height=200)

# Add the frame to the window
root.mainloop()
