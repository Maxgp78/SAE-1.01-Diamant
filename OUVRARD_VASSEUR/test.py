############################################
###############Fonction test################
############################################

import random

cartes = [["Araignee",1],["Araignee",2],["Araignee",3],["Serpent",1],["Serpent",2],
["Serpent",3],["Lave",1],["Lave",2],["Lave",3],["Momie",1],["Momie",2],
["Momie",3],["Scorpion",1],["Scorpion",2],["Scorpion",3],["Rubis",1,1],["Rubis",2,1],
["Rubis",3,1],["Rubis",4,1], ["Rubis",5,1],["Rubis",5,2],["Rubis",7,1],["Rubis",7,2],
["Rubis",9,1],["Rubis",11,1],["Rubis",11,2],["Rubis",13,1],["Rubis",14,1],["Rubis",15,1],
["Rubis",17,1],["Relique",1],["Relique",2],["Relique",3],["Relique",4],["Relique",5]]

cartes_terrain = [["Araignee",1],["Araignee",2],["Araignee",3],["Serpent",1],["Serpent",2],
["Serpent",3],["Lave",1],["Lave",2],["Lave",3],["Momie",1],["Momie",2],
["Momie",3],["Scorpion",1],["Scorpion",2],["Scorpion",3],["Rubis",1,1],["Rubis",2,1],
["Rubis",3,1],["Rubis",4,1], ["Rubis",5,1],["Rubis",5,2],["Rubis",7,1],["Rubis",7,2]]


def gagnant(dico):
    max = -1
    victoire = None
    for nom in dico.keys():
        if dico[nom][1] > max:
            victoire = nom
            max = dico[nom][1]
    return victoire

def test_gagnant():
    '''
    Cette fonction permet de tester la fonction gagnant()
    '''
    assert gagnant({'Marcel':[0,45,0],'Michel':[0,12,0],'Fabrice':[0,150,0]}) == 'Fabrice'
    assert gagnant({'Marcel':[0,45,0],'Michel':[0,512,0],'Fabrice':[0,150,0]}) == 'Michel'
    assert gagnant({'Marcel':[0,170,0],'Michel':[0,12,0],'Fabrice':[0,150,0]}) == 'Marcel'

def tirer_cartes(carte):
    if carte in cartes_terrain and carte in cartes:
        return True
    return False
    return carte

def test_tirer_cartes():
    '''
    Cette fonction permet de tester une version simplifier de tirer_cartes()
    '''
    assert tirer_cartes(["Relique",1]) == False
    assert tirer_cartes(["Araignee",1]) == True
    assert tirer_cartes(["Batman",1]) == False

def test_fin_manche(deck):
    cpt=0
    for dangers in ["Lave","Scorpion","Araignee","Serpent","Momie"]:
    	cpt = 0
    	for i in range(len(deck)):
            if dangers == cartes_terrain[i][0]:
            	cpt += 1
    	if cpt > 1:
            return 0
    return 1

def test_test_fin_manche():
    '''
    Cette fonction teste l'idée principale de test_fin_manche()
    '''
    assert test_fin_manche([["Scorpion",2],["Scorpion",3],["Rubis",17,1],["Relique",5]]) == 0
    assert test_fin_manche([["Araignee",2],["Scorpion",3],["Rubis",17,1],["Relique",5]]) == 0

def points_relique(deck):
    compteur = 0
    for val in deck:
        if val[0] == "Relique":
            compteur += 1
    if compteur < 3:
        return 10
    else:
        return 5

def test_points_relique():
    '''
    Cette fonction teste la fonction points_relique()
    '''
    assert points_relique([["Relique",1],["Relique",2],["Relique",3],["Relique",4],["Relique",5]]) == 5
    assert points_relique([["Relique",1],["Relique",2],["Relique",3]]) == 5
    assert points_relique([["Relique",1],["Relique",2]]) == 10
    assert points_relique([["Relique",1]]) == 10

def ajouter_rubis(carte):
    rubis_plateau = 0
    if carte[0] == "Rubis":
        rubis_plateau += carte[1]
    return rubis_plateau

def test_ajouter_rubis():
    '''
    Cette fonction permet de tester la fonction ajouter_rubis()
    '''
    assert ajouter_rubis(["Rubis",15]) == 15
    assert ajouter_rubis(["Araignée",1]) == 0


test_gagnant()
test_tirer_cartes()
test_test_fin_manche()
test_points_relique()
test_ajouter_rubis()