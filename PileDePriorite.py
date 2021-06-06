# coding: utf-8


"""la pile de priorite est responsable de 
  - n accepter l ajout de  sommets que s'ils possedent un champ clasement 
  (pas de gestion du classement "sale"  : modif du classement dans la pile de prio)
  - classer les sommets inseres par ordre de classement croissant
  - accepter de depiler le premier du classement
  - donner sa taille de pile (__len__) pour test pile_vide
  """
  
""" bonus : repr pour faire quelques essais avec print
     - un iterateur sur la pile de prio nécessaire pour avoir le test de presence in
     pour pouvoir ecrire __contains__ pour quelques essais avec print
     """
import Sommet
import copy
class ElemSansClassementException(Exception):
    """la lancer quand on essaie d ajouter un elem qui n a pas la ppte classement"""
    pass

class PileVideException(Exception):
    """la lancer quand la pile est vide"""
    pass

class ElemAbsentDelaPileDePrioException(Exception):
    """ la lancer quand l element demande est absent de la pile de prio"""
    pass

class ClassePileDePrioriteIterator:
    """ fabrication d un interateur pour la classe PileDePriorie"""
    def __init__(self, pile):
        self.pile = pile
        self._index = 0
        
    def __next__(self):
        if self._index < len(self.pile.listeDeSommets):
            result = self.pile.listeDeSommets[self._index]
            self._index += 1
            return result
        if self._index == len(self.pile.listeDeSommets):
            raise StopIteration



class ClassePileDePriorite:
    pass
    #isEmpty()
    #pop() -> first elem
    #append(elem) 
    #  (appelle _sort()
    #  verifie existence de classement dans elem sinon ElemSansClassementException
    #_sort()
    # in... abc.container
    def __init__(self):
        self.listeDeSommets = []
        
    
    def append(self,elem :'ClasseSommet'):
        try:
            classement = elem.classement
            self.listeDeSommets.append(elem)
            # trier par distance à l arrivee fera préferer l arrivee aux autres elem en cas
            # d egalite sur la fonction de classement
            self.listeDeSommets = sorted(self.listeDeSommets, key=lambda s: (s.classement, s.distanceArrivee))
        except AttributeError as a:
            raise ElemSansClassementException("lors de la tentative d ajout de l element:", elem, "pas d attribut classement")
        
    def __contains__(self, elem):
        return any(elem == e for e in self.listeDeSommets)
    
    def __repr__(self):
        representation = 'ObjetPilePrio['
        for sommet in self:
            representation += ',' + repr(sommet)
        representation += ']'
        return repr(representation)
    
    def __iter__(self):
        return ClassePileDePrioriteIterator(self)
    
    def __len__(self):
        return len(self.listeDeSommets)
    
    def depiler(self) ->'ClasseSommet' :
        if len(self.listeDeSommets) == 0:
            raise PileVideException("la pile est vide")
            
        if len(self.listeDeSommets) != 0:
            aRenvoyer = self.listeDeSommets[0]
            self.listeDeSommets = self.listeDeSommets[1:]
            return aRenvoyer
    def lireSommetParCoordonnees(self, sommetPorteurDeCoordonnees: 'Sommet.ClasseSommet'):
        """ 1 recupere l index du sommet ayant les memes coordonnees que celles pasees en paarm
        renvoie ElemAbsentDelaPileDePrioException si pas de telles coordonnees dans la pile
        2. une fois l index récuperé renvoie la valeur demandee
        """
        estTrouve = False
        for elem in self:
            if elem == sommetPorteurDeCoordonnees:
                estTrouve = True
                break
        if not estTrouve:
            raise ElemAbsentDelaPileDePrioException("l element suivant n a pas été trouvé par coordonnées dans le dico : ", sommetPorteurDeCoordonnees)
        if estTrouve:
            return elem
    
    def remplacerSommetParCoordonnees(self, sommetRemplacant: 'Sommet.ClasseSommet'):
        """1 recuperer l index..... 
        renvoie ElementAbsentDeLapileDePrioException si pas ces coordonnees dans la pile
        2 une fois l index récupéré, remplacer = supprimer + ajouter...."""
        estTrouve = False
        for elem in self:
            if elem == sommetRemplacant:
                estTrouve = True
                break
        if not estTrouve:
            raise ElemAbsentDelaPileDePrioException("l element suivant n a pas été trouvé par coordonnées dans le dico : ", sommetRemplacant)
        if estTrouve:
            # est ce que remove existe pour une liste?
            
            self.listeDeSommets.remove(elem)
            self.append(sommetRemplacant)
        
        
if __name__ == '__main__':
    pile = ClassePileDePriorite()
    d = Sommet.ClasseSommet(0,0)
    a = Sommet.ClasseSommet(10,10)
    premiere_case = Sommet.ClasseSommet(0,1)
    sommetEloigne = Sommet.ClasseSommet(100,100)
    print(sommetEloigne)
    #print(dir(sommetEloigne))
    sommetEloigne.mettreAJourDistanceArrivee(a) 
    sommetEloigne.parcoursCumule = 200
    sommetEloigne.mettreAJourClassement()
    d.initDepart(a)
    print(d)
    a.initArrivee()
    a.parcoursCumule = 100
    a.mettreAJourClassement()
    d.mettreAJourClassement()
    print(d)
    pile.append(d)
    pile.append(sommetEloigne)
    pile.append(a)
    print(len(pile))
    print("implementation appartemanance", d in pile)
    print(pile)
    premier = pile.depiler()
    print(repr(premier))
    print(pile)
    print(len(pile))
    
    
    un_sommet_similaire_a_sommetEloigne_mais_avec_valeur_parcours_different = Sommet.ClasseSommet(100,100)
    un_sommet_similaire_a_sommetEloigne_mais_avec_valeur_parcours_different.mettreAJourDistanceArrivee(a)
    sommetEloigne.parcoursCumule = 200
    un_sommet_similaire_a_sommetEloigne_mais_avec_valeur_parcours_different.parcoursCumule = 50
    un_sommet_similaire_a_sommetEloigne_mais_avec_valeur_parcours_different.antecedant = Sommet.ClasseSommet(99,100)
    un_sommet_similaire_a_sommetEloigne_mais_avec_valeur_parcours_different.mettreAJourClassement()
    print(un_sommet_similaire_a_sommetEloigne_mais_avec_valeur_parcours_different in pile)
    print(pile.lireSommetsParCoordonnees(un_sommet_similaire_a_sommetEloigne_mais_avec_valeur_parcours_different))
    #pile.lireSommetsParCoordonnees(un_sommet)
    sommet_remplacant = copy.deepcopy(sommetEloigne)
    sommet_remplacant.parcoursCumule=1000
    sommet_remplacant.distanceArrivee=1000
    sommet_remplacant.classement = 1000
    # je prends conscience qu il va falloir recalcluler le classement lors du remplacment
    pile.remplacerSommetParCoordonnees(sommet_remplacant)
    print(pile)
