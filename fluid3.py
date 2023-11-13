import numpy as np
from tkinter import Tk, ttk, Button, Label, Frame
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

xfig, yfig = 20, 11.25

#Creamos una clase de la aplicación
class UI(Frame):
    """Docstring."""
    #Parámetros generales referidos a la propia aplicación
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.parent = parent
        self.init_ui()
        
    #Función para cerrar aplicación
    def quit(self):
        return super().quit()
    
    #Inicializamos todos los elementos desde esta función
    def init_ui(self):
        def graphic():
            sc = scale.get()
            #Definimos el entorno de la gráfica
            fig, ax = plt.subplots(dpi=30, figsize=(sc*xfig, sc*yfig), facecolor='#00faafb7')
            plt.title('Gráfica en Tkinter con matplotlib', color='red',size=16,family='Arial') 
            plt.xlim(-14, 14)
            plt.ylim(-3, 3)
            ax.set_facecolor('black')
            ax.axhline(linewidth=2, color='r')
            ax.axvline(linewidth=2, color='r')
            ax.set_xlabel('Eje horizontal', color='black')
            ax.set_ylabel('Eje vertical', color='black')
            ax.tick_params(direction='out', length=6, width=2, colors='black',grid_color='r',grid_alpha=0.5)
        """Aqui colocariamos los widgets."""
        
        self.parent.title("Un titulo para la ventana")
        canvas = FigureCanvasTkAgg(fig, master=self.parent)
        canvas.get_tk_widget().grid(column=0, row=0, columnspan=3, padx=5, pady=5)
        scale = ttk.Scale(self.parent, to=10, from_=-10, orient='horizontal',length=400)
        scale.grid(column=1,row=0)
        Button(self.parent, text='Graphic data', width=30, bg='magenta',fg='white',command=graphic).grid(column=0,row=1,pady=5)
        Button(self.parent, text='Quit', width=30, bg='magenta', fg='white', command=quit).grid(column=0, row=1, pady=5)

#Creamos una instancia para ejecutar la aplicación
if __name__ == "__main__":
    ROOT = Tk()
    ROOT.geometry("3200x1800")
    APP = UI(parent=ROOT)
    APP.mainloop()
    ROOT.destroy()