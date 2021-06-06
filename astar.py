# coding:utf-8
import copy
""" 'package' astar responsable de fournir la liste des élements traités, 
fournir les  antecedants, avec 
le parcours cumulé à chaque étape
ajouter des elements à la liste de priorite, 
"""

""" nécessite encore une étape de filtrage des éléments traités"""

class EchecReconstructionCheminOptimalException(Exception):
    """"liste vide alors qu on devrait etre arrivé à départ"""
    pass



def est_cas_arret_pas_de_chemin(liste_priorite_noeuds_en_traitement):
    verite = False
    if liste_priorite_noeuds_en_traitement.estVide():
        verite = True
    return verite

def est_cas_arret_arrivee_atteinte(noeud_en_traitement,arrivee):
    verite = False
    # l egalite a été modifiee sur la classe sommet
    # de manière à ce que le test n ait lieu que sur les coordonnées
    # ainsi les problemes de mise à jour des poids calculés n influencent
    # pas le test d égalité
    if (noeud_en_traitement == arrivee):
        verite = True
    return verite
        



def renvoyer_message_erreur_pas_de_chemin():
    print("pas de chemin de depart à arrivee")

def renvoyer_message_succes():
    print("chemin trouvé")
    
def ajouterEnTeteDeCheminSommetConsidere(s : 'Sommet.ClasseSommet', chemin_optimal: 'List[Sommet.ClasseSommet]') -> 'List[Sommet.ClasseSommet]':
    chemin = copy.deepcopy(chemin_optimal)
    chemin = [s] + chemin
    return chemin
    
def estCheminPlusCourtPassantParSommetNouvellementDecouvert(le_sommet, occurence_deja_presente_de_sommet_dans_liste_prio):
    return le_sommet.parcoursCumule < occurence_deja_presente_de_sommet_dans_liste_prio.parcoursCumule
    
    
def creer_chemin_optimal_depuis_liste_noeuds_traites(liste_noeuds_traites, arrivee: 'Classe.sommet', depart):
    """creer une liste premier entrant dernier sorti prenant reccursivement les antecedants de cahcun"""
    chemin_optimal = []
    try:
        noeud_considere = liste_noeuds_traites.depilerParCoordonnees(arrivee)
    except CoordExistePasException as existepas:
                raise EchecReconstructionCheminOptimalException("arrivee absent de liste_noeuds_traites alors que devrait exister par construction")
    
    
    while(True):
        chemin_optimal = ajouterEnTeteDeCheminSommetConsidere(noeud_considere, chemin_optimal)
        
        if noeud_considere == depart:
            #premier cas d arret: on est arrive au bout.
            break
        if liste_noeuds_traites.estVide():
            #deuxieme cas d arret: on a epuise tous les noeuds sans attendre le depart. c est anormal
            raise EchecReconstructionCheminOptimalException("liste_noeuds_traites vide alors qu on devrait etre arrivé à départ")
            
        else:
            #cas de la boucle: on continue:
            # on recupere les coordonnes du suivant à trouver dans la liste_noeuds_traites
            # en lisant les coordonnees de l antecedant stocke
            try:
                antecedant = noeud_considere.antecedant
                #trouver l antecendant dans la liste
                noeud_considere = liste_noeuds_traites.depilerParCoordonnees(antecedant)
                #le retirer de la liste
                #et l affecter comme ttant le nouveau noeud considere
            except CoordExistePasException as existepas:
                raise EchecReconstructionCheminOptimalException("antecedant existe pas dans liste_noeuds_traites alors que devrait exister par construction")
            
    return chemin_optimal

def ajouter_successeurs_si_nouveaux_ou_meilleur_chemin(noeud_en_traitement: 'Sommet.sommet', le_graphe : 'graphe.Graphe', liste_de_sommets_visites: 'List[Sommet.sommet]', liste_priorite_noeuds_en_traitement: 'List[Sommet.sommet]'):
    #1. récuperer la liste des successeurs d un noeud
    liste_des_successeurs = le_graphe.calculerListeSuccesseurs(noeud_en_traitement)
    #  il faut que la liste des successeurs ne comporte pas les noeuds presents 
    # dans la liste associativeDeSommetsVisites
    liste_des_successeurs = le_graphe.filtrerSommetsVisites(liste_des_successeurs,liste_de_sommets_visites)
    #2. ajouter le sommet dans la liste des sommets 
    # sans condition s'il n existe pas
    # seulement s il est un meilleur chemin s il existe déjà
    for le_sommet in liste_des_successeurs:
         
        if estSommetNouvellementDecouvertAbsentDeListePrioNoeudsEnTraitement(le_sommet, liste_priorite_noeuds_en_traitement):
            liste_priorite_noeuds_en_traitement.append(le_sommet)
        if not estSommetNouvellementDecouvertAbsentDeListePrioNoeudsEnTraitement(le_sommet, liste_priorite_noeuds_en_traitement):
            # reuperer l occurence deja presente
            occurence_deja_presente_de_sommet_dans_liste_prio = liste_priorite_noeuds_en_traitement.lireSommetParCoordonnees(le_sommet)
            # remplacer par nouvelle decouverte seulement si elle propose chemin plus court
            if estCheminPlusCourtPassantParSommetNouvellementDecouvert(le_sommet, occurence_deja_presente_de_sommet_dans_liste_prio):
                liste_priorite_noeuds_en_traitement.replacerPar(le_sommet)
            if not estCheminPlusCourtPassantParSommetNouvellementDecouvert(le_sommet, occurence_deja_presente_de_sommet_dans_liste_prio):
                pass
                #rien à faire dans ce cas, le meilleur chemin est déjà dans la liste prio
            
        
    
    


def il_reste_des_noeuds_en_traitement_et_arrivee_pas_atteinte( noeud_en_traitement, point_d_arrivee):
    return not est_cas_arret_arrivee_atteinte(noeud_en_traitement,point_d_arrivee)


def estSommetNouvellementDecouvertAbsentDeListePrioNoeudsEnTraitement(le_sommet, liste_priorite_noeuds_en_traitement : 'PileDePriorite.ClassePileDePriorite') -> bool:
    """necessite indexer PileDePriorite en rajoutant une structure de dictionnaire
    pour ne pas avoir à parcourir la pileDePriorite"""
    return le_sommet not in liste_priorite_noeuds_en_traitement
    

def astar(le_graphe, point_de_depart, point_d_arrivee, liste_noeuds_traites, liste_priorite_noeuds_en_traitement):
    liste_priorite_noeuds_en_traitement.append(point_de_depart)
    liste_solutions = []
    while (True):
        if est_cas_arret_pas_de_chemin(liste_priorite_noeuds_en_traitement):
            renvoyer_message_erreur_pas_de_chemin()
            break
        
        if not est_cas_arret_pas_de_chemin(liste_priorite_noeuds_en_traitement):
            # debut branche 2
            noeud_en_traitement = liste_priorite_noeuds_en_traitement.depiler()
            liste_noeuds_traites.append(noeud_en_traitement)
            
            if est_cas_arret_arrivee_atteinte(noeud_en_traitement,point_d_arrivee):
                
                renvoyer_message_succes()
                liste_solutions = creer_chemin_optimal_depuis_liste_noeuds_traites(liste_noeuds_traites)
                break
                
            if il_reste_des_noeuds_en_traitement_et_arrivee_pas_atteinte( noeud_en_traitement, point_d_arrivee):
                #ajouter les successeurs à la liste de prio seulemment
                # s ils sont nouveaux
                # ou s ils representent un meilleur chemin
                ajouter_successeurs_si_nouveaux_ou_meilleur_chemin(noeud_en_traitement,le_graphe,liste_noeuds_traites, liste_priorite_noeuds_en_traitement)
                
            
    return liste_solutions

def verif_effets_de_bord_liste(liste: 'List'):
    liste.append("a")

if __name__ == '__main__':
    #verification des effets de bords sur une liste
    liste = []
    verif_effets_de_bord_liste(liste)
    print(len(liste) == 1)
