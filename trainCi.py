# Generated automatically with "cito". Do not edit.

class Main:

	@staticmethod
	def main(args):
		list_gare = ListGare()
		g1 = Gare()
		g1.init("Lille")
		list_gare.add_to_list(g1)
		g2 = Gare()
		g2.init("Paris")
		list_gare.add_to_list(g2)
		g3 = Gare()
		g3.init("Lyon")
		list_gare.add_to_list(g3)
		g4 = Gare()
		g4.init("Calais")
		list_gare.add_to_list(g4)
		g5 = Gare()
		g5.init("Marseille")
		list_gare.add_to_list(g5)
		t1 = Train()
		t1.init(237, g1, g2, "08:00", "08:59")
		t2 = Train()
		t2.init(709, g1, g3, "07:00", "10:00")
		t3 = Train()
		t3.init(900, g2, g5, "12:00", "18:00")
		list_gare.trajet_moins_long("Lille", "Marseille")

class Train:

	def __init__(self):
		pass

	def init(self, n_distance, n_depart_gare, n_arrive_gare, n_depart, n_arrive):
		self._distance = n_distance
		horaire = Horaire()
		horaire.init(n_depart, n_arrive, n_depart_gare)
		self._temps = horaire
		self._gare_depart = n_depart_gare
		self._gare_arrive = n_arrive_gare
		n_depart_gare.set_list_train_depart(self)
		n_arrive_gare.set_list_train_arrive(self)

	def get_gare_arrive(self):
		return self._gare_arrive

	def get_gare_depart(self):
		return self._gare_depart

	def get_distance(self):
		return self._distance

	def get_horaire(self):
		return self._temps

	def to_string(self):
		return f"Train de la gare de {self._gare_depart.get_ville()} pour {self._gare_arrive.get_ville()}, {self._temps.to_string()}, {self._distance} Km \n"

	def calcul_vitesse(self):
		heure_depart = self._temps.get_depart()[0:2]
		sec_depart = String2Int.parse_unsigned_int(heure_depart) * 3600
		minute_depart = self._temps.get_depart()[3:5]
		sec_depart += String2Int.parse_unsigned_int(minute_depart) * 60
		heure_arrive = self._temps.get_arrive()[0:2]
		sec_arrive = String2Int.parse_unsigned_int(heure_arrive) * 3600
		minute_arrive = self._temps.get_arrive()[3:5]
		sec_arrive += String2Int.parse_unsigned_int(minute_arrive) * 60
		sec_diff = sec_arrive - sec_depart
		vitesse = int(self._distance * 1000 / sec_diff)
		print(f"La vitesse moyenne prévu du train est {vitesse} m/s \n", end="")
		return vitesse

class Horaire:

	def __init__(self):
		pass

	def init(self, n_depart, n_arrive, n_gare):
		self._depart = n_depart
		self._arrive = n_arrive
		self._gare = n_gare
		self._gare.set_list_horaire(self)

	def get_depart(self):
		return self._depart

	def get_arrive(self):
		return self._arrive

	def to_string(self):
		return f"Depart à {self._depart} arrivée à {self._arrive}"

class Gare:

	def __init__(self):
		self._list_train_depart = []
		self._list_train_arrive = []
		self._list_horaire = []

	def init(self, n_ville):
		self._ville = n_ville

	def get_list_train(self):
		return self._list_train_depart

	def get_ville(self):
		return self._ville

	def set_list_horaire(self, h):
		self._list_horaire.append(h)

	def set_list_train_depart(self, t):
		self._list_train_depart.append(t)

	def set_list_train_arrive(self, t):
		self._list_train_arrive.append(t)

	def ville_depart(self):
		for train in self._list_train_depart:
			print(train.to_string(), end="")

class ListGare:

	def __init__(self):
		self._list_gare = []
		self._list_train = []

	def get_list_gare(self):
		return self._list_gare

	def get_list_train(self):
		return self._list_train

	def add_to_list(self, g):
		self._list_gare.append(g)

	def vitesse_plus_eleve(self):
		vitesse_max = 0
		for gare in self._list_gare:
			for train in gare.get_list_train():
				vitesse = train.calcul_vitesse()
				if vitesse > vitesse_max:
					vitesse_max = vitesse
					temp_train = train
		print(f"Le train le plus rapide est {temp_train.to_string()}\n", end="")
		return temp_train

	def parcourir_train(self):
		for train in self._list_train:
			print(train.to_string(), end="")

	def tri_horaire(self):
		self._list_train.clear
		for gare in self._list_gare:
			for train in gare.get_list_train():
				self._list_train.append(train)
		for i in range(len(self._list_train) - 1, -1, -1):
			comp_horaire = String2Int.to_second(self._list_train[i].get_horaire().get_depart())
			for j in range(i - 1, -1, -1):
				comp_horaire1 = String2Int.to_second(self._list_train[j].get_horaire().get_depart())
				if comp_horaire < comp_horaire1:
					temp = self._list_train[i]
					del self._list_train[i]
					self._list_train.insert(j, temp)
		self.parcourir_train()
		return self._list_train

	def calcul_duree(self, depart, arrive):
		heure_depart = depart[0:2]
		sec_depart = String2Int.parse_unsigned_int(heure_depart) * 3600
		minute_depart = depart[3:5]
		sec_depart += String2Int.parse_unsigned_int(minute_depart) * 60
		heure_arrive = arrive[0:2]
		sec_arrive = String2Int.parse_unsigned_int(heure_arrive) * 3600
		minute_arrive = arrive[3:5]
		sec_arrive += String2Int.parse_unsigned_int(minute_arrive) * 60
		sec_diff = sec_arrive - sec_depart
		hours = int(sec_diff / 3600)
		minutes = int(sec_diff % 3600 / 60)
		seconds = sec_diff % 60
		print(f"Le trajet durera {hours} heures et {minutes} minutes \n", end="")
		return sec_diff

	def train_apres(self, res):
		for train in res:
			for train2 in self._list_train:
				if train.get_gare_arrive().get_ville() == train2.get_gare_depart().get_ville() and String2Int.to_second(train.get_horaire().get_arrive()) < String2Int.to_second(train2.get_horaire().get_depart()):
					res.append(train2)
		return res

	def trajet_moins_long(self, depart, arrive):
		existe_d = False
		existe_a = False
		result = []
		for gare in self._list_gare:
			if gare.get_ville() == depart:
				existe_d = True
			if gare.get_ville() == arrive:
				existe_a = True
		if not existe_a and not existe_d:
			print("la ligne n'existe pas 1", end="")
			result.clear
			return result
		self.tri_horaire()
		temp_train = self.vitesse_plus_eleve()
		if temp_train.get_gare_depart().get_ville() == depart and temp_train.get_gare_arrive().get_ville() == arrive:
			print(f"Le trajet le moins ce fait par le train de {temp_train.to_string()}", end="")
			result.append(temp_train)
			return result
		else:
			chemin_possible = {}
			i = 0
			while i < len(self._list_train):
				res = []
				res.append(self._list_train[i])
				chemin_possible[i] = res
				i += 1
			duree_min = 1000000
			meilleur_chemin = []
			for j, tes in chemin_possible.items():
				meilleur_chemin = self.train_apres(tes)
				depart_t = meilleur_chemin[0].get_horaire().get_depart()
				arrive_t = meilleur_chemin[-1].get_horaire().get_arrive()
				duree = self.calcul_duree(depart_t, arrive_t)
				if duree_min > duree and meilleur_chemin[0].get_gare_depart().get_ville() == depart and meilleur_chemin[-1].get_gare_arrive().get_ville() == arrive:
					duree_min = duree
					index = j
			result = chemin_possible[index]
			print(f"Le trajet le plus rapide est le {index} pour {depart} -> {arrive}", end="")
			return result

class String2Int:

	@staticmethod
	def parse_unsigned_int(s):
		if len(s) == 0:
			raise Exception("Empty string")
		r = 0
		for c in s:
			if ord(c) < 48 or ord(c) > 57:
				raise Exception("Not a digit")
			if r > 214748364 or (r == 214748364 and ord(c) >= 56):
				raise Exception("Number too big")
			r = r * 10 + ord(c) - 48
		return r

	@staticmethod
	def to_second(s):
		to_sec = String2Int.parse_unsigned_int(s[0:2]) * 3600
		to_sec += String2Int.parse_unsigned_int(s[3:5]) * 60
		return to_sec
Main.main(0)