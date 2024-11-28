## Problema numero 1 Niedferson Vargas

vaca = 1
metros = int(input("Cuantos metros cuadrados tiene de pasto?: "))

leche_por_dia = vaca * metros

leche_semanal = leche_por_dia * 7
print(f"a la semana se producen {leche_semanal} litros de leche")

##Problema numero 2 

def huevos_mes(aves):

    gallinas = aves / 3
    huevos = (gallinas / 2) * (30 // 3) + (gallinas / 2) * (30 // 5)
    return int(huevos)

aves = int(input("Número total de aves: "))
print(f"Huevos producidos en un mes: {huevos_mes(aves)}")
