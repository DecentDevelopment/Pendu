# -*- coding: utf-8 -*-

from random import choice

#Définition du chemin du fichier contenant la liste des mots français
adresse_fichier = "liste_francais_modifiee.txt"

#Initialisation de la variable pour suivre les lettres déjà utilisées
lettres_utilisees = ""

def choix_mot(adresse_fichier) :
    """ fonction ouvrant un fichier texte dont l'adresse absolue ou relative
    est passée en argument sous la forme d'une chaine de caractère
    et renvoyant une chaine de caractère issue d'une ligne aléatoire du fichier
"""
    with open(adresse_fichier, 'r', encoding='utf8') as file:
        mot = choice([m for m in file.readlines()]).replace('\n', '').strip()
    return mot

#Fonction pour formater un mot en retirant les accents et en le mettant en majuscules
def formate_mot(mot : str) -> str :
    """ fonction transformant une chaine de caractères accentués
en une chaine de caractère latin strict (sans accents ni signes diacritiques).
La chaine renvoyée est en majuscule.

>>> formate_mot('tRuC')
'TRUC'
>>> formate_mot('Abécédaire')
'ABECEDAIRE'
>>> formate_mot('')
''
>>> formate_mot('où')
'OU'
>>> formate_mot('garçONs')
'GARCONS'
>>> formate_mot('àâäéèêëîïôöûùüç')
'AAAEEEEIIOOUUUC'
>>> formate_mot('œil')
'OEIL'
>>> formate_mot('Lætitia')
'LAETITIA'
"""

    #Définition des caractères spéciaux et des groupes d'accents
    caractere_speciaux = 'ÀÁÂÄÅÃÆÇÉÈÊËÍÌÎÏÑÓÒÔÖØÕŒÚÙÛÜÝŸŶ'
    accent_e = 'ÉÈÊË'
    accent_a = 'ÀÁÂÄÅÃ'
    accent_i = 'ÍÌÎÏ'
    accent_o = 'ÓÒÔÖØÕ'
    accent_u = 'ÚÙÛÜ'
    accent_y = 'ÝŸŶ'

    #Mettre le mot en majuscules
    mot = mot.upper()
    longueur = len(mot)

    #Parcourir le mot pour remplacer les caractères spéciaux par leurs équivalents sans accents
    if mot.find(caractere_speciaux):
        for i in range(longueur):
            if mot[i] in caractere_speciaux:
                if mot[i] in (accent_e):
                    mot = mot.replace(mot[i],'E')
                elif mot[i] in (accent_a):
                    mot = mot.replace(mot[i],'A')
                elif mot[i] in (accent_i):
                    mot = mot.replace(mot[i],'I')
                elif mot[i] in (accent_o):
                    mot = mot.replace(mot[i],'O')
                elif mot[i] in (accent_y):
                    mot = mot.replace(mot[i],'Y')
                elif mot[i] in (accent_u):
                    mot = mot.replace(mot[i],'U')
                elif mot[i] == 'Æ':
                    mot = mot.replace(mot[i],'AE')
                    longueur += 1
                elif mot[i] == 'Œ':
                    mot = mot.replace(mot[i],'OE')
                    longueur += 1
                elif mot[i] == 'Ñ':
                    mot = mot.replace(mot[i],'N')
                elif mot[i] == 'Ç':
                    mot = mot.replace(mot[i],'C')
                elif mot[i] == '@':
                    mot = mot.replace(mot[i],'A')

    return mot


#Fonction pour générer une chaîne avec des tirets pour les lettres non révélées
def genere_tirets(mot_a_trouver : str, lettres_utilisees: str ) -> str :
    """ fonction renvoyant une chaine de caractère correspondant
au mot à trouver pour lequel :
* les caractères non présents dans la chaine lettreUtilisees
sont remplacés par des _ (underscores) ;
* les tirest hauts "-" sont conservés ;
* tous les caractères sont suivis d'un espace, y compris le dernier.

>>> genere_tirets("Bidules", "Ble")
'B _ _ _ L E _ '
>>> genere_tirets("toto", "")
'_ _ _ _ '
>>> genere_tirets("bananes", "bn")
'B _ N _ N _ _ '
>>> genere_tirets("toto", "ot")
'T O T O '
>>> genere_tirets("pull-over", "plr")
'P _ L L - _ _ _ R '
>>> genere_tirets("pull-over", "pulover")
'P U L L - O V E R '
"""
    #Formater le mot à trouver
    mot_a_trouver = formate_mot(mot_a_trouver)
    lettres_utilisees = lettres_utilisees.upper()
    mot = ""
    longueur_formate = len(mot_a_trouver)

    #Parcourir le mot à trouver pour générer la chaîne avec des tirets
    for i in range(longueur_formate):
        if mot_a_trouver[i] in lettres_utilisees:
            mot = mot + mot_a_trouver[i] +" "
        elif mot_a_trouver[i] == "-" :
            mot = mot + "- "
        else :
            mot = mot +"_ "
            
    return mot


#Fonction pour compter les lettres non révélées restantes dans un mot
def compte_restantes(mot_a_trouver : str, lettres_utilisees : str ) -> int :
    """ fonction renvoyant le nombre de lettres non encore trouvées
dans le mot, en connaissant les lettres déjà utilisées.
Un tiret haut "-" ne compte pas dans les lettres à trouver.
La valeur renvoyée est un entier

>>> compte_restantes("bananes","bn")
4
>>> compte_restantes("toto","to")
0
>>> compte_restantes("toto","")
4
>>> compte_restantes("","")
0
>>> compte_restantes("","z")
0
>>> compte_restantes("bidules","bidule")
1
>>> compte_restantes("pull-over", "plr")
4
>>> compte_restantes("pull-over", "pulover")
0

"""
    formate_mot_a_trouver = formate_mot(mot_a_trouver)
    nb_echecs = 0
    mot = genere_tirets(mot_a_trouver, lettres_utilisees)

    # Compter les lettres non révélées
    compte_restantes = 0
    for lettre in lettres_utilisees:
        if lettre not in formate_mot_a_trouver:
            nb_echecs += 1

    for c in mot:
        if c == '_':
            compte_restantes += 1

    return compte_restantes

#Fonction pour afficher la figure du pendu
def affiche_pendu(mot_a_trouver : str, lettres_utilisees : str, nb_echecs : int) -> None :
    """ fonction affichant à la fois la potence mais aussi le mot
à trouver sous sa forme de tirets
    """
    #Définir les éléments de la figure du pendu en fonction du nombre d'erreurs
    if nb_echecs >= 1:
        a = "o"
    else:
        a = ' '
    if nb_echecs >= 2:
        corps = "|"
    else:
        corps = ' '
    if nb_echecs >= 3:
        bg = "/"
    else:
        bg = ' '
    if nb_echecs >= 5:
        jg = "/"
    else:
        jg = ' '
    if nb_echecs >= 4:
        bd = "\ "
    else:
        bd = '  '
    if nb_echecs >= 6:
        jd = "\ "
    else:
        jd = '  '
    
    #Afficher la figure du pendu
    print(f"""
   _ _ _
  {a}     |
{bg} {corps} {bd}  |
 {jg} {jd}   |
        |
 _______|__ 
""")

#Fonction pour demander une lettre au joueur
def demande_joueur_lettre() -> str:
    """ fonction demandant une lettre latine non accentuée au joueur,
et renvoyant cette lettre en majuscule. La fonction redemande au joueur
tant que celui-ci n'a pas fourni une lettre correcte.
La lettre est renvoyée en par la fonction.
"""
    global lettres_utilisees
    alpha = "abcdefghijklmnopqrstuvwxyz"

    while True:
        #Demander à l'utilisateur de saisir une lettre
        lettre = input("Veuillez saisir une lettre latine non accentuée : ")

        #Vérifier si la lettre est déjà utilisée
        if lettre in lettres_utilisees:
            print("Cette lettre est déjà utilisée.")
        else:
            #Vérifier si l'entrée est une lettre et si elle est non accentuée
            if len(lettre) == 1 and lettre in alpha:
                #Mettre à jour les lettres utilisées
                lettres_utilisees += lettre
                #Convertir la lettre en majuscule et la renvoyer
                return lettre.upper()
            else:
                #Afficher un message d'erreur et redemander à l'utilisateur de saisir une lettre correcte
                print("Veuillez saisir une seule lettre latine non accentuée.")


#Fonction pour effectuer une manche du jeu
def une_manche() -> None :
    """ fonction déclenchant une manche de jeu. On entend par manche de jeu :
* le choix d'un mot dans le fichier 'liste_francais_modifiee.txt' ;
* le formatage de ce mot ;
* puis la répétitions de :
    * la demande d'une lettre au joueur ;
    * la mise à jour des lettres utilisée le cas échéant ;
    * la mise à jour de l'affichage
    
    jusqu'à ce que soit le mot complet ait été trouvé,
    soit que le dessin du pendu soit terminé (6 étapes).
    """
    global lettres_utilisees
    lettres_utilisees = ""  #Réinitialisation de la variable globale pour chaque manche

    #Choix d'un mot aléatoire
    mot_a_trouver = choix_mot(adresse_fichier)
    mot = formate_mot(mot_a_trouver)
    nb_echecs = 0

    #Boucle principale du jeu
    while compte_restantes(mot, lettres_utilisees) > 0 and nb_echecs < 6:
        print(f"Les lettres déjà utilisées sont : {lettres_utilisees.upper()}")
        print(genere_tirets(mot_a_trouver, lettres_utilisees))

        #Affichage de la figure du pendu
        affiche_pendu(mot_a_trouver, lettres_utilisees, nb_echecs)

        #Demande de lettre au joueur
        lettre = demande_joueur_lettre()

        #Mise à jour du nombre d'échecs si la lettre n'est pas dans le mot
        if lettre not in mot:
            nb_echecs += 1

        #Vérification si le mot est entièrement trouvé
        if compte_restantes(mot, lettres_utilisees) == 0:
            print(genere_tirets(mot_a_trouver, lettres_utilisees))
            print(f"Vous avez gagné")
            break

    #Si le nombre d'échecs atteint 6, le joueur a perdu
    if nb_echecs == 6:
        print(f"Vous avez perdu, le mot était {mot}")


def presentation() -> None :
    """ fonction affichant uniquement la présentation"""
    print("""
##############################################
#                                            #
#                Jeu du Pendu                #
#                                            #
# 1ère NSI 2022-2023                         #
##############################################
""")
    
            
def main() -> None:
    """ fonction principale du jeu, permettant d'effectuer plusieurs manches"""
    while True :
        presentation()
        une_manche()
        rep = input("Voulez-vous rejouer ? (o/n)")
        if rep.lower() not in ['o', 'oui', 'y', 'yes'] :
            break
    print("Au revoir !")

## La partie ci-dessous n'est effectuée que si vous déclenchez le programme
## en tant que programme principal (notion de modules, vue en terminale)
            
if __name__ == "__main__" :
    
    import doctest
    doctest.testmod()
    main()
