import tkinter as tk

root = tk.Tk()
root.title("Simple House Canvas")

# Canvas setup
canvas = tk.Canvas(root, width=500, height=400, bg="deep sky blue")
canvas.pack()

# Grass / Ground
canvas.create_rectangle(0, 300, 500, 400, fill="forest green", outline="")

# Main House Body (Wall)
canvas.create_rectangle(150, 180, 350, 300, fill="khaki", outline="brown", width=2)

# Rooftop (Triangle using polygon)
canvas.create_polygon(130, 180, 250, 80, 370, 180, fill="crimson", outline="dark red", width=2)

# Main Door
canvas.create_rectangle(220, 230, 280, 300, fill="sienna", outline="black", width=2)
# Door Handle
canvas.create_oval(270, 265, 276, 271, fill="gold", outline="")

# Left Window
canvas.create_rectangle(170, 200, 210, 240, fill="light yellow", outline="navy", width=2)
canvas.create_line(190, 200, 190, 240, fill="navy", width=2)  # Vertical frame
canvas.create_line(170, 220, 210, 220, fill="navy", width=2)  # Horizontal frame

# Right Window
canvas.create_rectangle(290, 200, 330, 240, fill="light yellow", outline="navy", width=2)
canvas.create_line(310, 200, 310, 240, fill="navy", width=2)  # Vertical frame
canvas.create_line(290, 220, 330, 220, fill="navy", width=2)  # Horizontal frame

# Sun
canvas.create_oval(400, 30, 460, 90, fill="gold", outline="orange", width=2)

root.mainloop()