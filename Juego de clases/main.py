from Guerrero import Guerrero
from Hechicero import Hechicero
from Espada import Espada
from Conjuro import Conjuro

# Crear personajes
guerrero = Guerrero("Thorg", 50)
hechicero = Hechicero("Merlin", 50)

# Crear objetos
espada = Espada("Espada de valor", 50)
conjuro = Conjuro("Bola de fuego", 50)

# Equipar objetos
guerrero.equipar_arma(espada)
hechicero.aprender_conjuro(conjuro)

# acciones del juego
guerrero.atacar(hechicero)
hechicero.lanzar_conjuro(guerrero)