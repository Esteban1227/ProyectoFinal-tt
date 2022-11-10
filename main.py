from tkinter import *
import tkinter
def main():
    options = {
            "planesAvailable":[
                # [
                #     "Nombre del avion",
                #     "Estado de disponibilidad",
                #     "Ultimo mantenimiento",
                #     "precio de alquiler"
                # ]
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

def counter(label, optionsFpecific):
    print(optionsFpecific)
    label["text"] = "Aviones disponibles("+str(len(optionsFpecific))+")"

def add(root, rootClose, optionsFpecific, entryName, entrySate, entryMaintenance, entryPrice, labelCounter):
    close(rootClose)
    optionsFpecific.append([entryName, entrySate, entryMaintenance, entryPrice])
    frame = Frame(root)
    labaelName = Label(frame, text=entryName)
    btnMore = Button(frame, text="Ver mas")
    labaelName.pack()
    btnMore.pack()
    frame.pack()
    counter(labelCounter, optionsFpecific)


def menuAdmin(options, rootClose):
    close(rootClose)
    rootAdmin = Tk()
    tittle = Label(rootAdmin, text="JETT")
    planesAvailableFrame = Frame(rootAdmin)
    subTittle = Label(planesAvailableFrame, text="Aviones disponibles(0)")
    subTittle["text"] = counter(subTittle, options["planesAvailable"])
    btnAdd = Button(planesAvailableFrame, text="Agregar un nuevo avion", command= lambda: menuAddPlane(planesAvailableFrame, options["planesAvailable"], subTittle))
    tittle.pack()
    planesAvailableFrame.pack()
    subTittle.pack()
    btnAdd.pack()
    rootAdmin.mainloop()

def menuAddPlane(root, optionsFpecific, labelCounter):
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
    btnAccept = Button(rootCreate, text="Aceptar", command= lambda: add(root, rootCreate, optionsFpecific, entryName.get(), entryState.get(), entryMaintenance.get(), entryPrice.get(), labelCounter))
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