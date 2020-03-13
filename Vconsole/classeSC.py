from grilles import *

#Classes 

class SC:

	NbrSousCases = 0

	def __init__(self, etat=False, taille=0, l=[]):
		self.etat = etat
		self.taille = taille
		self.l = l
		SC.NbrSousCases += 1

	#ajoute une liste a une sous-grille
	def AjoutL(self, l):
		self.l.append(list(l))
		self.taille += 1 

	#cherche une case parmi une sous grille
	def Verif(self, x, y):
		for li in  self.l:
			if li==[int(x),int(y)] :
				return True
		return False

	#modifie true si sc est complet false sinon
	def ActuEtat(self):
		p=list()
		for li in self.l:
			if int(grille.item(int(li[0]),int(li[1])))==0:
				self.etat=False
				return
			else : 
				p.append(int(grille.item(int(li[0]),int(li[1]))))
		if int(len(p))==self.taille:
			for x in p:
				if int(p.count(x))!=1:
					self.etat=False
					return
			self.etat=True
			return
		else : return

	def getEtat(self):
		return self.etat

	def getTaille(self):
		return self.taille

	def getListe(self):
		return self.l


#Sous groupes 

SC1=SC(False, 5, [[0,0],[0,1],[1,1],[0,2],[0,3]]) 
SC2=SC(False, 1, [[1,0]])
SC3=SC(False, 3, [[1,2],[2,1],[2,2]])
SC4=SC(False, 6, [[1,3],[2,3],[3,1],[3,2],[3,3],[4,2]])
SC5=SC(False, 4, [[2,0],[3,0],[4,0],[5,0]])
SC6=SC(False, 6, [[4,1],[5,1],[5,2],[6,0],[6,1],[6,2]])
SC7=SC(False, 3, [[4,3],[5,3],[6,3]])