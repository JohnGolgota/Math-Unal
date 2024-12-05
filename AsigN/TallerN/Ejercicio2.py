uno_dos = 5
tres_cincos = 4
seis_dies = 3
mas_10 = 2

input_a = float(input())
i = 1
suma = 0
while input_a != 0:
    input_a = input_a - 1
    if i <= 2:
        suma = suma + uno_dos
    elif i <= 5:
        suma = suma + tres_cincos
    elif i <= 10:
        suma = suma + seis_dies
    else:
        suma = suma + mas_10
    i = i + 1

print(suma)