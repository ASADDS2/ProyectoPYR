import os
from colorama import Fore, init
preguntas = [
    {
        "pregunta": "¿🇨‌ 🇺‌ 🇦 ‌🇱‌  🇪‌ 🇸‌  🇱‌ 🇦‌  🇨‌ 🇦‌ 🇵‌ 🇮‌ 🇹‌ 🇦‌ 🇱‌  🇩‌ 🇪 ‌ 🇨 ‌🇴‌ 🇱‌ 🇴‌ 🇲‌ 🇧 ‌🇮‌ 🇦 ‌?",
        "opciones": ["Barranquilla", "Bogota", "Santa Marta", "Medellín"],
        "respuesta_correcta": 2
    },
    {
        "pregunta": "  ¿🇨‌ 🇺‌ 🇦‌ 🇳‌ 🇹‌ 🇴‌  🇪‌ 🇸‌  5  🇽‌  6? ",
        "opciones": ["187187", "25", "11", "30"],
        "respuesta_correcta": 4
    },
    {
        "pregunta": "¿🇨‌ 🇺‌ 🇦‌ 🇱‌  🇪‌ 🇸‌  🇱‌ 🇦‌  🇨‌ 🇦 ‌🇵‌ 🇮‌ 🇹‌ 🇦‌ 🇱‌  🇩‌ 🇪‌  🇧‌ 🇷 ‌🇦‌ 🇸‌ 🇮‌ 🇱 ‌?",
        "opciones": ["Rio de Janeiro", "Sao paulo", "Brasilia", "Manaos"],
        "respuesta_correcta": 3
    },
  
    {
        "pregunta": "¿🇶‌ 🇺 ‌🇮‌ 🇪 ‌🇳‌  🇩 ‌🇪‌ 🇸‌ 🇨‌ 🇺 🇧‌ 🇷‌ 🇮 ‌🇴‌  🇦‌ 🇲‌ 🇪 ‌🇷‌ 🇮‌ 🇨‌ 🇦 ‌?",
        "opciones": ["Simon Bolivar", "Cristobal Colon", "La Policarpa", "Juan Manuel Santos"],
        "respuesta_correcta": 2
    },
  
  {
        "pregunta": "¿🇶‌ 🇺‌ 🇮‌ 🇪‌ 🇳‌  🇫 ‌🇺‌ 🇪‌  🇪‌ 🇱 ‌ 🇷‌ 🇪‌ 🇸 ‌🇵‌ 🇴‌ 🇳‌ 🇸 ‌🇦‌ 🇧‌ 🇱‌ 🇪‌  🇩‌ 🇪‌  🇱‌ 🇦‌  🇲‌ 🇺‌ 🇪‌ 🇷‌ 🇹 ‌🇪‌  🇩‌ 🇪‌  🇵‌ 🇦 ‌🇧‌ 🇱 ‌🇴‌  🇪‌ 🇸‌ 🇨‌ 🇴‌ 🇧‌ 🇦 ‌🇷 ‌?",
        "opciones": ["La Guerrilla de las Farc", "El cartel de Cali", "La DEA", "El bloque de busqueda"], 
        "respuesta_correcta": 4
    },
    {
        "pregunta": "¿🇩‌ 🇪‌  🇩‌ 🇴‌ 🇳‌ 🇩‌ 🇪‌  🇪‌ 🇸‌  🇪‌ 🇱‌  🇸‌ 🇴 ‌🇲‌ 🇧 ‌🇷‌ 🇪‌ 🇷‌ 🇴‌  🇻‌ 🇺‌ 🇪‌ 🇱‌ 🇹 ‌🇮‌ 🇦‌ 🇴 ‌?",
        "opciones": ["La Guajira", "Magdalena", "Sucre", "Cordoba"],
        "respuesta_correcta": 4
    },
     {
        "pregunta": "¿🇨‌ 🇺‌ 🇦‌ 🇱‌  🇪‌ 🇸‌  🇪 ‌🇱 ‌ 🇷‌ 🇮‌ 🇴‌  🇲‌ 🇦‌ 🇸‌  🇱‌ 🇦 ‌🇷‌ 🇬‌ 🇴‌  🇶‌ 🇺‌ 🇪‌  🇵 ‌🇦 ‌🇸‌ 🇦‌  🇵 ‌🇴 ‌🇷‌  🇨‌ 🇴‌ 🇱 ‌🇴‌ 🇲‌ 🇧 ‌🇮‌ 🇦 ‌?",
        "opciones": ["Cauca", "Sinu", "Amazonas", "Magdalena"],
        "respuesta_correcta": 3
    }
]

respuestas_usuario = []
correctas = 0

def limpiar_pantalla():
    # Limpia la pantalla de la consola.
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_pregunta(numero_pregunta, pregunta):
    # Muestra la pregunta y sus opciones.
    print(Fore.YELLOW + f"\nPregunta {numero_pregunta}: {pregunta['pregunta']}")
    for i, opcion in enumerate(pregunta["opciones"], start=1):
        print(Fore.BLUE + f"  {i}. {opcion}")

def obtener_respuesta():
    # Obtiene la respuesta del usuario con validación.
    while True:
        try:
            respuesta = int(input(Fore.WHITE + "Tu respuesta (1-4): "))
            if 1 <= respuesta <= 4:
                return respuesta
            else:
                print(Fore.RED + "Por favor, ingresa un número entre 1 y 4.")
        except ValueError:
            print(Fore.RED + "Entrada inválida. Debes ingresar una entrada valida.")

def mostrar_resultado(pregunta, respuesta_usuario, respuesta_correcta):
    # "Muestra si la respuesta fue correcta o incorrecta.
    if respuesta_usuario == respuesta_correcta:
        print(Fore.GREEN + "¡Correcto!")
    else:
        print(Fore.RED + f"Incorrecto. La respuesta correcta era: {respuesta_correcta}. {pregunta['opciones'][respuesta_correcta - 1]}")

def mostrar_resumen(preguntas, respuestas_usuario):
    # Muestra el resumen de resultados.
    print(Fore.LIGHTCYAN_EX + "\n=== Resumen de Resultados ===")
    for i, (pregunta, respuesta) in enumerate(zip(preguntas, respuestas_usuario), start=1):
        correcta = pregunta["respuesta_correcta"]
        print(f"{i}. {pregunta['pregunta']}:", end=" ")
        if respuesta == correcta:
            print(f"Correcto ({pregunta['opciones'][respuesta - 1]})")
        else:
            print(f"Incorrecto (Tu: {pregunta['opciones'][respuesta - 1]}, Correcta: {pregunta['opciones'][correcta - 1]})")

def calcular_porcentaje(correctas, total_preguntas):
    # Calcula el porcentaje de respuestas correctas.
    return (correctas / total_preguntas) * 100

# Inicio del cuestionario
limpiar_pantalla()
print("¡🇧‌ 🇮‌ 🇪‌ 🇳‌ 🇻 ‌🇪‌ 🇳‌ 🇮‌ 🇩‌ 🇴‌  🇦‌ 🇱‌  🇨 🇺‌ 🇪 ‌🇸‌ 🇹 🇮‌ 🇴‌ 🇳‌ 🇦‌ 🇷 ‌🇮 ‌🇴 ‌  🇩‌ 🇪‌  🇵 ‌🇷‌ 🇪 ‌🇬 ‌🇺‌ 🇳‌ 🇹‌ 🇦 🇸‌  🇾‌  🇷 🇪‌ 🇸 ‌🇵‌ 🇺‌ 🇪‌ 🇸 🇹 ‌🇦 ‌🇸‌  🇩‌ 🇪‌  🇨‌ 🇺‌ 🇱‌ 🇹‌ 🇺‌ 🇷‌ 🇦‌  🇬 ‌🇪 ‌🇳‌ 🇪 ‌🇷‌ 🇦‌ 🇱 ‌!")

for i, pregunta in enumerate(preguntas, start=1):
    mostrar_pregunta(i, pregunta)
    respuesta = obtener_respuesta()
    respuestas_usuario.append(respuesta)
    mostrar_resultado(pregunta, respuesta, pregunta["respuesta_correcta"])
    if respuesta == pregunta["respuesta_correcta"]:
      correctas +=1

#Mostrar resumen
print(Fore.MAGENTA + "\n========== RESULTADOS ==========")
for i, (pregunta, respuesta) in enumerate(zip(preguntas, respuestas_usuario), start=1):
    correcta = pregunta["respuesta_correcta"]
    texto = f"{i}. {pregunta['pregunta']}"
    if respuesta == correcta:
        print(Fore.GREEN + texto + f" ✅ (Tu respuesta: {pregunta['opciones'][respuesta-1]})")
    else:
        print(Fore.RED + texto + f" ❌ (Tu respuesta: {pregunta['opciones'][respuesta-1]} | Correcta: {pregunta['opciones'][correcta-1]})")

porcentaje = (correctas / len(preguntas)) * 100
print(Fore.CYAN + f"\nHas acertado {correctas} de {len(preguntas)} preguntas.")
print(Fore.CYAN + f"Tu porcentaje de exito fue: {porcentaje:.0f}%")

print(Fore.LIGHTGREEN_EX + "\n¡Gracias por jugar! 👋\n")