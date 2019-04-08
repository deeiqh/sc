'''
    1. Realizar las siguientes sustituciones:
    	 j x i, h x i, ñ,x n, k x l, u x v, w x,v, y x z
    2. Elimine las tildes 
    3. Convierta todas las letras a mayúsculas
    4. Elimine los espacios en blanco y los signos de puntuación
'''
cad = "Puedo escribir los versos más tristes esta noche. Escribir, por ejemplo: \"La noche está estrellada, y tiritan, azules, los astros, a lo lejos.\" El viento de la noche gira en el cielo y canta. Puedo escribir los versos más tristes esta noche. Yo la quise, y a veces ella también me quiso. En las noches como esta la tuve entre mis brazos. La besé tantas veces bajo el cielo infinito. Ella me quiso, a veces yo también la quería. Cómo no haber amado sus grandes ojos fijos. Puedo escribir los versos más tristes esta noche. Pensar que no la tengo. Sentir que la he perdido. Oir la noche inmensa, más inmensa sin ella. Y el verso cae al alma como al pasto el rocío. Qué importa que mi amor no pudiera guardarla. La noche está estrellada y ella no está conmigo."

cambios = {	
					'j': 'i', 
					'h': 'i',
					'ñ': 'n',
					'k': 'l',
					'u': 'v',
					'w': 'v',
					'y': 'z',
					'á':'a',
					'é':'e',
					'í':'i',
					'ó':'o',
					'ú':'u',
					' ':'' ,
					';':'',
					',':'',
					'.':'',
					':':'',
					'\'':'',
					'\"':'',
					'(':'',
					')':'',
					'[':'',
					']':'',
					'{':'',
					'?':'',
					'¿':'',
					'¡':'',
					'!':'',
					'-':''
					}

res = ""
for c in cad:
	if cambios.get(c) !=  None:
		res += cambios[c]
	else:
		res += c
res = res.upper()

txt = open("poema20_pre.txt",'w')
txt.write(res)
txt.close()

print (res)