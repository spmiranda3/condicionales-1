MATERIAS = 5
nombre = input("Nombre completo: ")
grado = input("Grado: ")
grupo = input("Grupo: ")
contador = 1
sumatoria = 0
while contador <= MATERIAS:
    nombre_materia = input("Nombre de la materia {}: ".format(contador))
    calificacion = float(input("Calificación en {}: ".format(nombre_materia)))
    sumatoria = sumatoria + calificacion
    contador = contador + 1

promedio = sumatoria / MATERIAS
print("""***** Resultados *****
Alumno: {} | {} {}
*******************************
* Promedio: {}
*******************************
""".format(nombre, grupo, grado, promedio))
