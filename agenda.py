"""
Proyecto Agenda
Este programa consiste de una agenda digital, donde el usuario navega 
a través de menús, creando tareas y habitos y modificandolos, así
como un sistema de detección para las tareas atrasadas y hábitos 
cumplidos en la semana.
"""


# bibliotecas
import datetime

"""
Variable run permitirá que el programa corra infinitamente

Lista PRIORITIES es una constante, que se usará para checar que las
prioridades ingresadas por el usuario, estén dentro del márgen.
"""
run = True
PRIORITIES = ["1", "2", "3", "4", "5"]

"""
(almacenamiento de datos)
Listas para almacenar las tareas y habiitos
"""
tasks = []
habits = []


"""
============ Funciones para tareas ===================
"""


def task_name(dictionary):
    """
    (uso de funciones)
    Recibe un diccionario, pide al usuario el nombre de la tarea
    a crear y la agrega al diccionario con la llave "name"
    devuelve:  el diccionario modificado
    """
    name = input("\nNombre de tu tarea: ")
    dictionary["name"] = name
    return dictionary


def task_date(dictionary):
    """
    (uso de funciones, uso de ciclos (while))
    Recibe un diccionario, pide al usuario la fecha de entrega
    de la tarea a crear.
    Utiliza un ciclo while para verificar que la fecha exista
    y la agrega al diccionario con la llave "due_date"
    devuelve:  el diccionario modificado
    """
    print("\nSelecciona fecha de entrega")
    while True:
        try:
            day = int(input("Día (DD): "))
            month = int(input("Mes (MM): "))
            year = int(input("Año (YYYY): "))
            due_date = datetime.date(year, month, day)
            dictionary["due_date"] = due_date
            return dictionary
        except ValueError:
            print("Fecha no válida, intenta de nuevo \n")


def task_priority(dictionary):
    """
    (uso de funciones, uso de ciclos (while))
    Recibe un diccionario, pide al usuario la prioridad
    de la tarea a crear.
    Utiliza un ciclo while para verificar que la prioridad esté
    dentro del margen, y la agrega al diccionario 
    con la llave "priority"
    devuelve:  el diccionario modificado
    """
    print("\nSelección de prioridad")
    priority = input("Prioridad del 1 al 5: ")
    while priority not in PRIORITIES:
        print("La prioridad tiene que ser un número del 1 al 5")
        priority = input("Prioridad del 1 al 5: ")
    dictionary["priority"] = priority
    return dictionary


def task_status(task):
    """
    (uso de funciones, uso de condicionales)
    Recibe una tarea (que es un diccionario específico), 
    corrobora utilizando la fecha de hoy si la tarea está atrasada
    y la agrega al diccionario con la llave "due_date"
    devuelve:  el status de la tarea (Atrasado o En Tiempo)
    """
    today = datetime.date.today()
    if task["due_date"] < today:
        status = "Atrasado"
    else:
        status = "En Tiempo"
    return status


def task_create(dictionary):
    """
    (uso de funciones)
    Recibe un diccionaro, y llama a las funciones para su modificación
    devuelve:  el diccionario modificado
    """
    task_name(dictionary)
    task_date(dictionary)
    task_priority(dictionary)
    print("\nTarea creada: ", "\nNombre: ", dictionary["name"],
          "\nPrioridad: ", dictionary["priority"],
          "\nFecha de Entrega: ", dictionary["due_date"])
    return dictionary


"""
============ Funciones para hábitos ===================
"""


def habit_name(dictionary):
    """
    (uso de funciones)
    Recibe un diccionario, pide al usuario el nombre
    del  hábito a crear, y lo agrega al diccionario con la llave "name"
    devuelve:  el diccionario modificado
    """
    name = input("\nNombre de tu habito: ")
    dictionary["name"] = name
    return dictionary


def habit_frequency(dictionary):
    """
    (uso de funciones, uso de ciclos (while), uso de condicionales)
    Recibe un diccionario, pide el usuario la frecuencia a cumplir
    del hábito.
    Utiliza un ciclo while para evitar un crash al momento de ingresar
    una cadena.
    Utiliza un condicional para verificar que la frecuencia esté
    dentro del márgen permitido.
    Agrega la frecuencia al diccionario con la llave "frequency"
    devuelve: el diccionario modificado
    """
    print("\nSelecciona frecuencia (veces por semana)")
    while True:
        try:
            frequency = int(input("Frecuencia del 1 al 7: "))
            if frequency > 7 or frequency < 1:
                print("La frecuencia tiene que ser un número del 1 al 7")
                frequency = input("Frecuencia del 1 al 7: ")
            else:
                dictionary["frequency"] = frequency
                return dictionary
        except ValueError:
            print("Entrada no válida, intenta de nuevo \n")


def habit_priority(dictionary):
    """
    (uso de funciones, uso de ciclos (while))
    Recibe un diccionario, pide al usuario la prioridad
    del hábito a crear.
    Utiliza un ciclo while para verificar que la prioridad esté
    dentro del margen, y la agrega al diccionario 
    con la llave "priority"
    devuelve:  el diccionario modificado
    """
    print("\nSelección de prioridad")
    priority = input("Prioridad del 1 al 5: ")
    while priority not in PRIORITIES:
        print("La prioridad tiene que ser un número del 1 al 5")
        priority = input("Prioridad del 1 al 5: ")
    dictionary["priority"] = priority
    return dictionary


def habit_mean(dictionary):
    """
    (uso de funciones, uso de matrices, uso de operadores aritméticos)
    Recibe un diccionario, y utiliza la frecuencia de cada habito
    para calcular cuantos habitos hay por día en promedio
    devuelve:  el promedio de habitos por día
    """
    sum = 0
    for habit in dictionary:
        """
        Se divide la frecuencia entre 7 para encontrar la probabilidad 
        de que el hábito deba cumplirse ese día
        """
        probability = habit["frequency"] / 7
        sum = sum + probability
    return round(sum, 2)


def habit_create(dictionary):
    """
    (uso de funciones)
    Recibe un diccionaro, y llama a las funciones para su modificación
    devuelve:  el diccionario modificado
    """
    habit_name(dictionary)
    habit_priority(dictionary)
    habit_frequency(dictionary)
    dictionary["status"] = 0
    print("\nHábito creado: ", "\nNombre: ", new_habit["name"],
          "\nPrioridad: ", new_habit["priority"],
          "\nFrecuencia meta:", new_habit["frequency"])
    return dictionary


"""
============= Funciones Auxiliares =========
"""


def habit_show(matrix):
    """
    (uso de funciones, uso de matrices)
    Llama a una lista de diccionarios, e imprime cada diccionario
    """
    if len(matrix) > 0:

        print("\nPromedio de hábitos por día: ",
              habit_mean(matrix))
        print("\nHabitos: ")

        for habit in matrix:
            print("\nNombre:", habit["name"],
                  "\nPrioridad:", habit["priority"],
                  "\nFrecuencia: ", habit["frequency"],
                  "\nEstatus (días completados): ", habit["status"])
    else:
        print("No hay hábitos por mostrar")


def task_show(matrix):
    """
    (uso de funciones, uso de matrices)
    Llama a una lista de diccionarios, e imprime cada diccionario
    """
    if len(matrix) > 0:
        print("Tareas:")

        for task in matrix:
            print("\nNombre:", task["name"],
                  "\nPrioridad:", task["priority"],
                  "\nFecha de entrega:", task["due_date"],
                  "\nEstatus: ", task_status(task))
    else:
        print("No hay tareas por mostrar")


"""
============ Programa Principal ===================
"""

while run:

    print("\nSelecciona el Menú")
    option = input("1.- Tareas \n2.- Hábitos \
                    \n3.- Salir \nEscribe 1 2 o 3: ")
    if option == "1":
        task_run = True
        while task_run:
            print("\nAcción a realizar")
            task_option = input(
                "1.- Crear Tarea \n2.- Mostrar Tareas \
                    \n3.- Salir \nEscribe 1 2 o 3: ")

            if task_option == "1":

                create_task = "1"
                while create_task == "1":

                    new_task = {}
                    new_task = task_create(new_task)
                    tasks.append(new_task)

                    create_task = input("\n¿Deseas crear otra tarea? \
                        \n1.- Sí \n2.- No \n(Escribe el número): ")

            elif task_option == "2":
                task_show(tasks)

            elif task_option == "3":
                task_run = False

            else:
                print("Entrada no válida")

    elif option == "2":

        habit_run = True
        while habit_run:
            print("\nAcción a realizar")
            habit_option = input(
                "1.- Crear Hábito \
                \n2.- Mostrar Hábitos \
                \n3.- Modificar estatus (Agregar día) \
                \n4.- Salir \nEscribe 1 2 3 o 4: ")

            if habit_option == "1":

                create_habit = "1"
                while create_habit == "1":

                    new_habit = {}
                    new_habit = habit_create(new_habit)
                    habits.append(new_habit)

                    create_habit = input("\n¿Deseas crear otro hábito? \
                                    \n1.- Sí \n2.- No \n(Escribe el número): ")

            elif habit_option == "2":
                habit_show(habits)

            elif habit_option == "3":
                modify = True
                while modify:
                    print("¿Qué hábito deseas modificar?\n")

                    habit_show(habits)

                    habit_modify = input("\nNombre del hábito a modificar: ")
                    """
                    Utilizo un for else con break para que,
                    una vez encuentre el nombre indicado,
                    no se corra la acción del else (Hábito no
                    encontrado)
                    """
                    
                    for habit in habits:
                        if habit["name"] == habit_modify:
                            habit["status"] += 1
                            print("Día agregado")
                            if habit["status"] >= habit["frequency"]:
                                habit["status"] = "Completado"
                                print("Nuevo estatus: ", habit["status"])
                            modify = False
                            break
                    else:
                        print("Hábito no encontrado")

            elif habit_option == "4":
                habit_run = False

            else:
                print("Entrada no válida")

    elif option == "3":
        print("Agenda cerrada")
        run = False

    else:
        print("Entrada no válida, escribe 1 2 o 3")
