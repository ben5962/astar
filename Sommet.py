# coding: utf-8
import math
import traceback
import pdb


""" sommet est responsablede representer un sommmet 
    - au depart restreint a ses coordonees sur l espace metrique (sert d identifiant et de coord)
    - puis peuvent etre ajoutes  
         distanceArrivee
         par mettreAJourDistanceArrivee(), necessite de connaitre arrivee
        # - parcoursCumule
        par mettreAJourParcoursCumule(antecedant), nécessaite de connaitre antecedant
        
        # - classement
        necessite d avoir calcule distanceParcourue et distanceArrivee donc de connaitre
        antecedant et arrivee
        # - antecedant
        par mettreAJourAntecedant(sommet) necessite de connaitre antecedant 
        
    - marquer le depart comme etant un depart (pas d antecedant, distance parcourue nulle)
    - marquer l arrivee comme etant un point d arrivee (distanceRestante nulle)
    
        """

# j ajoute au fur et à mesure les proprietes necessaires au calcul
# je prends donc la précaution de verifier leur présence avant de les utiliser



class ClasseSommet:
    def __init__(self, x, y, **kwargs):
        self.x = x
        self.y = y
        # seront ajoutés lorsque besoin:
        # - distanceArrivee
        # - parcoursCumule
        # - classement
        # - antecedant
        for clef, valeur in kwargs.items():
            setattr(self,clef, valeur)
        
    

   
        
    
    def __eq__(self,other):
        #permet d utiliser in <list> par coordonnees avec les autres valeurs pas egales
        return other.x == self.x and other.y == self.y
    
    def mettreAJourDistanceArrivee(self, arrivee: 'ClasseSommet'):
        self.distanceArrivee = self.calculerDistanceArrivee(arrivee)
    
    def calculerDistanceArrivee(self, arrivee: 'ClasseSommet'):
        return self.calculerDistanceEuclidienneArrivee(arrivee)
    
    def calculerDistanceEuclidienneArrivee(self, arrivee : 'ClasseSommet') -> float:
        """pytha : rac_carree( carre(diff abscisses) + carre(diff ordonnees) """
        """verifier si on est dans les bonnes conditions pour calculer:
                - verifier qu on a bien les champs x et y dans arrivee... pas de pb.
                - verifier qu on a bien les champs distanceArrivee. sera
                verifie seulement avec ecrireArrivee"""
        resultat = float(0)
        try: 
            abscisse_arrivee = arrivee.x
            ordonnee_arrivee = arrivee.y
            abscisse_point_considere = self.x
            ordonnee_point_considere = self.y
            diff_abscisses = abscisse_arrivee - abscisse_point_considere
            diff_ordonnees = ordonnee_arrivee - ordonnee_point_considere
            carre_diff_abscisses = math.pow(diff_abscisses, 2)
            carre_diff_ordonnees = math.pow(diff_ordonnees, 2)
            somme_carres_diff = carre_diff_abscisses + carre_diff_ordonnees
            resultat = math.sqrt(somme_carres_diff)
            
        except AttributeError as attError:
            print(attError)
            traceback.print_exc()
            
        return resultat
    
    def calculerDistance(self, aQuelSommet: 'ClasseSommet'):
        return self.calculerDistanceArrivee(aQuelSommet)
    
    def calculerParcoursCumule(self,antecedant : 'ClasseSommet'):
        """dans cette representation ,tous les arcs ont le meme poids
        donc parcoursCulume + 1 ou 0 si antecedant vaut None:
        pas besoin d aller lire les poids des differents arcs dans le graphe"""
        resultat = float(0)
        if antecedant is not None:
            resultat = antecedant.parcoursCumule + self.calculerDistance(antecedant)
        return resultat
            
    def mettreAJourParcoursCumule(self, antecedant: 'ClasseSommet'):
        self.parcoursCumule = self.calculerParcoursCumule(antecedant)
            
    def calculerClassement(self):
        try:
            poids = self.parcoursCumule
            cout = self.distanceArrivee
            classement = cout + poids
        except AttributeError as attError:
            print("dans l objet" , self)
            print(attError)
            traceback.print_exc()
        return classement
    
    def mettreAJourClassement(self):
        self.classement = self.calculerClassement()
    
    def mettreAJourAntecedant(self, antecedant : 'ClasseSommet'):
        self.antecedant = antecedant
    
    def initDepart(self,arrivee : 'ClasseSommet'):
        #self.estDepart = True
        self.mettreAJourAntecedant(None)
        self.mettreAJourParcoursCumule(None)
        self.mettreAJourDistanceArrivee(arrivee)
        self.mettreAJourClassement()
        assert(self.antecedant is None)
        assert(self.parcoursCumule == 0)
        assert(self.classement == self.distanceArrivee)
        
        
        
    def initArrivee(self):
        self.mettreAJourDistanceArrivee(self)
    
    def __repr__(self):
        representation = 'ObjetClasseSommet['
        try:
            representation += 'ESTDEPART:' + str(self.estDepart)
            
        except AttributeError:
            pass
        representation += 'x:' + str(self.x) +',y:'+str(self.y)
        try:
            representation += ',classement :' + str(self.classement)
        except AttributeError:
            pass
        try:
            representation += ',parcoursCumule:' + str(self.parcoursCumule)
        except AttributeError:
            pass
        try:
            representation += ',distanceArrivee:' + str(self.distanceArrivee)
            
        except AttributeError:
            pass
        finally:
            representation += ']'
            return repr(representation)
    
        


if __name__ == '__main__':
    
    # le test d ini du depart
    u = ClasseSommet(10,10)
    arrivee = ClasseSommet(10,5)
    u.initDepart(arrivee=arrivee)
    arrivee.initArrivee()
    print("parcours cumule vaut 0 au depart", u.parcoursCumule == 0)
    print(u)
    print("distance a l arrivee vaut 0 a l arrivee",arrivee.distanceArrivee == 0)
    print(arrivee)
    # le test d egalite
    # essai d ajout de parametres additionnels si le besoin s en fait sentir)
    s = ClasseSommet(4,5, classement="qfqsdfqs", alpha=30, untruc=None)
    # creation d un sommmet de memes coordonnes pour test d egalité par coordonnees
    t = ClasseSommet(4,5)
    liste = []
    liste.append(s)
    liste.append(t)
    print(s)
    print( s == t )
    print(s in liste)
    
    
    
    #s.calculerDistanceEuclidienneArrivee(arrivee)
    s.mettreAJourDistanceArrivee(arrivee)
    print(s)
    print(s.distanceArrivee)
    #s.calculerParcoursCumule(None)
    s.mettreAJourParcoursCumule(None)
    #print(s.calculerClassement())
    s.mettreAJourClassement()
    print(s.classement)
