original = [0] * 6
inverse = [0] * 6

for i in range(6):
    print("Entrez une valeur pour la position", i + 1, ": ")
    original[i] = int(input())

for i in range(6):
    b = 5 - i
    inverse[b] = original[i]

print("Tableau inversé : ")
print(inverse)
