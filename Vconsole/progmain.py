from classeSC import *
from grilles import *

####################################### Algo de reso #######################################
'''
def AlgoReso(x):
	for i in range(7):
		for j in range(4):
			if int(grille.item(i,j))==0 :
			
				if bool(SC1.Verif(i,j)):
					if bool(SC1.getEtat())==False:
						

						y=int(input("votre chiffre : "))
						if y>int(SC1.getTaille()) or y<=0 :
							print("erreur le chiffre ")
							continue
						if bool(EgalVoisin(a,b,y)):
							grille.itemset((a,b),y)
							SC1.ActuEtat()
							continue
						else :
							print("Un voisin contient deja cette valeur")
							continue
					else:
						continue
			else :
				continue

'''


 
####################################### Programme #######################################

Jeu_lance=True
Quit=False

while Jeu_lance==True and Quit==False:
	print(" ")
	print(grille)
	print("Sous case 1 = {} ".format(list(SC1.getListe())))
	print("Sous case 2 = {} ".format(list(SC2.getListe())))
	print("Sous case 3 = {} ".format(list(SC3.getListe())))
	print("Sous case 4 = {} ".format(list(SC4.getListe())))
	print("Sous case 5 = {} ".format(list(SC5.getListe())))
	print("Sous case 6 = {} ".format(list(SC6.getListe())))
	print("Sous case 7 = {} ".format(list(SC7.getListe()))) 

	if bool(SC1.getEtat()) and bool(SC2.getEtat()) and bool(SC3.getEtat()) and bool(SC4.getEtat()) and bool(SC5.getEtat()) and bool(SC6.getEtat()) and bool(SC7.getEtat()) :
		Jeu_lance= False
		continue

	print("Quels case voulez-vous modifier ?/ entrer -1 pour afficher la solution /entrer -2 pour quitter")
	
	a=int(input("Entrer la premiere coordonnee : "))
	if a==-2 : 
		Quit = True 
		continue
	if a==-1 :
		print(Sgrille)
		Quit = True
		continue
	
	b=int(input("Entrer la deuxieme coordonnee : "))

	if bool(Const(a,b)):
		print("Cette cellule n'est pas modifiable")
		continue

	if bool(Existe(a,b))==False:
		print("valeurs incorrectes veuillez rentrer des coordonnees correctes")
		continue

	if bool(SC1.Verif(a,b)):
		y=int(input("votre chiffre : "))
		if y>int(SC1.getTaille()) or y<=0 :
			print("erreur le chiffre ")
			continue
		if bool(EgalVoisin(a,b,y)):
			grille.itemset((a,b),y)
			SC1.ActuEtat()
			continue
		else :
			print("Un voisin contient deja cette valeur")
			continue

	if bool(SC2.Verif(a,b)):
		y=int(input("votre chiffre : "))
		if y>int(SC2.getTaille()) or y<=0 :
			print("erreur le chiffre ")
			continue
		if bool(EgalVoisin(a,b,y)):
			grille.itemset((a,b),y)
			SC2.ActuEtat()
			continue
		else :
			print("Un voisin contient deja cette valeur")
			continue

	if bool(SC3.Verif(a,b)):
		y=int(input("votre chiffre : "))
		if y>int(SC3.getTaille()) or y<=0 :
			print("erreur le chiffre ")
			continue
		if bool(EgalVoisin(a,b,y)):
			grille.itemset((a,b),y)
			SC3.ActuEtat()
			continue
		else :
			print("Un voisin contient deja cette valeur")
			continue

	if bool(SC4.Verif(a,b)):
		y=int(input("votre chiffre : "))
		if y>int(SC4.getTaille()) or y<=0 :
			print("erreur le chiffre ")
			continue
		if bool(EgalVoisin(a,b,y)):
			grille.itemset((a,b),y)
			SC4.ActuEtat()
			continue
		else :
			print("Un voisin contient deja cette valeur")
			continue

	if bool(SC5.Verif(a,b)):
		y=int(input("votre chiffre : "))
		if y>int(SC5.getTaille()) or y<=0 :
			print("erreur le chiffre ")
			continue
		if bool(EgalVoisin(a,b,y)):
			grille.itemset((a,b),y)
			SC5.ActuEtat()
			continue
		else :
			print("Un voisin contient deja cette valeur")
			continue

	if bool(SC6.Verif(a,b)):
		y=int(input("votre chiffre : "))
		if y>int(SC6.getTaille()) or y<=0 :
			print("erreur le chiffre ")
			continue
		if bool(EgalVoisin(a,b,y)):
			grille.itemset((a,b),y)
			SC6.ActuEtat()
			continue
		else :
			print("Un voisin contient deja cette valeur")
			continue

	if bool(SC7.Verif(a,b)):
		y=int(input("votre chiffre : "))
		if y>int(SC7.getTaille()) or y<=0 :
			print("erreur sur le chiffre")
			continue
		if bool(EgalVoisin(a,b,y)):
			grille.itemset((a,b),y)
			SC7.ActuEtat()
			continue
		else :
			print("Un voisin contient deja cette valeur")
			continue

if Jeu_lance==False: 
	print("bravo vous avez fini le jeu")
else : print("Aurevoir")