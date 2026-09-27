estudiantes = ["ANDRES", "PABLO", "SAUL"]
print("Lista inicial:", estudiantes)

estudiantes.append("SANTOS")
print("Después de agregar a SANTOS:", estudiantes)

estudiantes.remove("ANDRES")
print("Después de eliminar a ANDRES:", estudiantes)

nombre_buscar = "PABLO"
if nombre_buscar in estudiantes:
    print(f"El nombre buscado es: {nombre_buscar}")

print("\nLista completa de estudiantes:")
for est in estudiantes:
    print(f"- {est}")
