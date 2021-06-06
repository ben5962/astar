import unittest
from astar import est_cas_arret_pas_de_chemin, est_cas_arret_arrivee_atteinte, renvoyer_message_erreur_pas_de_chemin, renvoyer_message_succes, ajouterEnTeteDeCheminSommetConsidere, estCheminPlusCourtPassantParSommetNouvellementDecouvert, creer_chemin_optimal_depuis_liste_noeuds_traites, ajouter_successeurs_si_nouveaux_ou_meilleur_chemin, il_reste_des_noeuds_en_traitement_et_arrivee_pas_atteinte, estSommetNouvellementDecouvertAbsentDeListePrioNoeudsEnTraitement, astar, verif_effets_de_bord_liste, EchecReconstructionCheminOptimalException
import ListeAssociativeDeSommetsVisites 
import Sommet
import copy


class le_test(unittest.TestCase):
    def test_est_cas_arret_pas_de_chemin(self):
        liste_priorite_noeuds_en_traitement = ListeAssociativeDeSommetsVisites.ListeAssociativeDeSommets()
        valeur_obtenue = est_cas_arret_pas_de_chemin(liste_priorite_noeuds_en_traitement )
        valeur_attendue = True
        self.assertEquals(valeur_obtenue, valeur_attendue)
                
    def test_est_cas_arret_arrivee_atteinte(self):
        arriv = Sommet.ClasseSommet(5,5)
        arriv.initArrivee()
        valeur_obtenue = est_cas_arret_arrivee_atteinte(noeud_en_traitement = arriv, arrivee = arriv )
        valeur_attendue = True
        self.assertEquals(valeur_obtenue, valeur_attendue)
    
    
    def test_ajouterEnTeteDeCheminSommetConsidere(self):
        valeur_obtenue = ajouterEnTeteDeCheminSommetConsidere(s = Sommet.ClasseSommet(1,1), chemin_optimal = [Sommet.ClasseSommet(0,0)] )
        valeur_attendue = [Sommet.ClasseSommet(1,1),Sommet.ClasseSommet(0,0)]
        self.assertEquals(valeur_obtenue, valeur_attendue)
    
    def test_estCheminPlusCourtPassantParSommetNouvellementDecouvert(self):
        le_sommet = Sommet.ClasseSommet(0,0,parcoursCumule=5)
        occurence_deja_presente_de_sommet_dans_liste_prio = Sommet.ClasseSommet(0,0,parcoursCumule=6)
        valeur_obtenue = estCheminPlusCourtPassantParSommetNouvellementDecouvert(le_sommet, occurence_deja_presente_de_sommet_dans_liste_prio )
        valeur_attendue = True
        self.assertEquals(valeur_obtenue, valeur_attendue)
        
    def test_creer_chemin_optimal_depuis_liste_noeuds_traites(self):
        une_arrivee = Sommet.ClasseSommet(5,3)
        une_arrivee.initArrivee()
        un_depart = Sommet.ClasseSommet(3,3)
        un_depart.initDepart(une_arrivee)
        au_milieu = Sommet.ClasseSommet(4,3)
        un_autre_au_pif_pas_a_prendre = Sommet.ClasseSommet(8,8)
        
        
        un_autre_au_pif_pas_a_prendre.antecedant = un_depart
        une_arrivee.antecedant = au_milieu
        au_milieu.antecedant = un_depart
        un_depart.antecedant = None
        
        une_liste_noeuds_traites = ListeAssociativeDeSommetsVisites.ListeAssociativeDeSommets()
        une_liste_noeuds_traites.append(un_depart)
        une_liste_noeuds_traites.append(une_arrivee)
        une_liste_noeuds_traites.append(au_milieu)
        une_liste_noeuds_traites.append(un_autre_au_pif_pas_a_prendre)
        
        valeur_obtenue = creer_chemin_optimal_depuis_liste_noeuds_traites(une_liste_noeuds_traites, arrivee = une_arrivee, depart = un_depart )
        valeur_attendue = [un_depart, au_milieu, une_arrivee]
        self.assertEquals(valeur_obtenue, valeur_attendue)

"""
	def test_ajouter_successeurs_si_nouveaux_ou_meilleur_chemin(self):
        #tester meilleur chemin
        noeud_en_traitement = Sommet.ClasseSommet(0,1)
        noeud_en_traitement.distanceParcourue = 1
        
        ancienne_version_du_noeud = 
        valeur_obtenue = ajouter_successeurs_si_nouveaux_ou_meilleur_chemin(noeud_en_traitement = TODO, le_graphe = TODO, liste_de_sommets_visites = TODO, liste_priorite_noeuds_en_traitement = TODO, )
        valeur_attendue = TODO
        self.assertEquals(valeur_obtenue, valeur_attendue)


	def test_il_reste_des_noeuds_en_traitement_et_arrivee_pas_atteinte(self):
		valeur_obtenue = il_reste_des_noeuds_en_traitement_et_arrivee_pas_atteinte(noeud_en_traitement = TODO, point_d_arrivee = TODO, )
		valeur_attendue = TODO
		self.assertEquals(valeur_obtenue, valeur_attendue)
	def test_estSommetNouvellementDecouvertAbsentDeListePrioNoeudsEnTraitement(self):
		valeur_obtenue = estSommetNouvellementDecouvertAbsentDeListePrioNoeudsEnTraitement(le_sommet = TODO, liste_priorite_noeuds_en_traitement = TODO, )
		valeur_attendue = TODO
		self.assertEquals(valeur_obtenue, valeur_attendue)
	def test_astar(self):
		valeur_obtenue = astar(le_graphe = TODO, point_de_depart = TODO, point_d_arrivee = TODO, liste_noeuds_traites = TODO, liste_priorite_noeuds_en_traitement = TODO, )
		valeur_attendue = TODO
		self.assertEquals(valeur_obtenue, valeur_attendue)
	def test_verif_effets_de_bord_liste(self):
		valeur_obtenue = verif_effets_de_bord_liste(liste = TODO, )
		valeur_attendue = TODO
		self.assertEquals(valeur_obtenue, valeur_attendue)

"""
