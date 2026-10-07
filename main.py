nombre = "Fran"
proyecto = "RAG PDF"

print("Hola", nombre)
print("Estamos construyendo:", proyecto)  

def saludar(nombre):
    return "Hola " + nombre

mensaje = saludar("Python")

print(mensaje)

frutas = ["manzana", "pera", "plátano"]

print(frutas[0])
print(frutas[2])

mensaje = {
    "role": "user",
    "content": "Hola, quiero aprender Python"
}

print(mensaje["role"])
print(mensaje["content"])