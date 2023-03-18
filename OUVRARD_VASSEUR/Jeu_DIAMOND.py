import random
import time
from tkiteasy import *

#Il s'agit ici de la liste contenant toutes les cartes du paquet, chaque carte
#possède son nom, son identifiant et leur valeur (pour les rubis)
cartes = [["Araignee",1],["Araignee",2],["Araignee",3],["Serpent",1],["Serpent",2],
["Serpent",3],["Lave",1],["Lave",2],["Lave",3],["Momie",1],["Momie",2],
["Momie",3],["Scorpion",1],["Scorpion",2],["Scorpion",3],["Rubis",1,1],["Rubis",2,1],
["Rubis",3,1],["Rubis",4,1], ["Rubis",5,1],["Rubis",5,2],["Rubis",7,1],["Rubis",7,2],
["Rubis",9,1],["Rubis",11,1],["Rubis",11,2],["Rubis",13,1],["Rubis",14,1],["Rubis",15,1],
["Rubis",17,1],["Relique",1],["Relique",2],["Relique",3],["Relique",4],["Relique",5]]
#Cette liste va posséder toutes les cartes qui sont tirées sur une manche
cartes_terrain = []
#Ce dictionnaire possède en clé le nom du joueur
#et en valeur [rubis_potentiel,coffre,état(fuite ou poursuivre)]
joueur = {}
#Cette liste possède tout les joueurs qui sont encore dans l'expedition
joueur_actif = []
#Cette liste possède tout les joueurs qui ne sont plus dans l'expedition
joueur_sortant = []
rubis_plateau = 0
reste_plateau = 0
relique_en_jeu = False
g_en_jeu=[[],[],[],[]]
HAUTEUR,LARGEUR=1920,1000
g = None
objet = None
nb_manches = 1

###################################################
###############Fonctions graphiques################
###################################################

def g_update():
    '''
    Cette fonction s'assure que les différents compteurs de rubis
    dans la partie soient graphiquement mis à jour.
    --------------------------------------------------------------
    Entrée: aucune
    Sortie: id d'un objet graphique
    '''
    global g
    global reste_plateau
    global objet
    for chaque in joueur.keys():            # Pour chaque joueur de la partie, afficher le contenu de son coffre et son nombre de rubis.
        g.changerTexte(joueur[chaque][6],str(joueur[chaque][0])+'\n'+str(joueur[chaque][1]))
    if objet!= None:
        g.supprimer(objet)
    return g.afficherTexte('Rubis restant :\n          '+str(reste_plateau),1400,875,'white')       # Renvoie l'id du texte affichant les rubis restant.


def path(image,transparence=False):
    '''
    Cette fonction extrait le chemin d'appel des images utilisées
    dans le jeu.
    --------------------------------------------------------------
    Entrée: str, bool(facultatif)
    Sortie: aucune
    '''
    if transparence==True:
        return 'Images/Modele_test/'+image+'.png'       # Chemin des images .png
    else:
        return 'Images/Modele_test/'+image+'.jpg'       # Chemin des images .jpg
    return


def g_reset():
    '''
    Cette fonction assure le nettoyage de la fenêtre entre chaque
    manche du jeu. Elle efface les objets graphiques superflus.
    --------------------------------------------------------------
    Entrée: aucune
    Sortie: aucune
    '''
    global g_en_jeu
    global g
    for ligne in g_en_jeu:      # Effacement des cartes sur le plateau
        for chaque in ligne:
            g.supprimer(chaque)
    for j in joueur.keys():     # Effacement des indicateurs de fuite des joueurs
        if len(joueur[j])>7:
            g.supprimer(joueur[j].pop())
    g.actualiser()
    g_en_jeu=[[],[],[],[]]      # Mise à 0 de du tableau d'affichage des cartes
    return

def g_joueur():
    '''
    Cette fonction affiche les cartes joueurs dans les emplacements adaptés
    et initialise graphiquement leurs coffre/rubis.
    --------------------------------------------------------------
    Entrée: aucune
    Sortie: aucune
    '''
    global g
    coo1,coo2=25,55
    for chaque in joueur:
        joueur[chaque].append((coo1,coo2))          # Stockage des coordonées d'apparition des élements graphiques
        joueur[chaque].append(g.afficherImage(coo1,coo2,path('carte_joueur',True)))         # Stockage de l'objet graphique : carte_joueur
        joueur[chaque].append(g.afficherTexte(chaque,coo1+100,coo2+25,'white'))     # Stockage de l'objet graphique du nom du joueur
        g.afficherTexte('Rubis :\nCoffre:',coo1+50,coo2+150,'lightgray')
        joueur[chaque].append(g.afficherTexte(str(joueur[chaque][0])+'\n'+str(joueur[chaque][1]),coo1+150,coo2+150,'white'))
        if coo1==25 and coo2==730:
            coo1,coo2=1695,55
        else:
            coo2+=225
    return


def g_carte(carte,liste,nb):
    '''
    Cette fonction détermine l'image à afficher pour chaque
    carte sorti sur le plateau.
    --------------------------------------------------------------
    Entrée: liste, liste, int
    Sortie: aucune
    '''
    global g
    if nb==3 and liste==[]:
        liste+=[None,None]
    if carte[0]=='Araignee':
        liste.append(g.afficherImage(len(liste)*215+322,nb*175+292,path('carte_araignee',True)))
    elif carte[0]=='Momie':
        liste.append(g.afficherImage(len(liste)*215+322,nb*175+292,path('carte_momie',True)))
    elif carte[0]=='Lave':
        liste.append(g.afficherImage(len(liste)*215+322,nb*175+292,path('carte_lave',True)))
    elif carte[0]=='Scorpion':
        liste.append(g.afficherImage(len(liste)*215+322,nb*175+292,path('carte_scorpion',True)))
    elif carte[0]=='Serpent':
        liste.append(g.afficherImage(len(liste)*215+322,nb*175+292,path('carte_serpent',True)))

    elif carte[0]=='Rubis':
        if carte[1]==1:
            liste.append(g.afficherImage(len(liste)*215+322,nb*175+292,path('rubis_1',True)))

        elif carte[1]==2:
            liste.append(g.afficherImage(len(liste)*215+322,nb*175+292,path('rubis_2',True)))

        elif carte[1]==3:
            liste.append(g.afficherImage(len(liste)*215+322,nb*175+292,path('rubis_3',True)))

        elif carte[1]==4:
            liste.append(g.afficherImage(len(liste)*215+322,nb*175+292,path('rubis_4',True)))

        elif carte[1]==5:
            liste.append(g.afficherImage(len(liste)*215+322,nb*175+292,path('rubis_5',True)))

        elif carte[1]==7:
            liste.append(g.afficherImage(len(liste)*215+322,nb*175+292,path('rubis_7',True)))

        elif carte[1]==9:
            liste.append(g.afficherImage(len(liste)*215+322,nb*175+292,path('rubis_9',True)))

        elif carte[1]==11:
            liste.append(g.afficherImage(len(liste)*215+322,nb*175+292,path('rubis_11',True)))

        elif carte[1]==13:
            liste.append(g.afficherImage(len(liste)*215+322,nb*175+292,path('rubis_13',True)))

        elif carte[1]==14:
            liste.append(g.afficherImage(len(liste)*215+322,nb*175+292,path('rubis_14',True)))

        elif carte[1]==15:
            liste.append(g.afficherImage(len(liste)*215+322,nb*175+292,path('rubis_15',True)))

        elif carte[1]==17:
            liste.append(g.afficherImage(len(liste)*215+322,nb*175+292,path('rubis_17',True)))
    return



def g_test_carte(carte):
    '''
    Cette fonction determine les emplacements adaptés auquels
    les différentes cartes doivent être positionnés.
    --------------------------------------------------------------
    Entrée: liste
    Sortie: aucune
    '''
    global g
    if carte[0]=='Relique':     # Affichage d'une relique
        g.afficherImage(429,817,path('carte_relique',True))
    else:               # Placement de la carte dans le tableau d'apparition
        if len(g_en_jeu[0])==6:
            if len(g_en_jeu[1])==6:
                if len(g_en_jeu[2])==6:
                    return g_carte(carte,g_en_jeu[3],3)
                return g_carte(carte,g_en_jeu[2],2)
            return g_carte(carte,g_en_jeu[1],1)
        return g_carte(carte,g_en_jeu[0],0)
    return


def g_prendre_relique():
    '''
    Cette fonction replace le dos de carte sur la carte relique
    une fois qu'elle n'est plus disponible.
    --------------------------------------------------------------
    Entrée: aucune
    Sortie: aucune
    '''
    global g
    g.afficherImage(429,817,path('dos_de_carte',True))
    return


def g_base():
    '''
    Cette fonction affiche les élements de base sur la fenêtre graphique
    et génère cette dernière.
    --------------------------------------------------------------
    Entrée: aucune
    Sortie: aucune
    '''
    global g
    g = ouvrirFenetre(HAUTEUR,LARGEUR)      # Génération de la fenêtre
    g.afficherImage(0,0,path('fond_de_jeu'))
    g_joueur()          # Création graphique des joueurs
    return



def g_choix(j):
    '''
    Cette fonction affiche les boutons permettant aux joueurs de
    choisir leurs actions.
    --------------------------------------------------------------
    Entrée: liste
    Sortie: int
    '''
    global g
    xb1,yb1=480,75
    xb2,yb2=1240,75
    texte=g.afficherTexte("C'est au tour de "+str(j)+" !",960,150,'white',24)
    bouton1=g.afficherImage(xb1,yb1,path('bouton_poursuivre'));bouton2=g.afficherImage(xb2,yb2,path('bouton_fuite'))    # Affichage des boutons
    choix = None
    while choix==None:          # Boucle attendant des coordonnées valides
        click=g.attendreClic()
        if xb1<click.x<xb1+200 and yb1<click.y<yb1+200:
            choix = 1
        elif xb2<click.x<xb2+200 and yb2<click.y<yb2+200:
            choix = 0
    g.supprimer(bouton1);g.supprimer(bouton2);g.supprimer(texte)        # Effacement des boutons
    return choix            # Retour du choix du joueur

def g_victoire(prenom):
    '''
    Cette fonction affiche le nom du vainqueur en fin de partie.
    --------------------------------------------------------------
    Entrée: str
    Sortie: aucune
    '''
    g.afficherTexte(str(prenom)+" l'emporte avec "+str(joueur[prenom][1])+" rubis !",960,150,'white',24)
    g.actualiser()
    sleep(10)
    return

def g_perte():
    '''
    Cette fonction alerte les joueurs ayant perdus leurs rubis suite
    à l'apparition d'un danger.
    --------------------------------------------------------------
    Entrée: aucune
    Sortie: aucune
    '''
    nom=""
    for j in joueur_actif:
        nom+=j+", "
    perte = g.afficherTexte("Vous avez encore rencontré un/une "+str(cartes_terrain[-1][0])+" !\n "+nom+"vous perdez tout vos rubis...",960,150,'white',24)        # Message d'alerte
    g.actualiser()
    sleep(4)
    g.supprimer(perte)          # Effacement du message
    return

def g_manche():
    '''
    Cette fonction affiche le numéro de la manche au début de
    cette dernière.
    --------------------------------------------------------------
    Entrée: aucune
    Sortie: aucune
    '''
    global nb_manches
    changement = g.afficherTexte("Début de la MANCHE "+str(nb_manches)+" !",960,150,'white',24)
    g.actualiser()
    sleep(5)
    g.supprimer(changement)
    return

def g_fuite(prenom):
    '''
    Cette fonction affiche un indicateur de fuite sur la carte des
    joueurs ayant stoppé leur progression.
    --------------------------------------------------------------
    Entrée: str
    Sortie: aucune
    '''
    joueur[prenom].append(g.afficherImage(joueur[prenom][3][0]+50,joueur[prenom][3][1]+40,path('indication_fuite',True)))


def g_apparition(carte):
    '''
    Cette fonction affiche un message d'alerte suite à l'apparition
    d'une nouvelle carte pour tenir au courant les joueurs du déroulement
    de la partie.
    --------------------------------------------------------------
    Entrée: liste
    Sortie: aucune
    '''
    global joueur_actif
    if carte[0] == 'Rubis':         # Message associé aux rubis
        txt = g.afficherTexte("Vous trouvez une bourse de "+str(carte[1])+" rubis !\n                  +"+str(carte[1]//len(joueur_actif))+" chacun",960,150,'white',24)
        g.actualiser()
        sleep(2)
        g.supprimer(txt)
    elif carte[0]=='Relique':       # Messgae associé aux reliques
        txt = g.afficherTexte("Vous trouvez une relique !",960,150,'white',24)
        g.actualiser()
        sleep(2)
        g.supprimer(txt)
    else:                       # Message associé aux dangers
        txt = g.afficherTexte("Attention ! Vous êtes attaqué par un/une "+str(carte[0]),960,150,'white',24)
        g.actualiser()
        sleep(2)
        g.supprimer(txt)
    return

def g_classement():
    '''
    Cette fonction crée le classmeent final des joueurs en fonction
    de leurs rubis et affiche ce classement.
    --------------------------------------------------------------
    Entrée: aucune
    Sortie: aucune
    '''
    global joueur
    tri=[]
    for k,v in joueur.items():
        tri.append((k,v[1]))    # Cr&ation d'une liste des couples (joueurs,scores)
    for n in range(len(tri)):       # Tri des scores des joueurs
        cle=tri[n]
        comp=n-1
        while comp>=0 and tri[comp][1] > cle[1]:
            tri[comp+1]=tri[comp]
            comp=comp-1
        tri[comp+1]=cle
    for chaque in range(len(tri)):
        g.afficherTexte(str(tri[-1-chaque][0])+" : "+str(tri[-1-chaque][1])+" rubis",960,chaque*50+350,'white',24)      # Affichage décroissant des scores.
    g.actualiser()

###################################################
###############Fonctions pythons###################
###################################################

def nb_joueur():
    '''
    Cette fonction permet de rentrer le nombre de joueur qu'il
    y aura dans la partie.
    Elle est est appelée par nom_joueur().
    ----------------------------------------------------------
    Entrée: aucune
    Sortie: un int entre 3 et 8
    '''
    nombre_j = 0
    while nombre_j < 3 or nombre_j > 8:
        nombre_j = int(input("Rentrez le nombre de joueurs : "))
    return nombre_j

def nom_joueur():
    '''
    Cette fonction permet de rentrer le nom de chaque joueur et de
    le stocker dans un dictionnaire.
    Elle est appelée par la fonction principale.
    --------------------------------------------------------------
    Entrée: aucune
    Sortie: un dict
    '''
    players = nb_joueur()
    for i in range(players):
        texte = "Rentrez le nom du joueur " + str(i + 1) + " : "
        nom = str(input(texte))
        joueur[nom] = [0,0,1]
        joueur_actif.append(nom)
    return joueur

def continuer():
    '''
    Cette fonction permet de permet de sauvegarder le choix d'un
    joueur, si il souhaite poursuivre ou non l'expedition.
    Elle est appelée par la fonction principale.
    '''
    c_or_p = 2
    sortant = []
    for prenom in joueur_actif:
        while c_or_p != 0 and c_or_p != 1:
            c_or_p = g_choix(prenom)
            joueur[prenom][2] = c_or_p
            if joueur[prenom][2] == 0:
                sortant.append(prenom)
        c_or_p = 2
    for prenom in sortant:
        if prenom in joueur_actif:
            joueur_sortant.append(prenom)
            joueur_actif.remove(prenom)
    return

def ajouter_rubis(carte_actu):
    """
    Cette fonction permet d'ajouter la valeur d'une carte qui est
    apparue sur le plateau.
    Elle est appelée par la fonction principale.
    """
    global rubis_plateau
    if carte_actu[0] == "Rubis":
        rubis_plateau += carte_actu[1]
    return

def distribuer_rubis():
    '''
    Cette fonction permet de distribuer équitablement les rubis entre
    les joueurs qui sont encore en expédition.
    Elle est appelée par la fonction principale.
    '''
    global rubis_plateau
    global reste_plateau
    for j in joueur_actif:
        joueur[j][0] += rubis_plateau//len(joueur_actif)
    rubis_plateau -= (rubis_plateau//len(joueur_actif))*len(joueur_actif)
    reste_plateau += rubis_plateau
    rubis_plateau = 0
    return

def fuite():
    '''
    Cette fonction permet de valider les rubis obtenus lorsqu'un joueur
    fuit en influant sur les rubis qui sont en jeu. Elle permet aussi
    de récupérer une relique si le joueur fuit seul et qu'une relique
    est disponible.
    Elle est appelée par la fonction principale.
    '''
    global rubis_plateau
    global reste_plateau
    global relique_en_jeu
    for j in joueur_sortant:
        joueur[j][1] += joueur[j][0]
        joueur[j][0] = 0
        joueur[j][1] += rubis_plateau//len(joueur_sortant)
        joueur[j][1] += reste_plateau//len(joueur_sortant)
        reste_plateau -= reste_plateau//len(joueur_sortant)
        g_fuite(j)
    if joueur_sortant != []:
        rubis_plateau -= (rubis_plateau//len(joueur_sortant))*len(joueur_sortant)
    if len(joueur_sortant) == 1:
        for rel in cartes_terrain:
            if rel[0] == "Relique" and relique_en_jeu == False:
                points = points_relique()
                joueur[joueur_sortant[0]][1] += points
                cartes.remove(rel)
                g_prendre_relique()
                relique_en_jeu = True
    joueur_sortant.clear()
    return

def mort():
    '''
    Cette fonction permet de supprimer tout les rubis qui étaient
    en jeu lorsque deux dangers sont sortis et donc que le joueur
    n'a pas fuit à temps.
    Elle est appelée par la fonction principale.
    '''
    for j in joueur_actif:
        joueur[j][0] = 0
    return

def points_relique():
    """
    Cette fonction permet de calculer le nombre de points d'une
    relique en fonction de son nombre d'occurence dans la liste
    cartes. Elle est appelée par la fonction fuite().
    -----------------------------------------------------------
    Entrée: aucune
    Sortie: un int
    """
    compteur = 0
    for val in cartes:
        if val[0] == "Relique":
            compteur += 1
    if compteur < 3:
        return 10
    else:
        return 5


def test_fin_manche():
    """
    Cette fonction permet de savoir quand une partie est terminée,
    c'est-à-dire, si tout les joueurs ont quitté la partie ou si
    deux cartes dangers similaires sont sur le plateau ou bien
    si nous pouvons continuer la partie.
    Elle est appelée par la fonction principale.
    --------------------------------------------------------------
    Entrée: aucune
    Sortie: un int
    """
    cpt=0
    if joueur_actif==[]:
        return 2
    for dangers in ["Lave","Scorpion","Araignee","Serpent","Momie"]:
    	cpt = 0
    	for i in range(len(cartes_terrain)):
            if dangers == cartes_terrain[i][0]:
            	cpt += 1
    	if cpt > 1:
            return 0
    return 1

def nouvelle_manche():
    '''
    Cette fonction permet de réinstaliser les variables et
    listes qui en besoin pour passer à une nouvelle manche.
    Elle ne retourne rien et ne prend pas de paramètres.
    Elle est appelée par la fonction principale.
    '''
    global rubis_plateau
    global reste_plateau
    global relique_en_jeu
    joueur_actif.clear()
    for prenom in joueur.keys():
    	joueur_actif.append(prenom)
    cartes_terrain.clear()
    joueur_sortant.clear()
    relique_en_jeu = False
    rubis_plateau = 0
    reste_plateau = 0
    return

def relique_possible(carte):
    '''
    Cette fonction permet de savoir si une relique est déjà
    présente sur le plateau en renvoyant True ou False.
    Elle est apelé par la fonction tirer_carte().
    -------------------------------------------------------
    Entrée: une carte de type list
    Sortie: un booléen
    '''
    for rel in cartes_terrain:
        if rel[0] == "Relique" and carte[0] == "Relique":
            return False
    return True

def tirer_cartes():
    '''
    Cette fonction permet de choisir une carte aléatoirement
    dans la liste des cartes en vérifiant qu'elle n'est pas
    déjà présente sur le plateau.
    --------------------------------------------------------
    Entrée: Aucune
    Sortie: une carte de type list
    '''
    nvl_carte = random.choice(cartes)
    while nvl_carte in cartes_terrain or relique_possible(nvl_carte) == False:
        nvl_carte = random.choice(cartes)
    cartes_terrain.append(nvl_carte)
    return nvl_carte

def gagnant():
    '''
    Cette fonction permet de trouver le joueur avec le plus de rubis.
    Elle est appelée par la fonction principale.
    -----------------------------------------------------------------
    Entrée: aucune
    Sortie: fonction g_victoire()
    '''
    max = -1
    victoire = None
    for nom in joueur.keys():
        if joueur[nom][1] > max:
            victoire = nom
            max = joueur[nom][1]
    return g_victoire(victoire)

############################################
############Fonction principale#############
############################################

def Jeu():
    '''
    Il s'agit ici de la fonction principale du code.
    Elle appelle toutes les fonctions qui sont nécessaires
    au bon déroulement du jeu.
    Cette fonction ne renvoie rien.
    '''
    global reste_plateau
    global g
    global objet
    global nb_manches
    print("Bienvenue dans Diamond")
    nom = nom_joueur()
    g_base()
    g_prendre_relique()
    aventure = True
    print("Êtes vous prêt pour l'expédition ?")
    time.sleep(1)
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)
    print("C'est parti !")
    while nb_manches < 6:
        #boucle permettant de ne pas stopper le jeu avant les 5 manches
        g_manche()
        while aventure is True:
            if test_fin_manche() == 1:
                carte_actu = tirer_cartes()
                g_test_carte(carte_actu)
                g.actualiser()
                g_apparition(carte_actu)
                ajouter_rubis(carte_actu)
                distribuer_rubis()
                objet=g_update()
            if test_fin_manche() == 1:
                continuer()
                fuite()
            elif test_fin_manche() == 0:
                cartes.remove(carte_actu)
                g_perte()
                aventure = False
            else:
                aventure = False
        mort()
        g_reset()
        nouvelle_manche()
        g_prendre_relique()
        nb_manches += 1
        aventure = True
        objet = g_update()
    g_classement()
    gagnant()
    g.fermerFenetre()
    print("Merci d'avoir joué")

Jeu()
