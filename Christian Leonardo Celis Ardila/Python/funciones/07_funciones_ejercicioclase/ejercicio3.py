
def descuento(VArticulo):
    desc = VArticulo * 0.05
    return desc

while True:
    try:
        CProducto = float(input("Digite el valor de un producto"))
        if(CProducto<0):
            print("ERROR NUmero negativo")
            continue
        break
    except Exception as e:
        print("Error ", e)

desc = 0

if(CProducto>150000):
    desc = descuento(CProducto)
    print(f"El valor del producto es : {CProducto}")
    print(f"El valor de descuento del producto es : {desc}")
else:
    print(f"El valor del producto es : {CProducto}")
    print(f"El valor de descuento del producto es : {desc}")

