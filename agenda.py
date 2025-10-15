#AVANCE 7

#importar librerias
import datetime

#Se crean listas para ir almacenando las tareas y habitos
tasks = []
habits = []


#Funciones para crear una tarea
def task_name(dictionary):
    name = input("\nNombre de tu tarea: ")
    dictionary["name"] = name
    return dictionary

def task_date(dictionary):
    print("\nSelecciona fecha de entrega")
    day = int(input("Día (DD): "))
    month = int(input("Mes (MM): "))
    year = int(input("Año (YYYY): "))
    due_date = datetime.date(year,month,day)
    dictionary["due_date"] = due_date
    return dictionary

def task_priority(dictionary):
    print("\nSelección de prioridad")
    priorities = ["1","2","3","4","5"]
    priority = input("Prioridad del 1 al 5: ")
    while priority not in priorities:
        print("La prioridad tiene que ser un número del 1 al 5")
        priority = input("Prioridad del 1 al 5: ")
    dictionary["priority"] = priority
    return dictionary

def task_status(task):
    today = datetime.date.today()
    if task["due_date"]<today:
        status = "Atrasado"
    else:
        status = "En Tiempo"
    return status

def task_create(dictionary):
    task_name(dictionary)
    task_date(dictionary)
    task_priority(dictionary)
    return dictionary


#Funciones para crear un habito
def habit_name(dictionary):
    name = input("\nNombre de tu habito: ")
    dictionary["name"] = name
    return dictionary

def habit_priority(dictionary):
    print("\nSelección de prioridad")
    priorities = ["1","2","3","4","5"]
    priority = input("Prioridad del 1 al 5: ")
    while priority not in priorities:
        print("La prioridad tiene que ser un número del 1 al 5")
        priority = input("Prioridad del 1 al 5: ")
    dictionary["priority"] = priority
    return dictionary

def habit_create(dictionary):
    habit_name(dictionary)
    habit_priority(dictionary)
    return dictionary

#Declarar variables
run = True


while run:
    
    #Selección de Menu
    print("\nSelecciona el Menú")
    option = input("1.- Tareas \n2.- Hábitos \n3.- Salir \nEscribe 1 2 o 3: ")
    
    #Acciones según el menu
    if option == "1":
        task_run=True
        while task_run:
            print("\nAcción a realizar")
            task_option = input("1.- Crear Tarea \n2.- Mostrar Tareas \n3.- Salir \nEscribe 1 2 o 3: ")
            if task_option == "1":
                create_task="1"
                #Ciclo while que permite crear varias tareas seguidas
                while create_task == "1":
                    new_task = {}
                    new_task = task_create(new_task)
                    #Se agrega el diccionario completo a la lista tasks
                    tasks.append(new_task)
                    print("\nTarea creada: ","\nNombre: ",new_task["name"],"\nPrioridad: ",new_task["priority"],"\nFecha de Entrega: ",new_task["due_date"])
                    create_task=input("\n¿Deseas crear otra tarea? \n1.- Sí \n2.- No \n(Escribe el número): ")

            elif task_option == "2":
                    #Se evalua si hay tareas por mostrar
                    if len(tasks) > 0:
                        print("Tareas:")
                        for task in tasks:
                            #Se imprime cada diccionario y estatus de cada tarea, por separado
                            print("\nNombre:",task["name"], 
                                "\nPrioridad:",task["priority"], 
                                "\nFecha de entrega:",task["due_date"],
                                "\nEstatus: ",task_status(task))
                    else:
                        print("No hay tareas por mostrar")
            elif task_option == "3":
                break

            else:
                print("Entrada no válida")


    elif option == "2":
        habit_run = True
        while habit_run:
            print("\nAcción a realizar")
            habit_option = input("1.- Crear Hábito \n2.- Mostrar Hábitos \n3.- Salir \nEscribe 1 2 o 3: ")

            if habit_option == "1":
                create_habit = "1"
                while create_habit == "1":
                    new_habit = {}
                    new_habit = habit_create(new_habit)
                    habits.append(new_habit)
                    print("\nHábito creado: ","\nNombre: ",new_habit["name"],"\nPrioridad: ",new_habit["priority"])
                    create_habit=input("\n¿Deseas crear otro hábito? \n1.- Sí \n2.- No \n(Escribe el número): ")

            elif habit_option == "2":
                    if len(habits)>0:
                        print("Habitos: ")
                        for habit in habits:
                            print("Nombre:",habit["name"]," Prioridad:",habit["priority"],)
                    else:
                        print("No hay hábitos por mostrar")

            elif habit_option == "3":
                break

            else:
                print("Entrada no válida")


    elif option == "3":
        print("Agenda cerrada")
        break
    else:
        print("Entrada no válida, escribe 1 2 o 3")
