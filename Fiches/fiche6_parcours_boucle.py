for row in range(3):
    indice_y = row
    print('Ligne :', indice_y)
    for col in range(3):
        indice_x = col
        print('* Colonne :',indice_x)
        x = 200 + row * 20
        y = 100 + col * 20
        print('  ->   x = ', x, '; y = ', y)
