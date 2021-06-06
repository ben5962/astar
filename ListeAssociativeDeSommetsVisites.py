# coding:utf-8
import Sommet

"""responsable dé gérer la liste des sommets visités:
 - depile un sommet en fournissant un sommet de memes coordonnees en parametre comme "clef"
     -> refuse de depiler un sommet absent. lance une exception CoordExistePasException 
 - autorise ajout de sommets : cree une entree dans le dictionnaire avec pour clef les coordonnees du sommet passé en parma
    -> refuse l ajout de sommets dont la clef existe déjà. lance une CoordExisteDejaException"""

class CoordExisteDejaException(Exception):
    """lancee qd tentative d insertion d un sommet dont la clef existe deja comme clef dans le dico"""
    pass
    
class CoordExistePasException(Exception):
    """lancee qd tentative d extraction d un sommet dont la clef n existe pas"""
    pass
    
class ListeAssociativeDeSommets:
    def __init__(self):
        self.dicoSommetParClefsCoordonnees = dict()
    def append(self, sommet : 'Sommet.ClasseSommet') -> 'Sommet.ClasseSommet':
        clef = (sommet.x, sommet.y)
        if clef in self.dicoSommetParClefsCoordonnees.keys():
            raise CoordExisteDejaException("la clef existe deja, donc pas d ajout ds le dico", repr(sommet))
        if clef not in self.dicoSommetParClefsCoordonnees.keys():
            self.dicoSommetParClefsCoordonnees[clef] = sommet
    def depilerParCoordonnees(self, sommet : 'Sommet.ClasseSommet') -> 'Sommet.ClasseSommet':
        clef = (sommet.x, sommet.y)
        if clef in self.dicoSommetParClefsCoordonnees.keys():
            resultat = self.dicoSommetParClefsCoordonnees.pop(clef)
        else:
            raise CoordExistePasException("tentative d extraction d une valeur dont la clef n existe pas dans le dico", repr(sommet))
        return resultat
    def __contains__(self, sommetCommeclef):
        clef = (sommetCommeclef.x, sommetCommeclef.y)
        return clef in self.dicoSommetParClefsCoordonnees.keys()
    def estVide(self):
        return len(self.dicoSommetParClefsCoordonnees.keys()) == 0
    
    
if __name__ == '__main__':
    un_sommet = Sommet.ClasseSommet(0,0)
    un_autre_sommet = Sommet.ClasseSommet(1,1)
    liste = ListeAssociativeDeSommets()
    liste.append(un_sommet)
    liste.append(un_autre_sommet)
    print(liste.depilerParCoordonnees(un_sommet))
    print(liste.depilerParCoordonnees(un_sommet))
