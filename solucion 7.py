import sqlite3
import os

#buscar= jinja2.Environment(loader= jinja2.FileSystemLoader("C:/Users/ARCUS COMP/Desktop/fundamentos de programacion/tarea 7/Metioritos/"))
#enlazar= buscar.get_template("metiorito.html")

def limpiar():
    os.system("cls")

def metiorito():
    miconexion= sqlite3.connect("base_metiorito")

    nombre= input("Digite el nombre del metiorito: ")
    fecha= input("Digite la fecha en el cual cayo el metiorito: ")
    tipo= input("Digite el tipo de metiorito: ")
    pais= input("Digite el pais donde cayo el metiorito: ")
    lat= input("Digite la latitud del metiorito: " )
    lon= input("Digite la longitud del metiorito: ")
    comen= input("Digite un comentario para el metiorito: ")

    micursor = miconexion.cursor()

    #micursor.execute("CREATE TABLE metiorito (llave integer PRIMARY KEY AUTOINCREMENT,Nombre varchar(100),Fecha date,Tipo varchar(50),Pais varchar(50),Latitud real, Longitud real, Comentario text) ")

    micursor.execute("INSERT INTO metiorito (nombre,fecha,tipo,pais,latitud,longitud,comentario) values ('"+nombre+"','"+fecha+"','"+tipo+"','"+pais+"','"+lat+"','"+lon+"','"+comen+"')")

    miconexion.commit()
    miconexion.close()

def mostrar():
    miconexion=sqlite3.connect("base_metiorito")
    micursor= miconexion.cursor()
    micursor.execute("SELECT  * FROM metiorito")

    print("\t llave \t\t Nombre \t\t Fecha \t\t Tipo \t\t Pais \t\t Latitud \t\t Longitud \t\t\t Comentario ")
    print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

    for Metiorito in micursor:
        cl='\t\t'+str(Metiorito[0])+ '\t\t'+Metiorito[1]+ '\t\t'+str(Metiorito[2])+ '\t\t' +Metiorito[3]+ '\t\t' +Metiorito[4]+ '\t\t' +str(Metiorito[5])+ '\t\t' + str(Metiorito[6])+ '\t\t' +Metiorito[7]

        print(cl)

    miconexion.close()

def editar():
    metioritos=[]
    miconexion = sqlite3.connect("base_metiorito")
    micursor = miconexion.cursor()
    micursor.execute("SELECT * FROM metiorito")
    print("\t llave \t\t Nombre \t\t Fecha \t\t Tipo \t\t Pais \t\t Latitud \t\t Longitud \t\t\t Comentario \t ")
    print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

    for Metiorito in micursor:
        metioritos.append(Metiorito)
        cl = '\t\t' + str(Metiorito[0]) + '\t\t' +Metiorito[1] + '\t\t' + str(Metiorito[2]) + '\t\t' + Metiorito[3] + '\t\t' + Metiorito[4] + '\t\t' + str(Metiorito[5]) + '\t\t' + str(Metiorito[6]) + '\t\t\t' + (Metiorito[7])
        print(cl)

    llave= input("Elija el numero del metiorito que desea editar: ")

    for Metiorito in metioritos:
        print(Metiorito[0])
        if int(Metiorito[0]) == int(llave):
            llave = Metiorito[0]
            nombre = Metiorito[1]
            fecha = Metiorito[2]
            tipo = Metiorito[3]
            pais = Metiorito[4]
            lat= Metiorito[5]
            lon = Metiorito[6]
            comen = Metiorito[7]

    nombre = input("Digite el nuevo nombre de " + nombre + ": ")
    fecha = input("Digite la nueva fecha del metiorito " + str(fecha) + " : ")
    tipo = input("Digite el nuevo tipo de metiorito " + tipo + " : ")
    pais = input("Digite el nuevo pais donde cayo el metiorito " + pais + " : ")
    lat = input("Digite la nueva latitud del metiorito " + str(lat) + " : ")
    lon = input("Digite la nueva longitud del metiorito " + str(lon) + " : ")
    comen = input("Digite el nuevo comentario del metiorito " + comen + " : ")

    sql = "UPDATE metiorito set   nombre= '" + nombre + "', fecha='" + str(fecha) + "', tipo='" + tipo + "', pais='" + pais + "', Latitud='" + str(lat) + "', Longitud='" + str(lon) + "', comentario='"+comen+"' where llave = " + str(llave)
    micursor.execute(sql)
    miconexion.commit()
    miconexion.close()
    print("Metiorito Actualizado")
    input("Presione ENTER para volver al menu: ")
    menu()


def conseguir_archivo(archivo):
    if os.path.exists(archivo):
        fp= open(archivo, "r")
        contenido= fp.read()
        fp.close()
        return contenido


def exportar():
    miconexion = sqlite3.connect("base_metiorito")
    micursor = miconexion.cursor()
    SQL = ("SELECT * FROM metiorito")
    micursor.execute(SQL)
    base = conseguir_archivo("metiorito.html")
    entrar=[]

    for meteoro in micursor:
        temporal= """L.marker(["""+str(meteoro[5])+""", """+str(meteoro[6])+"""])
                        .addTo(map)
                        .bindPopup('Metiorito:""" +meteoro[1]+ """ , Fecha:"""+str(meteoro[2])+""" , Tipo:"""+(meteoro[3])+""" , Pais:"""+(meteoro[4])+""" , Comentario:"""+(meteoro[7])+"""');"""
        entrar.append(temporal)

    sep=" "
    camb= sep.join(entrar)
    base= base.replace("{MARCADORES}" , camb)

    f = open("caida_metiorito.html", "w")
    f.write(base)
    f.close()
    miconexion.commit()
    miconexion.close()



def menu():
    limpiar()
    print("Bienvenido Al Registro de caidas de metioritos a nivel mundial")
    print("------------------------------------------------------------------")
    print("1.- Agregar metiorito caido")
    print("2.- Mostrar metiorito caido")
    print("3.- Editar metiorito caido")
    print("4.- Exportar metiorito caido")
    print("5.- Salir")
    opcion = input("Digite una opcion valida: ")


    if opcion == "1":
        limpiar()
        print("Vamos a agregar un metiorito")
        metiorito()
        input("Presione ENTER para volver al menu: ")
        menu()

    elif opcion == "2":
        limpiar()
        print("Vamos a mostrar los metioritos caidos")
        mostrar()
        input("Presione ENTER para volver al menu: ")
        menu()

    elif opcion == "3":
        limpiar()
        print("Vamos a editar un metiorito caido :) ")
        editar()

    elif opcion == "4":
        limpiar()
        print("Datos exportados exitosamente!! ")
        exportar()
        input("Presione ENTER para volver al menu: ")
        menu()

    elif opcion== "5":
        print("Gracias por tu tiempo")

    else:
        print("Digite una opcion valida!!")
        input("Preseione ENTER para volver al menu: ")
        menu()



menu()



