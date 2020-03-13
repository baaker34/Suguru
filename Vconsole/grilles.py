import numpy as np

################ Grille Solution ##############

grille = np.zeros((7,4), dtype=int)

grille.itemset(1,4)
grille.itemset(3,3)
grille.itemset(5,5)
grille.itemset(7,4)
grille.itemset(9,3)
grille.itemset(10,1)
grille.itemset(11,5)
grille.itemset(22,5)
grille.itemset(25,1)

################ Grille Solution ##############

Sgrille = np.zeros((7, 4), dtype=int)

Sgrille.itemset(0,2)
Sgrille.itemset(1,4)
Sgrille.itemset(2,1)
Sgrille.itemset(3,3)
Sgrille.itemset(4,1)
Sgrille.itemset(5,5)
Sgrille.itemset(6,2)
Sgrille.itemset(7,4)
Sgrille.itemset(8,4)
Sgrille.itemset(9,3)
Sgrille.itemset(10,1)
Sgrille.itemset(11,5)
Sgrille.itemset(12,1)
Sgrille.itemset(13,2)
Sgrille.itemset(14,6)
Sgrille.itemset(15,3)
Sgrille.itemset(16,3)
Sgrille.itemset(17,4)
Sgrille.itemset(18,1)
Sgrille.itemset(19,2)
Sgrille.itemset(20,2)
Sgrille.itemset(21,6)
Sgrille.itemset(22,5)
Sgrille.itemset(23,3)
Sgrille.itemset(24,3)
Sgrille.itemset(25,1)
Sgrille.itemset(26,2)
Sgrille.itemset(27,1)

############## Fonction ##############

#test l'existence d'une case		
def Existe(x,y):
	if int(x)<0 or int(x)>=7 or int(y)<0 or int(y)>=4 :
		return False 
	else : return True 


#renvoi faux si un voisin est égale 
def EgalVoisin(a,b,y):
	if bool(Existe((int(a)-1),(int(b)-1))):
		if int(grille.item((int(a)-1),(int(b)-1)))==int(y):
			return False
	if bool(Existe((int(a)-1),(int(b)))):
		if int(grille.item((int(a)-1),(int(b))))==int(y):
			return False
	if bool(Existe((int(a)-1),(int(b)+1))):
		if int(grille.item((int(a)-1),(int(b)+1)))==int(y):
			return False
	if bool(Existe((int(a)),(int(b)-1))):
		if int(grille.item((int(a)),(int(b)-1)))==int(y):
			return False
	if bool(Existe((int(a)),(int(b)+1))):
		if int(grille.item((int(a)),(int(b)+1)))==int(y):
			return False
	if bool(Existe((int(a)+1),(int(b)-1))):
		if int(grille.item((int(a)+1),(int(b)-1)))==int(y):
			return False
	if bool(Existe((int(a)+1),(int(b)))):
		if int(grille.item((int(a)+1),(int(b))))==int(y):
			return False
	if bool(Existe((int(a)+1),(int(b)+1))):
		if int(grille.item((int(a)+1),(int(b)+1)))==int(y):
			return False
	return True

#empeche la modification d'une constante
def Const(x,y):
	if (int(x)==0 and int(y)==1) or (int(x)==6 and int(y)==1) or (int(x)==1 and int(y)==1) or (int(x)==2 and int(y)==1) or (int(x)==2 and int(y)==2) or (int(x)==2 and int(y)==3) or (int(x)==1 and int(y)==3) or (int(x)==0 and int(y)==3) or (int(x)==5 and int(y)==2):
		return True
	else : return False