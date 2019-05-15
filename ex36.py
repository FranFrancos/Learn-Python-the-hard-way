from sys import exit

def camino_amarillo():
  print("Te encuentras a un mendigo en la puerta de una taberna.")
  print("-Necesito dinero para pasar una noche cómoda.")
  print("¿Que haces?")
  print("¿dar moneda, entrar en la taberna o pasar de largo?")

  next = input("> ")

  if next == "dar moneda":
    dar_moneda()
  elif next == "entrar en la taberna":
    entrar_taberna()
  elif next == "pasar de largo":
    pasar_de_largo()
  else:
    dead("La opción introducida no es válida.")

def dar_moneda():
  print("Sacas de tu mochila tu bolsa de monedas.")
  print("Mientras sacas una para dársela al mendigo...")
  print("Sientes una daga clavándose en tu vientre")
  print("-Mejor me llevo toda la bolsa hahahahaha.")
  dead("Sientes como tu vida se separa de tu cuerpo.")

def entrar_taberna():
  print("Te dispones a entrar en la taberna.")
  print("Al cruzar la puerta ves un reflejo a tú espalda.")
  print("se trata de una espada que cae sobre ti")
  dead("Antes de cerrar los ojos logras oír: -Aquí no aceptamos forasteros.")

def pasar_de_largo():
  print("Decides que aquél no es tu sitio y pasas de largo.")
  camino_verde()

def camino_rojo():
  print("Encuentras unos huevos que parecen ser de dragón.")
  print("¿Cual es tú decisión?")
  print("¿guardar en la mochila, romperlos o pasar de largo?")

  next = input("> ")

  if next == "guardar en la mochila":
    #funcion guardar_en_mochila
    print("Guardar en mochila.")
  elif next == "romerlos":
    #funcion romperlos
    print("Romperlos")
  elif next == "pasar de largo":
    #funcion pasar de largo
    print("Pasar de largo")
  else:
    dead("La opción introducida no es válida")

def camino_verde():
  print("Te abordan los guardias reales.")
  print("-Este es el bandido al que estabamos buscando")
  print("¿Que eliges?")
  print("se confunden, soy yo, escapar")

  next = input("> ")

  if next == "se confunden":
    #se_confunden()
    print("Se confunden")
  elif next == "soy yo":
    #soy_yo
    print("Soy yo")
  elif next == "escapar":
    #escapar()
    print("escapar")
  else:
    dead("La opción introducida no es válida.")



def start():
  print("Te encuentras ante tres caminos.")
  print("A la derecha amarillo, centro rojo e izquierda verde.")
  print("¿Que color eliges?")

  next = input("> ")

  if next == "amarillo":
    camino_amarillo()
  elif next == "rojo":
    camino_rojo()
  elif next == "verde":
    camino_verde()
  else:
    dead("El color introducido no es válido.")

def dead(porque):
  print(porque, "buen trabajo!")
  exit(0)

start()