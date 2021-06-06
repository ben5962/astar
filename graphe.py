# coding:utf-8

import Sommet
import typing
import traceback
import Environnement
import PileDePriorite
import copy

""" graphe est respoinsable de fournir la liste des successeurs d un sommet donné.
il fournit uniquement des successeurs qui ont les trois qualités suivantes:
   - qui sont dans le plateau de jeu
   - qui ne sont pas des obstacles (les successeurs en collision avec la liste des obstacles sont omis)
    -> il est donc dependant à environnement pour connaitre listeObstacles
   - dont les champs antecedants, distanceParcourue, classement et accessoirement distance à l arrivee
   sont mises à jour, donc prets à etres inseres dans la file de prio
"""

class SuccesseurInvalideException(Exception):
    """ leve quand le successeur porduit sort du cadre de jeu
    ou est un obstacle"""
    

class Succ:
    def __init__(self, environnement):
        try:
            self.environnement = environnement
            self.listeObstacles = environnement.listeDesObstacles
            
            
        except AttributeError as ae:
            print(ae)
            traceback.print_exc()
            
    def validerSuccesseur(self, s):
        """si le succcesseur est un obstacle, renvoyer ObstacleException
        s il est hors champs, renvoyer HorsPlateauExceptoin"""
        estValide = True
        if s in self.listeObstacles:
            estValide = False
        if not self.environnement.plateau.estDansPlateau(s):
            estValide = False
        return estValide
            
    def renvoyerSuccesseur(self, s):
        t = self.calculerSuccesseur(s)
        if not self.validerSuccesseur(t):
            if t in self.listeObstacles:
                raise SuccesseurInvalideException("le successeur produit est invalide car se trouve dans la liste des obstacles:", repr(t))
            if not self.environnement.plateau.estDansPlateau(t):
                raise SuccesseurInvalideException("le successeur produit est invalide car se trouve hors limites:", repr(t))
        else:
            return t
    def calculerSuccesseur(self, s : 'Sommet.ClasseSommet') -> 'Sommet.ClasseSommet':
        raise NotImplementedError


class SuccesseurNord(Succ):
    def __init__(self, environnement):
        super().__init__(environnement)
        
    def calculerSuccesseur(self, s : 'Sommet.ClasseSommet') -> 'Sommet.ClasseSommet':
        t = copy.deepcopy(s)
        t.y = t.y + 1
        t.mettreAJourAntecedant(s)
        t.mettreAJourParcoursCumule(t.antecedant)
        t.mettreAJourDistanceArrivee(self.environnement.arrivee)
        t.mettreAJourClassement()
        return t
    
class SuccesseurSud(Succ):
    def __init__(self, environnement):
        Succ.__init__(self, environnement)
        
    def calculerSuccesseur(self, s : 'Sommet.ClasseSommet') -> 'Sommet.ClasseSommet':
        t = copy.deepcopy(s)
        t.y = t.y - 1
        t.mettreAJourAntecedant(s)
        t.mettreAJourParcoursCumule(t.antecedant)
        t.mettreAJourDistanceArrivee(self.environnement.arrivee)
        t.mettreAJourClassement()
        return t

    
class SuccesseurEst(Succ):
    def __init__(self, environnement):
        Succ.__init__(self, environnement)
        
    def calculerSuccesseur(self, s : 'Sommet.ClasseSommet') -> 'Sommet.ClasseSommet':
        t = copy.deepcopy(s)
        t.x = t.x + 1
        t.mettreAJourAntecedant(s)
        t.mettreAJourParcoursCumule(t.antecedant)
        t.mettreAJourDistanceArrivee(self.environnement.arrivee)
        t.mettreAJourClassement()
        return t

    
class SuccesseurOuest(Succ):
    def __init__(self, environnement):
        Succ.__init__(self, environnement)
        
    def calculerSuccesseur(self, s : 'Sommet.ClasseSommet') -> 'Sommet.ClasseSommet':
        t = copy.deepcopy(s)
        t.x = t.x - 1
        t.mettreAJourAntecedant(s)
        t.mettreAJourParcoursCumule(t.antecedant)
        t.mettreAJourDistanceArrivee(self.environnement.arrivee)
        t.mettreAJourClassement()
        return t


class Graphe:
    def __init__(self, environnement):
        try:
            self.listeObstacles = environnement.listeDesObstacles
            self.listeDesMethodesSucc = [SuccesseurNord(environnement),SuccesseurSud(environnement),
                                         SuccesseurEst(environnement),SuccesseurOuest(environnement)]
            self.listeDesSuccesseursDunSommet = []
        except AttributeError as ae:
            print(ae)
            traceback.print_exc()
            
    
    def calculerListeSuccesseurs(self,s: 'Sommet.ClasseSommet') -> 'Sommet.ClasseSommet':
        self.listeDesSuccesseursDunSommet = []
        for ObjMethode in self.listeDesMethodesSucc:
            try:
                t = ObjMethode.renvoyerSuccesseur(s)
                self.listeDesSuccesseursDunSommet.append(t)
            except SuccesseurInvalideException as SI:
                print("successeur invalide", SI)
        return self.listeDesSuccesseursDunSommet
    
    def filtrerSommetsVisites(self, listeSuccesseurs: 'List[Sommet.ClassSommet]', listeDeSommetsVisites:'List[Sommet.ClassSommet]') -> 'List[Sommet.ClassSommet]':
        listeResultante = copy.deepcopy(listeSuccesseurs)
        for un_sommet in listeResultante:
            if un_sommet in listeDeSommetsVisites:
                listeResultante.remove(un_sommet)
        return listeResultante
        
    
if __name__ == '__main__':      
    # validé pour la verif du type de environnement
    #env = "qdfqdsf"
    #g = Graphe(env)
    # generer un environnement:
    # 1. definir les dims du plateau
    plateau = Environnement.ClassePlateau(50,50)
    # 2. définir le nombre d obstacles
    nbObstacles = 200
    env = Environnement.ClasseEnvironnement(plateau, nbObstacles)
    # 3. générer les obstacles
    env.genererListeObstacles()
    #print(len(env.listeDesObstacles))
    # 4. tirer un sommet d arrivee
    env.genererArrivee()
    # 5. tirer un sommet de départ
    env.genererDepart()
    # validation ok:
    #print(env.depart.x)
    
    # 6. ajouter le necessaire pour que depart puisse etre ajoute dans la 
    # pile de priorite
    env.depart.initDepart(env.arrivee)
    # 7. marque le point d arrivee comme etant l arrivee (distance arrivee nulle)
    env.arrivee.initArrivee()
    # 8. creer une pilie de prio
    liste_priorite_noeuds_en_traitement = PileDePriorite.ClassePileDePriorite()
    env.pile = liste_priorite_noeuds_en_traitement
    # validation ok:
    #print(liste_priorite_noeuds_en_traitement)
    # 9. la liste de noeuds traités, une bete liste
    liste_de_noeuds_traites = []
    env.traite = liste_de_noeuds_traites
    
    
    ## le test:
    G = Graphe(env)
    print("depart",env.depart)
    liste = G.calculerListeSuccesseurs(env.depart)
    print(liste)
    print("depart pas modif normalement", env.depart)
