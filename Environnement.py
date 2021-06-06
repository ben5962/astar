# coding:utf-8
import typing
import traceback
import alea
import Sommet


"""'package' environnement responsable de stocker les variables d environnement : 
taile du plateau, nbObstacles, listes des obstacles, arrivee, depart,
de générer l arrivee, de générer le départ, en vue de 
- fournir un modele de données qui pourra facliement etre passé à une fonction d affichage
- fournir un modele de donnéées qui pourra etre passe en parametre d entree à astar"""

listeDesObstacles: typing.List[Sommet.ClasseSommet]


class HorsPlateauException(Exception):
    """lancee lorsque l on sort du plateau"""
    pass

class ClassePlateau:
    def __init__(self, xmax, ymax):
        self.xmax = xmax
        self.ymax = ymax
        
    def estDansPlateau(self, sommet : Sommet.ClasseSommet):
        return sommet.x > 0 and sommet.x <= self.xmax and sommet.y > 0 and sommet.y <= self.ymax 

class ClasseEnvironnement:
    def __init__(self, plateau, nbObstacles):
        self.plateau = plateau
        self.nbObstacles = nbObstacles
        self.listeDesObstacles = []
        self.arrivee = None
        self.depart = None
    def genererListeObstacles(self):
        compteur = 1
        while(True):
            if compteur == self.nbObstacles:
                break
            compteur += 1
            abscisse = self.plateau.xmax + 1
            ordonnee = self.plateau.ymax + 1
            sommetTire = Sommet.ClasseSommet(abscisse, ordonnee)
            while(True):
                if not sommetTire in self.listeDesObstacles:
                    if self.plateau.estDansPlateau(sommetTire):
                        break
                    
                    
                abscisse = alea.entier_aleatoire_dans_intervalle(0,self.plateau.xmax)
                ordonnee = alea.entier_aleatoire_dans_intervalle(0,self.plateau.ymax)
                sommetTire = Sommet.ClasseSommet(abscisse, ordonnee)
            self.listeDesObstacles.append(sommetTire)
            
    def genererArrivee(self):
        abscisse = self.plateau.xmax + 1
        ordonnee = self.plateau.ymax + 1
        sommetTire = Sommet.ClasseSommet(abscisse, ordonnee)
        while(True):
            if not sommetTire in self.listeDesObstacles:
                if self.plateau.estDansPlateau(sommetTire):
                    break
            abscisse = alea.entier_aleatoire_dans_intervalle(0,self.plateau.xmax)
            ordonnee = alea.entier_aleatoire_dans_intervalle(0,self.plateau.ymax)
            sommetTire = Sommet.ClasseSommet(abscisse, ordonnee)
            
        self.arrivee = sommetTire
        
    def genererDepart(self):
        abscisse = self.plateau.xmax + 1
        ordonnee = self.plateau.ymax + 1
        sommetTire = Sommet.ClasseSommet(abscisse, ordonnee)
        while(True):
            if not sommetTire in self.listeDesObstacles:
                if not sommetTire == self.arrivee:
                    if self.plateau.estDansPlateau(sommetTire):
                        break
            abscisse = alea.entier_aleatoire_dans_intervalle(0,self.plateau.xmax)
            ordonnee = alea.entier_aleatoire_dans_intervalle(0,self.plateau.ymax)
            sommetTire = Sommet.ClasseSommet(abscisse, ordonnee)
            
        self.depart = sommetTire
        
    def filtrerSommetsVisites(self, listeSuccesseurs: 'List[Sommet.ClassSommet]') -> 'List[Sommet.ClassSommet]':
        listeResultante = copy.deepcopy(listeSuccesseurs)
        for un_sommet in listeResultante:
            if un_sommet in listeDeSommetsVisites:
                listeResultante.pop(un_sommet)
        return listeResultante
            
                    
