
nombre = input("¿Cuál es tu nombre?: ")

mensaje = """🧭 MENÚ DE AYUDA

Bienvenido al sistema de gestión de materias y actividades.
Aquí puedes administrar tus materias, registrar tus evaluaciones, ingresar notas y consultar tus promedios.
A continuación, te explicamos qué hace cada opción del menú principal:

1️⃣ Materias (Agregar)

Con esta opción puedes agregar una nueva materia.
Solo tendrás que escribir el nombre de la materia que deseas registrar.
Por ejemplo: “Matemáticas”, “Historia”, “Programación”, etc.

2️⃣ Actividad o Evaluación (Agregar)

Aquí puedes añadir una nueva actividad o evaluación a una de tus materias ya registradas.
Primero, el sistema te mostrará la lista de materias disponibles para que elijas a cuál quieres agregar la actividad.
Luego te preguntará si la actividad es individual o grupal, y deberás indicar la ponderación (el porcentaje o peso que tiene esta actividad en la nota final).

3️⃣ Consulta de Materias y Actividades

En esta sección puedes ver todas tus materias junto con las actividades que tienes registradas.
Además, se mostrarán las notas que ya hayas ingresado y su ponderación correspondiente, para que lleves un control claro de tu progreso en cada materia.

4️⃣ Notas (Agregar)

Esta opción te permite agregar notas a tus actividades.
Primero deberás elegir la materia (se te mostrarán todas las que tienes).
Luego elegirás la actividad dentro de esa materia, y finalmente ingresarás la nota obtenida.

5️⃣ Consulta de Promedio

Si quieres saber cómo vas en una materia, esta es la opción indicada.
Selecciona la materia y el sistema te mostrará tu promedio actual considerando todas las actividades registradas y sus ponderaciones.

⚖️ Reglas especiales para el promedio:

Si las actividades grupales tienen una ponderación total menor o igual al 50%, solo se sumarán si tu promedio en las notas individuales es 6.0 o más.

Si las actividades grupales representan más del 50% del total, se sumarán siempre, sin importar la nota individual.

6️⃣ Editar (Materias o Actividades)

¿Te equivocaste o quieres cambiar algo? Aquí puedes editar materias o actividades.

Si eliges Materia, el sistema te mostrará las materias actuales y podrás cambiarle el nombre a la que elijas.

Si eliges Actividad, primero seleccionarás la materia que la contiene, luego verás la lista de actividades y podrás modificar sus datos (tipo: individual o grupal, y ponderación).

7️⃣ Ayuda

Si seleccionas esta opción, se mostrará este menú de ayuda, donde podrás leer la descripción completa de cada función del sistema.
"""

verificado = "permiso"
materias = []
actividades = []

while verificado == "permiso":
    
    print(f"¡Bienvenido {nombre}!")
    lista = ("1 - Materias (agregar), 2 - Actividad o Evaluación (agregar), 3 - Consulta de materias y actividades, 4 - Notas (agregar), 5 - Consulta de promedio, 6 - Editar, 7 - Ayuda")
    print(lista)
    opción = int(input("¿Qué desea hacer? introduzca el número: "))
    
    if opción == 1:
        subject = input("¿Cuál es el nombre de la materia?: ")
        materias.append(subject)
    
    if opción == 2:
        print(materias)
        seleccionsubject = input("'¿A cuál materia pertenece la actividad?: ").lower()
        if seleccionsubject is materias:
            nombreactividad = input("Cuál es la actividad?")
            tipodeactividad = input("La actividad es grupal o individual: escriba solo individual o grupal: ").lower()
            if tipodeactividad == "grupal":
                print("grupal")
            elif tipodeactividad == "individual":
                print("individual)")
        
    elif opción == 3:
        print(materias, actividades)
    
    elif opción == 4:
        subject1 =  input("¿Cuál es el nombre de la materia: ")
        
    elif opción == 5:
        print("5")
        
    elif opción == 6:
        print("6")
        
    elif opción == 7:
        print(mensaje)