from tkinter import *; import math; import random; import time

root=Tk()
root.geometry("2366x720")

mouseY, mouseX = 0,0
Objectx, Objecty, Objectxvel, Objectyvel, ObjectMass, ObjectR = [],[],[],[],[],[]

for i in range(3):   # numero objetos
    Objectx.append(random.randint(100,1000))
    Objecty.append(random.randint(100,700))
    Objectxvel.append(0)                #Objectxvel.append(random.randint(-30,30) / 100) 
    Objectyvel.append(0)                #Objectyvel.append(random.randint(-30,30) / 100)
    ObjectMass.append(random.randint(500,20000))
    ObjectR.append(ObjectMass[i]**0.3333333)

canvas=Canvas(root, bg="white")
canvas.pack(fill="both", expand=True)

def mousePos(event):
    global mouseX; global mouseY
    mouseX,mouseY = event.x, event.y

root.bind("<Motion>", mousePos)
mouseMass=500000 # masa del circulo rojo. No es importante pero se puede cambiar por diversion
G = 6.67428e-11

while True:
    canvas.delete("all")
    for Num in range(len(Objectx)):
        angle = math.atan2(mouseY-Objecty[Num], mouseX-Objectx[Num])
        distance = math.sqrt( ((mouseX-Objectx[Num])**2) + ((mouseY-Objecty[Num])**2) )
        Objectxvel[Num] += math.cos(angle) * G * ObjectMass[Num] * mouseMass / (distance ** 2)
        Objectyvel[Num] += math.sin(angle) * G * ObjectMass[Num] * mouseMass / (distance ** 2)
        Objectx[Num] += Objectxvel[Num] 
        Objecty[Num] += Objectyvel[Num]

        if distance < 20:
            if distance < 15:
                Objectx[Num] -= Objectxvel[Num] * 1.5
                Objecty[Num] -= Objectyvel[Num] * 1.5
                Objectxvel[Num] = 0
                Objectyvel[Num] = 0
            else:
                Objectx[Num] -= Objectxvel[Num] * 1.01
                Objecty[Num] -= Objectyvel[Num] * 1.01
                Objectxvel[Num] = 0
                Objectyvel[Num] = 0         

        for Num2 in range(len(Objectx)):
            angle = math.atan2(     Objectx[Num]-Objecty[Num2], Objecty[Num]-Objectx[Num2]  )
            distance = math.sqrt( ((Objectx[Num]-Objectx[Num2])**2) + ((Objecty[Num]-Objecty[Num2])**2) )
            try:
                Objectxvel[Num] += math.cos(angle) * G * ObjectMass[Num] * ObjectMass[Num2] / (distance ** 2)
                Objectyvel[Num] += math.sin(angle) * G * ObjectMass[Num] * ObjectMass[Num2] / (distance ** 2)
            except:
                pass

            Objectx[Num] += Objectxvel[Num] 
            Objecty[Num] += Objectyvel[Num]

            if distance < 20 and distance > 0:
                try:
                    Objectx[Num] -= Objectxvel
                    Objecty[Num] -= Objectyvel
                except:
                    pass
        sc = 1000 # Escala para el "vector velocidad"
        x, y, r, vx, vy = Objectx[Num], Objecty[Num], ObjectR[Num]//2, Objectxvel[Num], Objectyvel[Num] 
        canvas.create_oval(x+r, y+r, x-r, y-r, fill="black", width=0)
        canvas.create_line(x, y, x+sc*vx, y+sc*vy, arrow=LAST)

    oval1=canvas.create_oval(mouseX+15, mouseY+15, mouseX-15, mouseY-15, fill="red", width=0)
    root.update()