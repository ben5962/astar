# coding: utf-8
""" 'package' alea resp de fournir des entiers aléatoires positifs selon demande parametree"""
import random

def entier_aleatoire_dans_intervalle(debut_intervalle, fin_intervalle):
    # init gene nb alea
    random.seed(a=None, version=2)
    entier_aleatoire = random.randint(debut_intervalle, fin_intervalle)
    return entier_aleatoire




if __name__ == "__main__":
    #validé
    for i in range(0, 10):
        print("entier de 1 à 10: " + str(entier_aleatoire_dans_intervalle(1,10)))
              
