# TC1028
# Mi idea de Proyecto
Isauro Alejandro Garza Elizondo

## **Contexto**:
Las agendas digitales no son un concepto nuevo, especialmente hoy en día que se podría decir que tenemos todo a un botón de distancia en nuestros dispositivos móviles, pero como es de esperarse las agendas,
calendarios y trackers que se pueden encontrar navegando en cualquier tienda de aplicaciones vienen con cargos extras, ya sea una suscripción mensual que desbloquea toda la app o solo un pago para desbloquear
ciertas funciones.
Pensando en que podría utilizar los recursos aprendidos en clase, me dí a la tarea de crear la estructura de lo que en un futuro podría ser mi propia aplicación de agenda semanal, removiendo las funciones que no  me gustan de otras aplicaciones (como los micropagos y suscripciones) y agregando cosas que no he logrado encontrar en otras aplicaciónes como que se reconozca al momento de cumplir la frecuencia de un hábito.

## **Algoritmo en Pseudocódigo**
Inicio
Generar 2 páginas iniciales que tengan contenidos parecidos más no se relacionen entre sí
pag_one = "Página de Tareas"
pag_two = "Página de Habitos"

interfaz_o = interfaz con 3 elementos principales:
                * Calendario
                * Lista de Tareas
                * Menú de Proyectos

interfaz_t = interfaz con 3 elementos principales:
                * Calendario
                * Lista de Hábitos
                * Menú de Proyectos

calendar = Función que obtenga la información de fecha y hora del dispositivo y agregue las tareas correspondientes a tal fecha y hora
hw_list = Menú desplegable que permita crear tareas (con título, materia, tipo, prioridad, fecha de entrega, y descripción) y visualizarlos posteriormente
hb_list = Menú desplegable que permita crear hábitos (con nombre, y frecuencia meta) y administrar si para el dia de hoy se realizó el hábito o su contaparte
project = Menú deplegabble que permita crear proyectos con sus propias tareas (con propiedades igual es al de la lista de tareas) y agregar un progreso modificable establecido por el usuario

Si usuario selecciona "Página Personal"
  Mostrar interfaz_o
Si usuario selecciona "Página Académica"
  Mostrar interfaz_t

## Librería datetime (Referencias al API)
Mi programa utiliza la librería datetime de python, que permite insertar fechas con segundo, minuto, hora, día, mes y año exactos, dependiendo incluso de las zonas de uso horarias de la region en la que te encuentres.
De igual manera la librería permite obtener la fecha registrada como "hoy" en el equipo en el que se está corriendo. En el programa se utiliza esto para determinar si una tarea está atrasada según su fecha de entrega que es pedida al usuario utilizando la librería, que da formato de DD-MM-YYYY a lo que se ingrese.

datetime — Basic date and time types. (2019). Python Documentation. https://docs.python.org/3/library/datetime.html#examples-of-usage-date

‌


