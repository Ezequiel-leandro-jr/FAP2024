# CONJUNTOS
# Coleções de elementos únicos e não ordenados.
# Úteis para realizar operações como UNIÃO, INTERSEÇÃO e DIFERENÇA entre as coleções


# OPERAÇÕES COMUNS COM CONJUNTOS #
conjuntoA = { 1, 2, 3, 4, 5 }
conjuntoB = { 5, 6, 7, 8 }
print(f'Conjunto A = {conjuntoA}\nConjunto B = {conjuntoB}\n')

conjuntoA.add(6)
conjuntoB.remove(6)
print('Adicionamos o elemento "6" do Conjunto A e removemos o elemento "6" do conjunto B')

print(f'\nConjunto A = {conjuntoA}\nConjunto B = {conjuntoB}\n')

# UNIÃO ENTRE CONJUNTOS #
conjuntoC = conjuntoA | conjuntoB
print(f'ConjuntoA U ConjuntoB = {conjuntoC}')

# INTERSEÇÃO ENTRE CONJUNTOS #
conjuntoC = conjuntoA & conjuntoB
print(f'ConjuntoA ∩ ConjuntoB = {conjuntoC}')

# DIFERENÇA ENTRE CONJUNTOS #
conjuntoC = conjuntoA - conjuntoB
print(f'ConjuntoA ≠ ConjuntoB = {conjuntoC}')

# DIFERENÇA ENTRE CONJUNTOS #
conjuntoC = conjuntoB - conjuntoA
print(f'ConjuntoB ≠ ConjuntoA = {conjuntoC}')
