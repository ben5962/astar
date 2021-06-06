import unittest
from alea import entier_aleatoire_dans_intervalle
class le_test(unittest.TestCase):
	def test_entier_aleatoire_dans_intervalle(self):
		valeur_obtenue = entier_aleatoire_dans_intervalle(debut_intervalle = 0, fin_intervalle = 5)
		valeur_attendue = valeur_obtenue <= 5
		self.assertEquals(True, valeur_attendue)
