import json

def cargar_datos(archivo):
    try:
        with open(archivo, "r") as json_file:
            data = json.load(json_file)
    except FileNotFoundError:
        data = []
    return data

def guardar_datos(archivo, data):
    with open(archivo, "w") as json_file:
        json.dump(data, json_file, indent=4)
        
def Filtro(data_aux, pregunta, respuesta):
    data_aux = [superheroe for superheroe in data_aux if superheroe[pregunta] == respuesta]
    return data_aux

def buscar_superheroe(data, pregunta, respuesta):
    coincidencias = [superheroe for superheroe in data if superheroe[pregunta] == respuesta]
    if len(coincidencias) == 1:
        return coincidencias[0]["SuperHeroe"]
    return None

def nuevo_h(data, genero, fuerza, velocidad, rayos_laser, garras, invisible, volar, trepar, espadas, elastico):
    archivo = "SuperBD.json"
    data_h=cargar_datos(archivo)
    
    
    if genero is None:
        genero =input("¿Tu héroe es hombre o mujer? (Hombre, Mujer)\n")
    if fuerza is None:
        fuerza =input("¿Qué tan fuerte es tu héroe? (Baja, Media, Alta, Muy Alta, Super Alta)\n")
    if velocidad is None:
        velocidad =input("¿Qué tan rápido es tu héroe? (Baja, Media, Alta, Muy Alta, Super Alta)\n")
    if rayos_laser is None:
        rayos_laser =input("¿Tiene rallos láser? (Si, No)\n")
    if garras is None:
        garras =input("¿Tiene garras? (Si, No)\n")
    if invisible is None:
        invisible =input("¿Puede hacerse invisible? (Si, No)\n")
    if volar is None:
        volar =input("¿Puede volar? (Si, No)\n")
    if trepar is None:
        trepar =input("¿Puede trepar? (Si, No)\n")
    if espadas is None:
        espadas =input("¿Usa espadas? (Si, No)\n")
    if elastico is None:
        elastico =input("¿Es elástico? (Si, No)\n")
        
    
        
    Nom=input("¿Cual es su nombre?\n")
    TXT={
        "SuperHeroe": Nom ,
        "Genero": genero ,
        "SFuerza": fuerza ,
        "SVelocidad": velocidad ,
        "RallosLaser": rayos_laser ,
        "Garras": garras ,
        "Invisible": invisible ,
        "Volar": volar ,
        "Trepar": trepar ,
        "Espadas": espadas ,
        "Elastico": elastico
        }
    data_h.append(TXT)
    preguntas = [
        ("Genero", genero),
        ("SFuerza", fuerza),
        ("SVelocidad", velocidad),
        ("RallosLaser", rayos_laser),
        ("Garras", garras),
        ("Invisible", invisible),
        ("Volar", volar),
        ("Trepar", trepar),
        ("Espadas", espadas),
        ("Elastico", elastico)
    ]
    for pregunta, respuesta in preguntas:
      data_h=Filtro(data_h, pregunta, respuesta)
      superheroe = buscar_superheroe(data_h, pregunta, respuesta)
      if superheroe:
          print("Tu personaje fue agregado correctamente")
          break
    if not superheroe:
        print("Tu superhéroe ya estaba en la lista\n")
        return data
      
    data.append(TXT)
    guardar_datos(archivo, data)
    print("Bot: Nuevo heroe guardado\n")
    return data

def main():
    archivo = "SuperBD.json"
    data = cargar_datos(archivo)
    data_aux = cargar_datos(archivo)
    print("Bot: Hola, puedo ayudarte a encontrar un superhéroe. Responde a las siguientes preguntas:")

    genero = None
    fuerza = None
    velocidad = None
    rayos_laser = None
    garras = None
    invisible = None
    volar = None
    trepar = None
    espadas = None
    elastico = None

    preguntas = [
        ("Genero", "Bot: ¿Tu héroe es hombre o mujer? (Hombre, Mujer)"),
        ("SFuerza", "Bot: ¿Qué tan fuerte es tu héroe? (Baja, Media, Alta, Muy Alta, Super Alta)"),
        ("SVelocidad", "Bot: ¿Qué tan rápido es tu héroe? (Baja, Media, Alta, Muy Alta, Super Alta)"),
        ("RallosLaser", "Bot: ¿Tiene rallos láser? (Si, No)"),
        ("Garras", "Bot: ¿Tiene garras? (Si, No)"),
        ("Invisible", "Bot: ¿Puede hacerse invisible? (Si, No)"),
        ("Volar", "Bot: ¿Puede volar? (Si, No)"),
        ("Trepar", "Bot: ¿Puede trepar? (Si, No)"),
        ("Espadas", "Bot: ¿Usa espadas? (Si, No)"),
        ("Elastico", "Bot: ¿Es elástico? (Si, No)")
    ]

    for pregunta, descripcion in preguntas:
        respuesta = input(f"Bot: {descripcion}: \n").strip()
        if pregunta == "Genero":
            genero = respuesta
        elif pregunta == "SFuerza":
            fuerza = respuesta
        elif pregunta == "SVelocidad":
            velocidad = respuesta
        elif pregunta == "RallosLaser":
            rayos_laser = respuesta
        elif pregunta == "Garras":
            garras = respuesta
        elif pregunta == "Invisible":
            invisible = respuesta
        elif pregunta == "Volar":
            volar = respuesta
        elif pregunta == "Trepar":
            trepar = respuesta
        elif pregunta == "Espadas":
            espadas = respuesta
        elif pregunta == "Elastico":
            elastico = respuesta
        data_aux=Filtro(data_aux, pregunta, respuesta)
        superheroe = buscar_superheroe(data_aux, pregunta, respuesta)
        if superheroe:
            print(f"Bot: ¡Tu superhéroe es {superheroe}!")
            respuesta=input("¿Este es el heroe correcto?(si, no)\n")
            if respuesta.lower() == "no":
                nuevo_h(data, genero, fuerza, velocidad, rayos_laser, garras, invisible, volar, trepar, espadas, elastico)

            break

    if not superheroe:
        print("Bot: No conozco a este heroe ")
        nuevo_h(data, genero, fuerza, velocidad, rayos_laser, garras, invisible, volar, trepar, espadas, elastico)
        

while (True):
    finish=input("Bot:Para continuar presione enter\nBot: Para salir pulse q\n")
    if finish.lower() == "q":
        print("Bot: Adiós, hasta la próxima.")
        break
    main()
