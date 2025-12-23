equipos = [
{"pais":"Canadá","confederacion":"CONCACAF"},
{"pais":"México","confederacion":"CONCACAF"},
{"pais":"Estados Unidos","confederacion":"CONCACAF"},
{"pais":"Panamá","confederacion":"CONCACAF"},
{"pais":"Haití","confederacion":"CONCACAF"},
{"pais":"Curaçao","confederacion":"CONCACAF"},
{"pais":"Japón","confederacion":"AFC"},
{"pais":"Irán","confederacion":"AFC"},
{"pais":"Corea del Sur","confederacion":"AFC"},
{"pais":"Australia","confederacion":"AFC"},
{"pais":"Arabia Saudita","confederacion":"AFC"},
{"pais":"Qatar","confederacion":"AFC"},
{"pais":"Uzbekistán","confederacion":"AFC"},
{"pais":"Jordania","confederacion":"AFC"},
{"pais":"Argentina","confederacion":"CONMEBOL"},
{"pais":"Ecuador","confederacion":"CONMEBOL"},
{"pais":"Colombia","confederacion":"CONMEBOL"},
{"pais":"Uruguay","confederacion":"CONMEBOL"},
{"pais":"Brasil","confederacion":"CONMEBOL"},
{"pais":"Paraguay","confederacion":"CONMEBOL"},
{"pais":"Nueva Zelanda","confederacion":"OFC"},
{"pais":"Marruecos","confederacion":"CAF"},
{"pais":"Túnez","confederacion":"CAF"},
{"pais":"Egipto","confederacion":"CAF"},
{"pais":"Argelia","confederacion":"CAF"},
{"pais":"Ghana","confederacion":"CAF"},
{"pais":"Cabo Verde","confederacion":"CAF"},
{"pais":"Sudáfrica","confederacion":"CAF"},
{"pais":"Costa de Marfil","confederacion":"CAF"},
{"pais":"Senegal","confederacion":"CAF"},
{"pais":"Inglaterra","confederacion":"UEFA"},
{"pais":"Francia","confederacion":"UEFA"},
{"pais":"Croacia","confederacion":"UEFA"},
{"pais":"Portugal","confederacion":"UEFA"},
{"pais":"Noruega","confederacion":"UEFA"},
{"pais":"Alemania","confederacion":"UEFA"},
{"pais":"Países Bajos","confederacion":"UEFA"},
{"pais":"Bélgica","confederacion":"UEFA"},
{"pais":"Austria","confederacion":"UEFA"},
{"pais":"Suiza","confederacion":"UEFA"},
{"pais":"España","confederacion":"UEFA"},
{"pais":"Escocia","confederacion":"UEFA"}

]


UEfa = 0
CONmebol = 0
CAF = 0
AFC = 0
OFC = 0
CONCACAF = 0
repechaje = 0

for equipo in equipos:
    if equipo["confederacion"] == "UEFA":
        UEfa += 1
    elif equipo["confederacion"] == "CONMEBOL":
        CONmebol += 1
    elif equipo["confederacion"] == "CAF":
        CAF += 1
    elif equipo["confederacion"] == "CONCACAF":
        CONCACAF += 1
    elif equipo["confederacion"] == "AFC":
        AFC += 1
    elif equipo["confederacion"] == "OFC":
        OFC += 1
    else:
        repechaje += 1

cantidad_equipos = [
    {"confederacion":"UEFA","cantidad":UEfa},
    {"confederacion":"CONMEBOL","cantidad":CONmebol},
    {"confederacion":"CAF","cantidad":CAF},
    {"confederacion":"AFC","cantidad":AFC},
    {"confederacion":"OFC","cantidad":OFC},
    {"confederacion":"CONCACAF","cantidad":CONCACAF},
    {"confederacion":"Repechaje","cantidad":repechaje}
]

confederaciones = {}

for equipo in equipos:
    confederacion = equipo["confederacion"]
    if confederacion not in confederaciones:
        confederaciones[confederacion] = []
    confederaciones[confederacion].append(equipo["pais"])
