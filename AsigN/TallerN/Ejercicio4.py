def vol_cilindro(r,h):
    return (3.141592654*r*r*h)

def feet_to_meters(p):
    return p * 0.3048

r = float(input())
h = float(input())


tiempo_de_vaciado = float(input())
velocidad_de_vaciado = float(input())

Volumen_vaciado = tiempo_de_vaciado * velocidad_de_vaciado

r_m = feet_to_meters(r)
h_m = feet_to_meters(h)

total_vol = vol_cilindro(r_m,h_m)
vol = total_vol - Volumen_vaciado
print(vol)
