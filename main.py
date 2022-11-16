from tkinter import *
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
                # [
                #     "Numero del hangar",
                #     "Estado de disponibilidad",
                #     "precio de alquiler",
                #     "medidas"
                # ]
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

def counter(label, optionsSpecify, isPlanes):
    if(isPlanes):
        label["text"] = "Aviones disponibles("+str(len(optionsSpecify))+")"
    else: 
        label["text"] = "Hangares disponibles("+str(len(optionsSpecify))+")"

def add(root, rootClose, optionsSpecify, entryName, entrySate, entryMaintenance, entryPrice, labelCounter, isPlanes):
    close(rootClose)
    optionsSpecify.append([entryName, entrySate, entryMaintenance, entryPrice])
    frame = Frame(root)
    labaelName = Label(frame, text=entryName)
    btnMore = Button(frame, text="Ver mas")
    labaelName.pack()
    btnMore.pack()
    frame.pack()
    counter(labelCounter, optionsSpecify, isPlanes)


def menuAdmin(options, rootClose):
    close(rootClose)
    rootAdmin = Tk()
    tittle = Label(rootAdmin, text="JETT")
    planesAvailableFrame = Frame(rootAdmin, bg="blue", padx=5, pady=5)
    hangarsAvailableFrame = Frame(rootAdmin, bg="red", padx=5, pady=5)
    subTittle = Label(planesAvailableFrame, text="Aviones disponibles(0)")
    btnAddPlane = Button(planesAvailableFrame, text="Agregar un nuevo avion", command= lambda: menuAddPlane(planesAvailableFrame, options["planesAvailable"], subTittle))
    subTittle2 = Label(hangarsAvailableFrame, text="Hangares disponibles(0)")
    btnAddHangar = Button(hangarsAvailableFrame, text="Agregar un nuevo Hangar", command= lambda: menuAddHangar(hangarsAvailableFrame, options["hangarsAvailable"], subTittle2))
    tittle.pack()
    planesAvailableFrame.pack()
    hangarsAvailableFrame.pack()
    subTittle.pack()
    btnAddPlane.pack()
    subTittle2.pack()
    btnAddHangar.pack()
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
    btnAccept = Button(rootCreate, text="Aceptar", command= lambda: add(root, rootCreate, optionsFpecific, entryName.get(), entryState.get(), entryMaintenance.get(), entryPrice.get(), labelCounter, True))
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

def menuAddHangar(root, optionsFpecific, labelCounter):
    rootCreate = Tk()
    tittle = Label(rootCreate, text="JETT")
    labelEntryName = Label(rootCreate, text="Numero de hangar")
    entryName = Entry(rootCreate)
    labelEntryState = Label(rootCreate, text="Estado de disponibilidad")
    entryState = Entry(rootCreate)
    labelEntryMaintenance = Label(rootCreate, text="medidas")
    entryMaintenance = Entry(rootCreate)
    labelEntryPrice = Label(rootCreate, text="Precio")
    entryPrice = Entry(rootCreate)
    btnAccept = Button(rootCreate, text="Aceptar", command= lambda: add(root, rootCreate, optionsFpecific, entryName.get(), entryState.get(), entryMaintenance.get(), entryPrice.get(), labelCounter, False))
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
