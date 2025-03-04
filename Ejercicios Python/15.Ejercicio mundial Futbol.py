Equipos=['1.Países Bajos vs. Estados Unidos.','2.Argentina vs. Australia.',
         '3.Francia vs. Polonia.','4.Inglaterra vs. Senegal.',
         '5.Japón vs. Croacia.','6.Brasil vs. Corea del Sur.',
         '7.Marruecos vs. España.','8.Portugal vs. Suiza.']
Resultados={}
print('Mundial Qatar 2022\n\nOctavos de final\n')

def Ganadores_octavos(Marcador, Equipo1,Equipo2):
    Goles=Marcador.split(' - ')
    Goles_1=int(Goles[0])
    Goles_2=int(Goles[1])
    return Equipo1 if Goles_1>Goles_2 else Equipo2
for Partidos in Equipos:
    print(Partidos)
    Marcador=input('Ingrese el marcador final (Formato: 2-1):')
    Resultados[Partidos]=Marcador
print('Ganadores de la fase de grupos')
for Partidos, Marcador in Resultados.items():
    print(len(Resultados))
    



    
