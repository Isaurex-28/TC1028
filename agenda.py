#AVANCE 3

#Importo biblioteca de tiempo
import datetime

#Utilizable por tarea/proyecto

def date_calc(due):
  date = datetime.date.now().date()
  if due < date:
    return("Atraso")
  elif due_date == date:
    return("Hoy")
  else:
    return(due - date ,"días")

print("Seleccióna fecha de entrega")
due_date = datetime.date(int(input("Año: "),int(input("Mes: "),int(input("Día: "))

print(date_calc(due_date))



# Utilizable con los habitos

def hab_count(habit,days):
  if habit == "Sí":
    return days + 1
  elif habit == "No":
    days = 0  
    return days
  else:
    return "Asegúrate de escribir Sí o No tal cual está escrito en la pregunta"

habit = input("¿Cumpliste con tu hábito? (Sí o No)")
count = 0
count = hab_count(habit,count)

print(count)



#Utilizable con las tareas (color segun su prioridad)

def red(priority):
  if priority >= 3:
    return 255
  else:
    return 102

def green(priority):
  if priority <= 3:
    return 255
  else:
    return 102

priority = int(input("Prioridad del 1 al 5 "))

r = red(priority)
g = green(priority)
b = 102

print(r,g,b)
