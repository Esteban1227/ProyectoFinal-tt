from tkinter import *
import tkinter
def main():
    options = {
            "planesAvailable":[
                [
                    "Nombre del avion",
                    "Estado de disponibilidad",
                    "Ultimo mantenimiento",
                    "precio de alquiler"
                ]
            ],
            "planesBusy":[
                [
                    "Nombre del avion",
                    "Estado de disponibilidad",
                    "Ultimo mantenimiento",
                    "precio de alquiler"
                ]
            ],
            "hangarsAvailable":[
                [
                    "Numero del hangar",
                    "Estado de disponibilidad",
                    "precio de alquiler",
                    "medidas"
                ]
            ],
            "hangarsBusy":[
                [
                    "Numero del hangar",
                    "Estado de disponibilidad",
                    "precio de alquiler",
                    "medidas"
                ]
            ]
        }
    root = Tk()
    tittle = Label(root, text="JETT")
    cuestion = Label(root, text="¿Como desea ingresar")
    btonAdmin = Button(root, text="Administrador", command= lambda: menuAdmin(options, root))
    btonUser = Button(root, text="Usuario", command= lambda: menuUser(options, root))
    tittle.pack()
    cuestion.pack()
    btonAdmin.pack()
    btonUser.pack()
    root.mainloop()

""" def counter(add):
    if(add):
        message =+ 1
    else:
        message = 0
    return message """

def add(root, rootClose, optionsFpecific, entryName, entrySate, entryMaintenance, entryPrice):
    close(rootClose)
    optionsFpecific.append([entryName, entrySate, entryMaintenance, entryPrice])
    frame = Frame(root)
    labaelName = Label(frame, text=entryName)
    btnMore = Button(frame, text="Ver mas")
    labaelName.pack()
    btnMore.pack()
    frame.pack()
    print(optionsFpecific)


def menuAdmin(options, rootClose):
    close(rootClose)
    rootAdmin = Tk()
    tittle = Label(rootAdmin, text="JETT")
    planesAvailableFrame = Frame(rootAdmin)
    subTittle = Label(planesAvailableFrame, text="Aviones Disponibles")
    btnAdd = Button(planesAvailableFrame, text="Agregar un nuevo avion", command= lambda: menuCreate(planesAvailableFrame, options["planesAvailable"]))
    tittle.pack()
    planesAvailableFrame.pack()
    subTittle.pack()
    btnAdd.pack()
    rootAdmin.mainloop()

def menuCreate(root, optionsFpecific):
    rootCreate = Tk()
    tittle = Label(rootCreate, text="JETT")
    labelEntryName = Label(rootCreate, text="Nombre")
    entryName = Entry(rootCreate)
    labelEntryState = Label(rootCreate, text="Estado de disponibilidad")
    entryState = Entry(rootCreate)
    labelEntryMaintenance = Label(rootCreate, text="Ultimo Mantenimiento")
    entryMaintenance = Entry(rootCreate)
    labelEntryPrice = Label(rootCreate, text="Precio")
    entryPrice = Entry(rootCreate)
    btnAccept = Button(rootCreate, text="Aceptar", command= lambda: add(root, rootCreate, optionsFpecific, entryName.get(), entryState.get(), entryMaintenance.get(), entryPrice.get()))
    tittle.pack()
    labelEntryName.pack()
    entryName.pack()
    labelEntryState.pack()
    entryState.pack()
    labelEntryMaintenance.pack()
    entryMaintenance.pack()
    labelEntryPrice.pack()
    entryPrice.pack()
    btnAccept.pack()


def close(root):
    root.destroy()




def menuUser(options):
    root = Tk()
    tittle = Label(root, text="JETT")

def modify(optionsFpecific, number):
    # optionsFpecific[number]
    # optionsFpecific[0] = input("Nombre")
    # optionsFpecific[1] = input("Nombre")
    # optionsFpecific[2] = input("Nombre")
    # optionsFpecific[3] = input("Nombre")+
    pass


def delete():
    pass

main()