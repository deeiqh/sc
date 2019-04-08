cad = "Puedo escribir los versos más tristes esta noche. Escribir, por ejemplo: \"La noche está estrellada, y tiritan, azules, los astros, a lo lejos.\" El viento de la noche gira en el cielo y canta. Puedo escribir los versos más tristes esta noche. Yo la quise, y a veces ella también me quiso. En las noches como esta la tuve entre mis brazos. La besé tantas veces bajo el cielo infinito. Ella me quiso, a veces yo también la quería. Cómo no haber amado sus grandes ojos fijos. Puedo escribir los versos más tristes esta noche. Pensar que no la tengo. Sentir que la he perdido. Oir la noche inmensa, más inmensa sin ella. Y el verso cae al alma como al pasto el rocío. Qué importa que mi amor no pudiera guardarla. La noche está estrellada y ella no está conmigo."

def sustitucion_letras(cad):	
	cambios =	{	
				'j': 'i', 
				'h': 'i',
				'ñ': 'n',
				'k': 'l',
				'u': 'v',
				'w': 'v',
				'y': 'z'			
			}

	texto_claro = ""
	for c in cad:
		if cambios.get(c) !=  None:
			texto_claro += cambios[c]
		else:
			texto_claro += c
	return texto_claro

def eliminar_tildes(cad):
	cambios =	{	
				'á':'a',
				'é':'e',
				'í':'i',
				'ó':'o',
				'ú':'u',			
			}

	texto_claro = ""
	for c in cad:
		if cambios.get(c) !=  None:
			texto_claro += cambios[c]
		else:
			texto_claro += c
	return texto_claro

def a_mayuscula(cad):
	texto_claro = ""
	letras = ['a','b','c','d','e','f','g','i','l','m','n','o','p','q','r','s','t','v','x','z']
	for c in cad:
		if c in letras:
			texto_claro += chr(ord(c)-32)
		else:
			texto_claro += c
	return texto_claro

def eliminar_blancos_puntuacion(cad):
	signos =	[' ',';',',','.',':','\'','\"','(',')','[',']','{','?','¿','¡','!','-']
	texto_claro = ""
	for c in cad:
		if c in signos:
			texto_claro += ''
		else:
			texto_claro += c
	return texto_claro

def main():
	print(cad+'\n')
	#print(sustitucion_letras(cad))
	aux = a_mayuscula(eliminar_tildes(sustitucion_letras(cad)))
	texto_claro = eliminar_blancos_puntuacion(aux)

	txt = open("poema20_pre.txt",'w')
	txt.write(texto_claro)
	txt.close()

	print(texto_claro)

main()





