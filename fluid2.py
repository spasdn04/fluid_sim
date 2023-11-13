import numpy as np
from tkinter import Tk, ttk, Button, Label, Frame, VERTICAL, Canvas
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

#Gráfica matplotlib
fig, ax = plt.subplots(dpi=30, figsize=(18,12), facecolor='#00faafb7')
plt.title('Gráfica en Tkinter con matplotlib', color='red',size=16,family='Arial')

plt.xlim(-14, 14)
plt.ylim(-3, 3)
ax.set_facecolor('black')
ax.axhline(linewidth=2, color='r')
ax.axvline(linewidth=2, color='r')
ax.set_xlabel('Eje horizontal', color='black')
ax.set_ylabel('Eje vertical', color='black')
ax.tick_params(direction='out', length=6, width=2, colors='black',grid_color='r',grid_alpha=0.5)


def graphic_data():
    level = scale.get()
    x = np.arange(-4*np.pi, 4*np.pi, 0.01)
    line = ax.plot(x, np.tanh(x+level),color='b',linestyle='solid')
    canvas.draw()
    label.config(text=level)
    line.set_ydata(np.sin(x)+10)
    root.after(150, graphic_data)
    

# Aplicación Tkinter
root = Tk()
root.geometry('1600x1000')

def quit():
    root.quit()

frame = Frame(root, bg='gray22',bd=3)
frame.grid(column=0,row=0)
# Agregar un Canvas al Frame para la gráfica
canvas_frame = Canvas(frame, bg='black', width=1500, height=900)
canvas_frame.grid(column=0, row=0, columnspan=3, padx=5, pady=5)

canvas = FigureCanvasTkAgg(fig, master=canvas_frame)
canvas_widget = canvas.get_tk_widget()
canvas_widget.pack(fill='both', expand=True)

# Agregar la barra de desplazamiento al Frame
scrollbar = ttk.Scrollbar(frame, orient=VERTICAL, command=canvas_frame.yview)
scrollbar.grid(column=3, row=0, rowspan=2, sticky='ns')
canvas_frame.config(yscrollcommand=scrollbar.set)

canvas = FigureCanvasTkAgg(fig,  master=canvas_frame)
canvas.get_tk_widget()

Button(frame, text='Graphic data', width=30, bg='magenta',fg='white',command=graphic_data).grid(column=0,row=1)
label = Label(frame, width=15)
label.grid(column=1,row=1)

scale = ttk.Scale(frame, to=10, from_=-10, orient='horizontal',length=400)
scale.grid(column=1, row=2)

style = ttk.Style()
style.configure('Horizontal.TScale', background='gray22')
style.configure("TScrollbar", arrowcolor="#0000ff", arrowsize=10, background="#00ff00", bordercolor="#ffffff", darkcolor="#ff0000", lightcolor="#ff0000", foreground="#ffff00", gripcount=5, troughcolor="#ff00ff")

Button(frame, text='Quit', width=30, bg='magenta',fg='white',command=quit).grid(column=0, row=2)

root.mainloop() 