valor_producto = float(input())
descuento = valor_producto * 0.3

total = valor_producto - descuento
total_iva = total + total * 0.19
print(total)
print(descuento)
print(total_iva) 

