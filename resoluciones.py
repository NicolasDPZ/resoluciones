
def negar(letra):
    return letra[1:] if letra.startswith("~") else "~" + letra

def resolver(c1, c2):
    resolvible = []
    for l in c1:
        if negar(l) in c2:
            nueva_clausula = (c1 - {l}) | (c2 - {negar(l)})
            resolvible.append(nueva_clausula)
    return resolvible
    

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