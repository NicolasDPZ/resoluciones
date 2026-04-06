#funcion para negar una letra, si la letra empieza con "~" se le quita, si no, se le agrega "~" al inicio

def negar(letra):
    return letra[1:] if letra.startswith("~") else "~" + letra

#funcion para resolver dos clausulas, se busca una letra en la primera clausula que tenga su negacion en 
# la segunda clausula, si se encuentra, se crea una nueva clausula que es la union de las dos clausulas 
# sin la letra y su negacion, y se agrega a la lista de resolvibles

def resolver(c1, c2):
    resolvible = []
    for l in c1:
        if negar(l) in c2:
            nueva_clausula = (c1 - {l}) | (c2 - {negar(l)})
            resolvible.append(nueva_clausula)
    return resolvible
    
#funcion para aplicar el algoritmo de resolucion a una lista de clausulas, se convierte cada clausula 
# a un conjunto para facilitar las operaciones de union y diferencia, luego se iteran todas las combinaciones 
# de clausulas y se aplican las resoluciones, si se encuentra una clausula vacia se retorna True, si no se 
# encuentran nuevas clausulas se retorna False, si se encuentran nuevas clausulas se agregan a la lista de 
# clausulas y se repite el proceso

def resolucion(clausulas):
    clausulas = [set(c) for c in clausulas]

    while True:
        nuevas = []
        for i in range(len(clausulas)):
            for j in range(i + 1, len(clausulas)):

                resolvible = resolver(clausulas[i], clausulas[j])

                for r in resolvible:
                    if not r:
                        return True
                    if r not in clausulas and r not in nuevas:
                        nuevas.append(r)

        if not nuevas:
            return False

        clausulas.extend(nuevas)


#usos para probar las clausulas 

clausulas = [
    {"~Llueve", "Trafico"},  
    {"Llueve"},
    {"~Trafico"}
]

clausulas2 = [
    {"A", "B"},
    {"~A"},
    {"~B"}
]

clausulas3 = [
    {"A", "B"},
    {"~A"}
]

clausulastaller = [
    {"Mata_Jack_Tuna", "Mata_Curiosidad_Tuna"},
    {"~Mata_Jack_Tuna"},
    {"~Mata_Curiosidad_Tuna"}
]

print("llueve?", resolucion(clausulas))
print("si o no?", resolucion(clausulas2))
print("si o no?", resolucion(clausulas3))
print("curiosidad mata al gato?", resolucion(clausulastaller))