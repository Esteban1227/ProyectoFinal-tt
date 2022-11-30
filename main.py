from tkinter import *
from datetime import date
import random

def randomNumber():
    numero = int(random.random() * 1000000000)
    return '{:,.2f}'.format(numero)
options = {
            "planesAvailable":[
                [
                    "La reina de los cielos",
                    True,
                    date.today(),
                    randomNumber()
                ],
                [
                    "Chancho",
                    True,
                    date.today(),
                    randomNumber()
                ],
                [
                    "Mapache",
                    True,
                    date.today(),
                    randomNumber()
                ],
                [
                    "Buff",
                    True,
                    date.today(),
                    randomNumber()
                ],
                [
                    "Ballena",
                    True,
                    date.today(),
                    randomNumber()
                ]
            ],
            "planesBusy":[
            ],
            "hangarsAvailable":[
                [
                    "Hangar-1",
                    True,
                    "500x500",
                    randomNumber()
                ],
                [
                    "Hangar-2",
                    True,
                    "500x500",
                    randomNumber()
                ],
                [
                    "Hangar-3",
                    True,
                    "500x500",
                    randomNumber()
                ],
                [
                    "Hangar-4",
                    True,
                    "500x500",
                    randomNumber()
                ],
                [
                    "Hangar-5",
                    True,
                    "500x500",
                    randomNumber()
                ],
            ],
            "hangarsBusy":[
            ]
        }

def main():
    root = Tk()
    tittle = Label(root, text="JETT")
    cuestion = Label(root, text="¿Como desea ingresar")
    btonAdmin = Button(root, text="Administrador", command= lambda: menuAdmin())
    btonUser = Button(root, text="Usuario", command= lambda: menuUser())
    tittle.pack()
    cuestion.pack()
    btonAdmin.pack()
    btonUser.pack()
    root.mainloop()

def menuAdmin():
    rootAdmin = Tk()
    tittle = Label(rootAdmin, text="JETT")
    tittle.pack()

    searchPlanesFrame = Frame(rootAdmin)
    searchPlanesLabel = Label(searchPlanesFrame, text="Escriba el nombre del avion que quiere editar")
    searchPlanesLabel.pack()
    searchPlanesEntry = Entry(searchPlanesFrame)
    searchPlanesEntry.pack()
    searchPlanesButton = Button(searchPlanesFrame, text="Buscar", command=lambda: searchPlane(options["planesAvailable"], searchPlanesEntry.get(), searchPlanesFrame, rootAdmin))
    searchPlanesButton.pack()
    searchPlanesFrame.pack()

    planesAvailableFrame = Frame(rootAdmin, bg="#D1DDFF", padx=5, pady=5)
    planesAvailableFrame.pack()
    labelCounterPlanes = Label(planesAvailableFrame, text=f"Aviones disponibles({len(options['planesAvailable'])})")
    showItems(options["planesAvailable"], planesAvailableFrame)
    btnSeeMorePlanes = Button(planesAvailableFrame, text="Mas Informacion", command= lambda: menuSeeMore(options["planesAvailable"]))
    labelCounterPlanes.pack()
    btnSeeMorePlanes.pack()

    planesBusyFrame = Frame(rootAdmin, bg="#D1DDFF", padx=5, pady=5)
    planesBusyFrame.pack()
    labelCounterPlanesBuy = Label(planesBusyFrame, text=f"Aviones Ocupados({len(options['planesBusy'])})")
    showItems(options["planesBusy"], planesBusyFrame)
    btnSeeMorePlanesBuy = Button(planesBusyFrame, text="Mas Informacion", command= lambda: menuSeeMore(options["planesBusy"]))
    labelCounterPlanesBuy.pack()
    btnSeeMorePlanesBuy.pack()

    searchHangarFrame = Frame(rootAdmin)
    searchHangarFrame.pack()
    searchHangarLabel = Label(searchHangarFrame, text="Escriba el nombre del hangar que quiere editar")
    searchHangarLabel.pack()
    searchHangarEntry = Entry(searchHangarFrame)
    searchHangarEntry.pack()
    searchHangarButton = Button(searchHangarFrame, text="Buscar", command=lambda: searchHangar(options["hangarsAvailable"], searchHangarEntry.get(), searchHangarFrame, rootAdmin))
    searchHangarButton.pack()

    hangarsAvailableFrame = Frame(rootAdmin, bg="#D1DDFF", padx=5, pady=5)
    hangarsAvailableFrame.pack()
    labelCounterHangars = Label(hangarsAvailableFrame, text=f"Hangares disponibles({len(options['hangarsAvailable'])})")
    showItems(options["hangarsAvailable"], hangarsAvailableFrame)
    btnSeeMoreHangars = Button(hangarsAvailableFrame, text="Mas Informacion", command= lambda: menuSeeMore(options["hangarsAvailable"]))
    labelCounterHangars.pack()
    btnSeeMoreHangars.pack()

    hangarsBusyFrame = Frame(rootAdmin, bg="#D1DDFF", padx=5, pady=5)
    hangarsBusyFrame.pack()
    labelCounterHangarsBusy = Label(hangarsBusyFrame, text=f"Hangares disponibles({len(options['hangarsBusy'])})")
    showItems(options["hangarsBusy"], hangarsBusyFrame)
    btnSeeMoreHangarsBusy = Button(hangarsBusyFrame, text="Mas Informacion", command= lambda: menuSeeMore(options["hangarsBusy"]))
    labelCounterHangarsBusy.pack()
    btnSeeMoreHangarsBusy.pack()
    
    rootAdmin.mainloop()

def searchPlane(optionsSpecify, searchedName, frame, rootClose):
    for i in optionsSpecify:
        if(searchedName.lower() == i[0].lower()):
            name = i[0]
            nameLabel = Label(frame, text=f"Nombre: {name}")
            nameLabel.pack()
            stateLabel = Label(frame)
            if(i[1]):
                stateLabel["text"] = "Estado: Activo"
            else:
                stateLabel["text"] = "Estado: Ocupado"
            stateLabel.pack()
            dateLabel = Label(frame, text=f"Tamaño: {i[2]}")
            dateLabel.pack()
            priceLabel = Label(frame, text=f"Precio: ${i[3]}")
            priceLabel.pack()
            btnEdit = Button(frame, text="Editar elemento", command=lambda: menuEdit(rootClose, optionsSpecify, name))
            btnEdit.pack()
            btnDelete = Button(frame, text="Elimar elemento", command=lambda: deleteElement(optionsSpecify, name, rootClose))
            btnDelete.pack()
            btnChangeState = Button(frame, text="Cambiar el estado", command=lambda: changeState(optionsSpecify, name, rootClose, options["planesBusy"]))
            btnChangeState.pack()

def searchHangar(optionsSpecify, searchedName, frame, rootClose):
    for i in optionsSpecify:
        if(searchedName.lower() == i[0].lower()):
            name = i[0]
            nameLabel = Label(frame, text=f"Nombre: {name}")
            nameLabel.pack()
            stateLabel = Label(frame)
            if(i[1]):
                stateLabel["text"] = "Estado: Activo"
            else:
                stateLabel["text"] = "Estado: Ocupado"
            dateLabel = Label(frame, text=f"Fecha del ultimo mantenimineto: {i[2]}")
            dateLabel.pack()
            priceLabel = Label(frame, text=f"Precio: ${i[3]}")
            priceLabel.pack()
            btnEdit = Button(frame, text="Editar elemento", command=lambda: menuEdit(rootClose, optionsSpecify, name))
            btnEdit.pack()
            btnDelete = Button(frame, text="Elimar elemento", command=lambda: deleteElement(optionsSpecify, name, rootClose))
            btnDelete.pack()
            btnChangeState = Button(frame, text="Cambiar el estado", command=lambda: changeState(optionsSpecify, name, rootClose, options["hangarsBusy"]))
            btnChangeState.pack()

def menuEdit(rootClose, optionsSpecify, itemToEdit):
    close(rootClose)
    for i in optionsSpecify:
        if(i[0] == itemToEdit):
            rootEdit = Tk()
            tittle = Label(rootEdit, text="JETT")
            name = i[0]
            labelEntryLastName = Label(rootEdit, text=f"Nombre anterior {i[0]}")
            labelEntryLastName.pack()
            labelEntryName = Label(rootEdit, text=f"Digite el numero nombre:")
            entryName = Entry(rootEdit)
            btnAccept = Button(rootEdit, text="Aceptar", command= lambda: edit(optionsSpecify, name, entryName.get(), rootEdit))
            btnClose = Button(rootEdit, text="Salir", command= lambda: close(rootEdit))
            btnClose.pack
            tittle.pack()
            labelEntryName.pack()
            entryName.pack()
            btnAccept.pack()
def changeState(optionsSpecify, name, rootClose, optionsChange):
    for i in range(len(optionsSpecify)):
        if(optionsSpecify[i][0] == name):
            copyOptionsSpecify = optionsSpecify[i]
            optionsSpecify.remove(copyOptionsSpecify)
            copyOptionsSpecify[1] = False
            optionsChange.append(copyOptionsSpecify)
            break
    close(rootClose)
    menuAdmin()

def edit(optionsSpecify,name, itemToChange, rootClose):
    print(optionsSpecify)
    for i in range(len(optionsSpecify)):
        if(optionsSpecify[i][0] == name):
            optionsSpecify[i][0] = itemToChange
    close(rootClose)
    menuAdmin()

def deleteElement(optionsSpecify, itemToDelete, rootClose):
    for i in optionsSpecify:
        if(i[0] == itemToDelete):
            optionsSpecify.remove(i)
    close(rootClose)
    menuAdmin()
def showItems(optionsSpecify, root):
    if(len(optionsSpecify) != 0):
        for i in range(len(optionsSpecify)):
            frame = Frame(root)
            labaelName = Label(frame, text=optionsSpecify[i][0])
            labaelName.pack()
            frame.pack()
    else: 
        labelMessage = Label(root, text="No hay elementos")
        labelMessage.pack()


def menuSeeMore(optionsSpecify):
    rootSeeMore = Tk()
    tittle = Label(rootSeeMore, text="JETT")
    tittle.pack()
    frame = Frame(rootSeeMore)
    frame.pack()
    if(len(optionsSpecify) != 0):
        for i in range(len(optionsSpecify)):
            frameElemento = Frame(frame, bg="#D1DDFF", padx=10, pady=10)
            labelNamePlane = Label(frameElemento, text=optionsSpecify[i][0])
            labelStatePlane = Label(frameElemento)
            if(optionsSpecify[i][1] == True):
                labelStatePlane["text"] = "Activo"
            else: labelStatePlane["text"] = "Ocupado"
            labelDatePlane = Label(frameElemento, text=optionsSpecify[i][2])
            labelPricePlane = Label(frameElemento, text="$"+str(optionsSpecify[i][3]))
            frameElemento.pack()
            labelNamePlane.pack()
            labelStatePlane.pack()
            labelDatePlane.pack()
            labelPricePlane.pack()
        else:
            labelMessage = Label(frame, text="No hay elementos")
            labelMessage.pack()
    rootSeeMore.mainloop()

def close(root):
    root.destroy()


def menuUser():
    root = Tk()
    tittle = Label(root, text="JETT")
main()
