import clases

personas = clases.Persona()

personas.setNombre("Mike")
personas.setApellidos("Castañeda")
personas.setAltura("1.90m")
personas.setEdad("900 años")

print(f"La persona es: {personas.getNombre()} {personas.getApellidos()}")


print(personas.hablar())


informatico = clases.Informatico()
informatico.setNombre("Karen")
informatico.setApellidos("Barrera")

print(f"\nEl informatico es: {informatico.getNombre()} {informatico.getApellidos()}")

print(informatico.getLenguajes())
print(informatico.caminar())
print(informatico.experienca())

tecnico = clases.TecnicoRedes()
tecnico.setNombre("Manolito")
print(tecnico.audiatarRedes,tecnico.getNombre(),tecnico.getLenguajes())