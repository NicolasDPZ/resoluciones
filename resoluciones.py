def negate(literal):
    return literal[1:] if literal.startswith("~") else "~" + literal


def resolve(c1, c2):
    resolvents = []
    for l in c1:
        if negate(l) in c2:
            new_clause = (c1 - {l}) | (c2 - {negate(l)})
            resolvents.append(new_clause)
    return resolvents


def resolution(clauses):
    clauses = [set(c) for c in clauses]

    while True:
        new = []
        for i in range(len(clauses)):
            for j in range(i + 1, len(clauses)):
                resolvents = resolve(clauses[i], clauses[j])
                for r in resolvents:
                    if not r:
                        return True  # cláusula vacía → éxito
                    if r not in clauses and r not in new:
                        new.append(r)

        if not new:
            return False

        clauses.extend(new)

clauses = [
    {"Mata_Jack_Tuna", "Mata_Curiosidad_Tuna"},
    {"¬Mata_Jack_Tuna"},
    {"¬Mata_Curiosidad_Tuna"}
]

print("si o no?", resolution(clauses))