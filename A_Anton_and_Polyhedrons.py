t = int(input())
result = 0

for i in range(t):
    shape = input()

    if shape == 'Tetrahedron':
        result += 4
    elif shape == 'Cube':
        result += 6
    elif shape == 'Octahedron':
        result += 8
    elif shape == 'Dodecahedron':
        result += 12
    elif shape == 'Icosahedron':
        result += 20

print(result)



# Tetrahedron. Tetrahedron has 4 triangular faces.
# Cube. Cube has 6 square faces.
# Octahedron. Octahedron has 8 triangular faces.
# Dodecahedron. Dodecahedron has 12 pentagonal faces.
# Icosahedron. Icosahedron has 20 triangular faces.