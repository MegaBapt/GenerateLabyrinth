import random
labi = {
	1: [4,4,4,4,4,4,4,2,2,2,2,2,2,2,2,2], 
	2: [4,4,4,4,4,4,4,2,2,2,2,2,2,2,2,2],
	3: [4,4,4,4,4,4,4,2,2,2,2,2,2,2,2,2], 
	4: [4,4,4,4,4,4,4,2,2,2,2,2,2,2,3,2], 
	5: [4,4,4,4,4,4,4,2,2,2,2,2,2,2,2,3], 
	6: [4,4,4,4,4,4,4,2,2,2,2,2,2,2,2,2], 
	7: [4,4,4,4,4,4,4,2,2,2,2,2,2,2,2,2], 
	8: [4,4,4,4,4,4,4,5,3,3,3,3,3,3,3,2], 
	9: [1,1,1,1,1,1,1,1,3,3,3,3,3,3,3,3],
	10:[1,1,1,1,1,1,1,1,3,3,3,3,3,3,3,3],
	11:[1,1,1,1,1,1,1,1,3,3,3,3,3,3,3,3],
	12:[1,1,1,1,1,1,1,1,3,3,3,3,3,3,1,3],
	13:[1,1,1,1,1,1,1,1,3,3,3,3,3,3,2,3],
	14:[1,1,1,1,1,1,1,1,3,3,3,3,3,3,3,3],
	15:[1,1,1,1,1,1,1,1,3,3,3,3,3,3,3,3],
	16:[1,1,1,1,1,1,1,1,3,3,3,3,3,3,3,3]

} 
itération = len(labi)*1000
changement = 0
direction = 1

position_5 = 2
ligne_5 = 3
SHOW_DEBUG = False

def fleche():
	strd =''
	for tric in labi:
		for trac in labi[tric]:
			if trac == 5:
				strd += str(f"\033[1;31m{trac}\033[1;37m")
			else:
				strd += str(trac)
		return strd
		strd=''


def logDebug(strLog, bShow = SHOW_DEBUG):
	if (bShow):
		print(strLog)

def inversion(ligne_5, ligne, position_5, position, direction):
	global changement
	logDebug(f"Inversion : {ligne_5} - {ligne} - {position_5} - {position}", False)
	labi[ligne_5][position_5] = direction
	labi[ligne][position] = 5


while changement < itération:
	position2 = position_5 + 1
	tour2 = 0
	direction = random.randint(1, 4)
	avancé = random.randint(1, 5)
	ligne1 = ligne_5 - 1
	ligne2 = ligne_5 + 1
	logDebug(f"{changement} - {itération}")
	while avancé != tour2:
		match direction:
			# Aller en haut
			case 1:
				logDebug(f"Case 1 : {ligne_5} - {position_5} ",)
	#				print(changement)
				if ligne_5 == 1:
					changement = changement -1
				else:
#					print("truc2")
					inversion(ligne_5, ligne_5-1, position_5, position_5, direction)
					ligne_5 = ligne_5-1
			# Aller en bas
			case 2:
				logDebug(f"Case 2 : {ligne_5} - {position_5} ")
				if ligne_5 >= len(labi):
					changement = changement -1
				else:
					inversion(ligne_5, ligne_5+1, position_5, position_5, direction)
					ligne_5 = ligne_5+1	
			# Aller à gauche
			case 3:
				logDebug(f"Case 3 : {ligne_5} - {position_5}")			
				if position_5 == 0:
					changement = changement - 1
				elif position_5 < 0:
					logDebug("position_5 est trop bas", True)
				else:
					inversion(ligne_5, ligne_5, position_5, position_5 - 1, direction)
					position_5 = position_5 - 1
			# Aller à droite
			case 4:
				logDebug(f"Case 4 : {ligne_5} - {position_5} ")			
#				print(changement)
				if position_5 == len(labi[ligne_5])-2 :	
					changement = changement - 1
				else:
					inversion(ligne_5, ligne_5, position_5, position_5 + 1, direction)
					position_5 = position_5 + 1
			case _:
				logDebug("Je n'ai rien a faire ici")
		changement = changement + 1
		tour2 = tour2+1

logDebug(fleche())

nombre2 = []
itération = 0
tour = 0
ligne1 = 1 
nombre = 0

affichage = ''
while tour != len(labi[1]):
	affichage = affichage + "=|"
	tour = tour +1
tour = 0
print(f"|{affichage}")
while itération != len(labi):
	while tour != len(labi[ligne1])-1:

		if (labi[ligne1][nombre] == 4) or (labi[ligne1][nombre+1] == 3):
			nombre2.append("  ")
		else:
			nombre2.append(" |")
		nombre = nombre+1
		tour = tour+1
	tour = 0
	nombre = 0
	affichage = ''
	for mur in nombre2:
		affichage = affichage + mur
	if ligne1 == 1:
		print(f">{affichage} |")
	elif ligne1 == len(labi):
		print(f"|{affichage} > ")
	else:
		print(f"|{affichage} |")
	nombre2.clear()
	while tour != len(labi[ligne1]):
		if ligne1 == len(labi):
			nombre2.append("=|")
		elif (labi[ligne1][nombre] == 2) or (labi[ligne1+1][nombre] == 1):
			nombre2.append(" |")
		else:
			nombre2.append("=|")
		nombre = nombre+1
		tour = tour+1
	tour = 0
	nombre = 0
	affichage = ''
	for mur in nombre2:
		affichage = affichage + mur
	print(f"|{affichage}")
	nombre2.clear()
	ligne1 = ligne1+1
	itération = itération +1

