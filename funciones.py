def menu():
    while True:
        print("\n ______________________________________");
        print("|             Menu de opciones             |");
        print("| 1.- Agregar un estudiante.                |");
        print("| 2.- Ver todos los estudiantes.            |");
        print("| 3.- Modificar un estudiante.              |");
        print("| 4.- Eliminar un estudiante.               |");
        print("| 5.- Guardar coleccion en un archivo. |");
        print("| 6.- Salir del programa.              |");
        print("|______________________________________|\n");
        try:
            opc = int(input("Ingrese una opcion: "));
        except:
            print("Error inesperado, vuelva a intentarlo.");
        else:
            if (opc == 1):
                funcion.agregar_estudiante();
            elif (opc == 2):
                funcion.ver_estudiantes();
            elif (opc == 3):
                funcion.modificar_estudiante();
            elif (opc == 4):
                funcion.eliminar_estudiante();
            elif (opc == 5):
                funcion.guardar_archivo();
            elif (opc == 6):
                break;
            else:
                print("Ingrese una de las opciones dadas, vuelva a intentarlo.");
def agregar_estudiante():
    print("lol")

def ver_estudiantes():
    print("lol")

def modificar_estudiante():
    print("lol")

def eliminar_estudiante():
    print("lol")

def guardar_archivo():
    print("lol")