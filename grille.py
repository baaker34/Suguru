from tkinter import *
from case import Case
from group import Group


class Grille:
	#constructeur grille aleatoire
	def __init__(self, window):
		#attributs
		self.__window = window
		self.__n = 0 #taille de la grille
		self.__selected = None #case selectionnée
		self.__matrice = [] #matrices des cases
		self.__list_group = [] #liste des groupe

		self.create_frame()

		#devra généré une grille aléatoire

		self.pack_frame()


	#constructeur grille a partir d'un fichier de config
	def __init__(self, window, cfg):
		#attributs
		self.__window = window
		self.__n = 0 #taille de la grille
		self.__selected = None #case selectionnée
		self.__matrice = [] #matrices des cases
		self.__list_group = [] #liste des groupe

		self.create_frame()

		self.load_config(cfg) #charge la grille selectionné dans les options

		self.pack_frame() #l'affiche

		self.load_change_grid()


	#charge une grille a partir d'un fichier de config
	def load_config(self, name):
		file = open("config.cfg", "r")

		lines = file.readlines() #récupere une liste contenant toutes les lignes du fichier de config
		length = len(lines) #compte le nombre de lignes

		#recherche de la config specifié dans le fichier (jusqu'a la fin du fichier)
		k = 0
		lines[k] = lines[k].rstrip()
		while lines[k] != name and k < length:
			k += 1
			lines[k] = lines[k].rstrip() #enleve les \r\n ou \n a la fin

		k += 1  #avance d'une ligne

		n = int(lines[k][0]) # n = taille de la grille
		self.__n = n #on iscrit la taille comme parametre de la grille

		k += 1  #avance d'une ligne

		# rappel :  dans x:y, x est le numero affiché dans une case, et y le numero du groupe
		grid = self.configFormat(lines, k, n) #grille de taille n de couple x:y

		self.create_config(grid, n) #charge et place les widget


	#met la config choisie sous forme exploitable / enleve les caracteres inutiles / isoles les x:y (cf fichier de config)
	def configFormat(self, lines, k, n):
		grid = []
		l = len(lines[k])-1 #nombre de caractere d'une ligne -1
		for i in range(n):
			sgrid = [] #une ligne de la matrice
			for j in range(l):
				if lines[k+i][j] ==":": #pour chaque ':' trouver on regarde ce qu'il y a a gauche et a droite
					sgrid.append(lines[k+i][j-1]+lines[k+i][j]+lines[k+i][j+1]) #on met x:y dans une ligne
			grid.append(sgrid) #on ajoute la ligne a la matrice
		return grid


	#charge et place les widget dans la grille
	def create_config(self, grid, n):
		for i in range(n):
			sgrid = [] #initialise une ligne
			for j in range(n):
				num = int(grid[i][j][0]) #chifre de la case
				numGrp = int(grid[i][j][2]) #numero du groupe

				if num > 0:
					estModifiable = False # on est dans une config précréer, alors on ne veut pas modifier les case qui on un numero
				else:
					estModifiable = True
					num = "" #pas de numero pour les autres cases

				# creation de la case
				case = Case(self.__frame, "btn{}{}".format(i, j), num, estModifiable, i, j, self)

				# on ajoute la case dans la ligne
				sgrid.append(case)

				# placement de la case
				case.btn.grid(row=i, column=j)

				#on met la case dans son groupe
				self.addInGroup(case, numGrp)

			self.__matrice.append(sgrid) #ajout de la ligne dans la grille

		self.colorError() #colore en rouge les nombres identique et cote a cote



	#colore en rouge les nombres identique et cote a cote et les doublon dans un groupe
	#de plus renvoie vrai si il n'y a aucune erreurs (cf victoire)
	def colorError(self):
		#reinitialise les couleurs avant de recolorier les erreurs
		for i in range(self.__n):
			for j in range(self.__n):
				if self.__matrice[i][j] == self.__selected: #on ne change pas le bg de la case selectionnée
					self.__matrice[i][j].bgYellow()
				else:#sinon on met la couleur de base de la case
					if self.__matrice[i][j].getEstModif():
						self.__matrice[i][j].bgLightGray()
					else:
						self.__matrice[i][j].bgGray()
				#deux couleur differente selon si la case est modifiable ou non

		res = True# res sert a determiner la victoire

		#pour les groupes
		for i in self.__list_group:
			# si res est a faux alors on y touche plus mais on termine le coloriage
			if res is not False:
				res = i.colorGroupError()
			else:
				i.colorGroupError()

		#pour les cases cote a cote
		for i in range(self.__n):
			for j in range(self.__n):
				#teste les 4 case a coté de celle au rang [i][j] et les colore si elles ont le meme numero
				if self.__matrice[i][j].getNum() != "":
					if i+1 < self.__n:
						if self.__matrice[i][j].getNum() == self.__matrice[i+1][j].getNum():
							self.__matrice[i][j].bgRed()
							self.__matrice[i+1][j].bgRed()
							if res is not False:
								res = False

					if j+1 < self.__n :
						if self.__matrice[i][j].getNum() == self.__matrice[i][j+1].getNum():
							self.__matrice[i][j].bgRed()
							self.__matrice[i][j+1].bgRed()
							if res is not False:
								res = False

					if i-1 >= 0 :
						if self.__matrice[i][j].getNum() == self.__matrice[i-1][j].getNum():
							self.__matrice[i][j].bgRed()
							self.__matrice[i-1][j].bgRed()
							if res is not False:
								res = False

					if j-1 >= 0 :
						if self.__matrice[i][j].getNum() == self.__matrice[i][j-1].getNum():
							self.__matrice[i][j].bgRed()
							self.__matrice[i][j-1].bgRed()
							if res is not False:
								res = False
		return res

	#affiche les boutons pour changer la valeur d'un bouton
	def load_change_grid(self):
		self.frame2 = Frame(self.__window)
		k = 0 #s'incremente jusqu'a 9
		for i in range(3):
			for j in range(3):
				k += 1
				Button(self.frame2, text="{}".format(k), width=5, height=2, command=lambda i=k: self.__selected.changeVal(i)).grid(row=i, column=j)

		self.frame2.place(relx=0.5, rely=0.85, anchor=CENTER)


	def addInGroup(self, case, numGrp):
		nom = "groupe{}".format(numGrp)

		#si le groupe existe deja, ajoute la case dedans
		for x in self.__list_group:
			if x.getNom() == nom:
				x.ajout(case)
				return

		#crée un groupe, y ajoute la case et l'ajoute dans la liste des groupes
		grp = Group(nom)
		grp.ajout(case)
		self.__list_group.append(grp)


	def setSelected(self, obj):
		if self.__selected is not obj:
			try: #si une case est deja selectionnée, remet sa couleur a la normale
				self.__selected.bgLightGray()
			except:
				pass
			self.__selected = obj #selectionne la case
			self.colorError()
			self.__selected.bgYellow() #met la couleur a jaune

	#renvoie le groupe dans lequel la case est
	def getGrp(self, case):
		for x in self.__list_group:
			for y in x:
				if y.getNom() == case.getNom():
					return x
		return False

	#renvoie True si la victoire est acquise et dessine un gros VCTOIRE
	def victory(self):
		if(self.colorError() and self.remplie()): #si le grille est remplie et qu'il n'y a pas d'erreur : on gagne
			self.frame_vict = Frame(self.__window)
			Label(self.frame_vict, text = "VICTOIRE", font = ("Courrier", 40), fg="green").pack()
			self.frame_vict.place(relx=0.5, rely=0.25, anchor=CENTER)
		else:
			return False

	#renvoie vraie si toutes les cases sont remplies par un chiffre
	def remplie(self):
		for i in range(self.__n):
			for j in range(self.__n):
				if self.__matrice[i][j].getNum() == "":
					return False
		return True


	#créer une frame
	def create_frame(self) :
		self.__frame = Frame(self.__window)


	# empaquetage d'une frame
	def pack_frame(self) :
		self.__frame.pack(expand = YES, side = "top")

	#renvoie la frame
	def getFrame(self):
		return self.__frame