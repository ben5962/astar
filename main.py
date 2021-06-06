# coding: utf-8
import Sommet
import Environnement
import PileDePriorite
import ListeAssociativeDeSommetsVisites
import graphe
import astar
import pdb
""" main est responsable de 
lancer l initialisation de depart (la taille du plateau et le nb obstacles est à parametrer ici,
le reste est une serie d appels sytematiques qui pourraient etre enfermes dans une methode)
 - initialise la liste de noeuds_traités
 to continue

"""

def main():
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
    #pdb.set_trace()
    # 5. tirer un sommet de départ
    env.genererDepart()
    
    
    # validation ok:
    #print(env.depart.x)
    
    # 6. ajouter le necessaire pour que depart puisse etre ajoute dans la 
    # pile de priorite
    env.depart.initDepart(env.arrivee)
    env.depart.mettreAJourClassement()
    
    # 7. marque le point d arrivee comme etant l arrivee (distance arrivee nulle)
    env.arrivee.initArrivee()
    print(dir(env.depart))
    # 8. creer une pilie de prio
    liste_priorite_noeuds_en_traitement = PileDePriorite.ClassePileDePriorite()
    env.pile = liste_priorite_noeuds_en_traitement
    # validation ok:
    #print(liste_priorite_noeuds_en_traitement)
    # 9. la liste de noeuds traités, une bete liste
    liste_de_noeuds_traites = ListeAssociativeDeSommetsVisites.ListeAssociativeDeSommets()
    env.traite = liste_de_noeuds_traites
    
    # 10. il nous faut une structure qui represente le graphe en fournissant les voisins 
    # d un noeud donné
    G = graphe.Graphe(env)
    resultat = astar.astar(G, env.depart, env.arrivee, liste_de_noeuds_traites, liste_priorite_noeuds_en_traitement)
if __name__ == '__main__':
    main()
    print(resultat)
