#Integrantes: Constanza Cardenas, Matias Loyola, Paola Vallejos 

#Creacion de funciones
import funciones as funcion
Estudiantes = [[]]
TituloLista = ["NOMBRE", "EDAD", "CURSO", "PROMEDIO"];

def menu():
    while True:
        print("\n _________________________________________");
        print("|              Menu de opciones             |");
        print("| 1.- Agregar un estudiante.                |");
        print("| 2.- Ver todos los estudiantes.            |");
        print("| 3.- Modificar un estudiante.              |");
        print("| 4.- Eliminar un estudiante.               |");
        print("| 5.- Guardar coleccion en un archivo.      |");
        print("| 6.- Salir del programa.                   |");
        print("|___________________________________________|\n");
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
                print(" _____________________________");
                print("|                            |");
                print("|  Saliendo del Programa...  |");
                print("|____________________________|");
                break;
            else:
                print("Ingrese una de las opciones dadas, vuelva a intentarlo.");

#Se agregan los estudiantes a la coleccion 
def agregar_estudiante():
    print(" __________________________________________________");
    print("|                                                  |");
    print("| Ha decidido agregar a un estudiante a la escuela |");
    print("|__________________________________________________|");
    try:
        nombre = input("Ingrese el nombre y apellido del estudiante (ej: Paola Vallejos) --> ");
        edad = int(input("Ingrese la edad del estudiante (ej: 25) --> "));
        curso = input("Ingrese el curso del estudiante (ej: 4to basico) --> ");
        promedio = input("Ingrese el promedio del estudiante (ej: 6,7) --> ");
    except:
        print ("Error inesperado, ingrese los datos nuevamente")
    else:
        Estudiantes.append ([nombre, edad, curso, promedio])
        print(" ____________________________________________");
        print("|                                            |");
        print("|  Ha agregado exitosamente a un estudiante  |");
        print("|____________________________________________|");
        

#Se muestran todos los estudiantes
def ver_estudiantes():
    contador = 0
    print(" ________________________________________________");
    print("|                                                |");
    print("| Ha decidido ver a los estudiante de la escuela |");
    print("|________________________________________________|");
    for x in TituloLista:
        print (x, end= '          |  ');
    
    for y in Estudiantes:
        print(f"{contador}           |", end=" ");
        for z in y:
            print(z, end = '           | ');
        print("");
        contador += 1;

        
#Se modofican el o los estudiantes
def modificar_estudiante():
    print(" _____________________________________________________");
    print("|                                                     |");
    print("| Ha decidido modificar a un estudiante de la escuela |");
    print("|_____________________________________________________|");
    try:
        opc = int(input("¿Que Nº de linea de la lista de estudiantes desea modificar?: "));
    except:
        print("Error inesperado, vuelva a intentarlo.");
    else:
        if (opc < 0 or opc >= len(Estudiantes)):
            print("N° de fila inexistente, vuelva a intentarlo.");
        else:
            try:
                modificacion = input(f"Ingrese los nuevos datos del estudiante separados por espacios: ");
            except:
                print ("Error inesperado, vuelva a intentarlo");
            else:
                modificacion = modificacion.split();
                Estudiantes[opc] = modificacion;
            print(" ____________________________________________");
            print("|                                            |");
            print("|  Ha modificado exitosamente al estudiante  |");
            print("|____________________________________________|");
        
#Eliminar el o los estudiantes de la lista 
def eliminar_estudiante():
    print(" ____________________________________________________");
    print("|                                                    |");
    print("| Ha decidido eliminar a un estudiante de la escuela |");
    print("|____________________________________________________|");
    try:
        opc = int(input("¿Que Nº de linea de la lista de estudiantes desea eliminar?: "));
    except:
        print("Error inesperado, vuelva a intentarlo.");
    else:
        if (opc < 0 or opc > len(Estudiantes)):
            print("Ingrese un numero que este en el rango de numero de estudiantes, vuelva a intentarlo.");
        else:
            Estudiantes.pop(opc)
            print(" ___________________________________________");
            print("|                                           |");
            print("|  Ha eliminado exitosamente al estudiante  |");
            print("|___________________________________________|");
        
        
 #Se importa la lista a un nuevo archivo 
def guardar_archivo():
    print(" ___________________________________________________________");
    print("|                                                           |");
    print("| Ha decidido guardar la lista de estudiantes en un archivo |");
    print("|___________________________________________________________|");
    print("|                                                           |");
    print("| 1.- Archivo tipo Excel.                                   |");
    print("| 2.- Archivo tipo Texto.                                   |");
    print("|___________________________________________________________|");
    try:
        opc = int(input("¿En que tipo de archivo desea imprimir la lista de estudiantes?: "));
    except:
        print ("Error inesperado, vuelva a intentarlo");
    else:
        if (opc == 1):
            with open('Escuela.csv', 'w', encoding= 'utf-8' ) as estudiantes_csv:
                estudiantes_csv.write (f"{Estudiantes}")
                print(" _____________________________________");
                print("|                                     |");
                print("|  Ha guardado exitosamente la lista  |");
                print("|_____________________________________|");
        elif (opc == 2):
            with open('Escuela.txt', 'w', encoding= 'utf-8', newline= '') as estudiantes_txt:
                estudiantes_txt.write (f"{TituloLista}\n")
                estudiantes_txt.write (f"{Estudiantes}")
                print(" _____________________________________");
                print("|                                     |");
                print("|  Ha guardado exitosamente la lista  |");
                print("|_____________________________________|");
        else:
            print ("Error, vuelva a intentarlo")