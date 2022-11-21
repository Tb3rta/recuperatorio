from recuperatorio.ejer1.SortedTableMap import SortedTableMap
print(f"{'':*^60}")
print(f"{' SortedTableMap ':*^60}")
print(f"{'':*^60}")
mapeo = SortedTableMap()

lorem_ipsum = """lorem ipsum dolor sit amet, consectetur adipiscing elit. duis nec ligula
dapibus, malesuada nibh in, porta massa. donec eget sodales tellus, non venenatis nisi.
praesent at lacinia ligula. praesent tristique, arcu nec suscipit facilisis, justo tellus
laoreet ex, sit amet pellentesque sem nisi nec ex. phasellus congue dapibus erat, vitae
vulputate nulla accumsan eget. praesent mi nisi, pellentesque ut ante sed, rutrum
malesuada mauris. aenean sed lacinia orci. sed et diam quis libero pulvinar facilisis.
etiam varius eu velit id mattis. sed consequat ex erat. quisque tincidunt malesuada
mauris sed faucibus."""
for texto in lorem_ipsum.split():
    palabra = ''.join(c for c in texto if c.isalpha())
    if palabra:
        mapeo[palabra] = 1 + mapeo.get(palabra, 0)

print(mapeo)

max_palabra = ''
max_cantidad = 0

for (p, c) in mapeo.items():
    if c > max_cantidad:
        max_palabra = p
        max_cantidad = c

print('La palabra más frecuente es:', max_palabra)
print('El número de ocurrencias es:', max_cantidad)

print("-------------------------------------")


