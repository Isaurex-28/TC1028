# TC1028
# Mi idea de Proyecto
Isauro Alejandro Garza Elizondo

## **Contexto**:
Las agendas digitales no son un concepto nuevo, especialmente hoy en día que se podría decir que tenemos todo a un botón de distancia en nuestros dispositivos móviles, pero como es de esperarse las agendas,
calendarios y trackers que se pueden encontrar navegando en cualquier tienda de aplicaciones vienen con cargos extras, ya sea una suscripción mensual que desbloquea toda la app o solo un pago para desbloquear
ciertas funciones.
Pensando en que podría utilizar los recursos aprendidos en clase, me dí a la tarea de crear la estructura de lo que en un futuro podría ser mi propia aplicación de agenda semanal, removiendo las funciones que no  me gustan de otras aplicaciones (como los micropagos y suscripciones) y agregando cosas que no he logrado encontrar en otras aplicaciónes como que se reconozca al momento de cumplir la frecuencia de un hábito.

## **Algoritmo en Pseudocódigo**

**Inicio**

Generar una interfaz inicial que funcione como menú para mostrar otras 2 interfaces principales
"Interfaz de Tareas" e "Interfaz de Habitos"

Interfaz de Tareas = interfaz con 3 elementos principales:
                
                * Crear una tarea
                * Ver las tareas creadas (si es que las hay)
                * Salir de la interfaz (regresar al menú principal)

Interfaz de Hábitos = interfaz con 4 elementos principales:
                
                * Crear un hábito
                * Ver los hábitos creados
                * Agregar días cumplidos a un habito
                * Salir de la interfaz (regresar al menú principal)


Si usuario selecciona "Interfaz de Tareas"
  
  Mostrar interfaz de Tareas
  
  Si el usuario selecciona Crear una tarea
    
    Correr una función para crear tareas
  
  Si el usuario selecciona Mostrar Tareas
    
    Si hay tareas por mostrar
      
      Mostrar las tareas
      
Si usuario selecciona "Interfaz de Hábitos"
  Mostrar Interfaz de Hábitos
  Si el usuario selecciona Crear un hábito
    Correr una función para crear hábitos
  Si el usuario selecciona Mostrar Hábitos
    Si hay hábitos por mostrar
      Mostrar los hábitos
  Si el usuario selecciona Modificar un hábito
    Si hay hábitos por modificar
      Correr una función para modificar hábitos

Si el usuario selecciona "Salir" 
  Terminar el programa
  

## Librería datetime (Referencias al API)
Mi programa utiliza la librería datetime de python, que permite insertar fechas con segundo, minuto, hora, día, mes y año exactos, dependiendo incluso de las zonas de uso horarias de la region en la que te encuentres.
De igual manera la librería permite obtener la fecha registrada como "hoy" en el equipo en el que se está corriendo. En el programa se utiliza esto para determinar si una tarea está atrasada según su fecha de entrega que es pedida al usuario utilizando la librería, que da formato de DD-MM-YYYY a lo que se ingrese.

datetime — Basic date and time types. (2019). Python Documentation. https://docs.python.org/3/library/datetime.html#examples-of-usage-date

## Instrucciones 

Descargar el archivo y correr en la terminal con

```
python agenda.py
```

Responder a los menús para realizar las acciones deseadas.
Podrás regresar y ver tus tareas y hábitos guardados.
Una vez que se cierra el programa, se perderán los datos.

## **Gracias por visitar :D**

