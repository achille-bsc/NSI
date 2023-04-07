# -*- coding: utf-8 -*-
import csv

def lire_fichier_csv(nom_fichier):
    """
    Lit un fichier CSV et retourne son contenu sous forme d'une liste de listes.
    Chaque sous-liste correspond à une ligne du fichier.

    Args:
        nom_fichier (str): le chemin vers le fichier CSV à lire.

    Returns:
        list: le contenu du fichier CSV sous forme d'une liste de listes.
    """
    # Ouverture du fichier en mode lecture
    fichier = open(nom_fichier, "r")

    # Lecture du contenu du fichier CSV dans une liste de listes
    table = list(csv.reader(fichier, delimiter=";"))

    # Fermeture du fichier
    fichier.close()

    # Retourne le contenu du fichier
    return table


# Lecture du fichier CSV PN_01.csv
table = lire_fichier_csv("./PN_01.csv")

# Création d'une nouvelle liste ordonnée pour chaque personne, avec le format [DD,MM,YYYY,G]
nvliste = []
for elt in table[1:] :
    person = elt[0].split('/')
    person.append(elt[1])
    nvliste.append(person)


def switch_week_days(actual_day, switch_size) -> str :
    """
    Cette fonction permet de passer d'un jour à l'autre en utilisant un décalage d'un certain nombre de jours.

    Args:
        actual_day (str): le jour de départ.
        switch_size (int): le nombre de jours de décalage.

    Returns:
        str: le jour correspondant au décalage par rapport au jour de départ.
    """
    while (switch_size > 0):
        if (actual_day == "Lundi" and switch_size >= 1):
            actual_day = "Mardi"
            switch_size -= 1
        elif (actual_day == "Mardi" and switch_size >= 1):
            actual_day = "Mercredi"
            switch_size -= 1
        elif (actual_day == "Mercredi" and switch_size >= 1):
            actual_day = "Jeudi"
            switch_size -= 1
        elif (actual_day == "Jeudi" and switch_size >= 1):
            actual_day = "Vendredi"
            switch_size -= 1
        elif (actual_day == "Vendredi" and switch_size >= 1):
            actual_day = "Samedi"
            switch_size -= 1
        elif (actual_day == "Samedi" and switch_size >= 1):
            actual_day = "Dimanche"
            switch_size -= 1
        elif (actual_day == "Dimanche" and switch_size >= 1):
            actual_day = "Lundi"
            switch_size -= 1
        else :
            switch_size -= 1
    return actual_day


def day_of_week(date: str) -> str:
    """
    Cette fonction prend une date au format string "jj/mm/aaaa" et renvoie le jour de la semaine correspondant
    en utilisant la méthode de Zeller. 
    
    Args:
        date (str): Une date au format "jj/mm/aaaa"
        
    Returns:
        str : le jour de la semaine correspondant à la date entrée
    
    """
    # Jours de chaque mois
    ja  = 31
    fev = 28
    ma  = 31
    av  = 30
    mai = 31
    ju  = 30
    jui = 31
    ao  = 31
    sep = 30
    oct = 31
    nov = 30
    dec = 31

    jour_sem = ''  # initialisation de la variable du jour de la semaine
    date1 = date[0].split("/")  # séparer la date en jour, mois, année

    # Algorithme de Zeller pour déterminer le jour de la semaine
    if date1[2] == "2000" :
        jour_sem = "Samedi"
    if date1[2] == "2001" :
        jour_sem = "Lundi"
    if date1[2] == "2002" :
        jour_sem = "Mardi"
    if date1[2] == "2003" :
        jour_sem = "Mercredi"
    if date1[2] == "2004" :
        jour_sem = "Jeudi"
    if date1[2] == "2005" :
        jour_sem = "Samedi"
    if date1[2] == "2006" :
        jour_sem = "Dimanche"
    if date1[2] == "2007" :
        jour_sem = "Lundi"

    if date1[2] == "2000" or date1[2] == "2004":
        fev = 29  # année bissextile : le mois de février contient 29 jours

    # Calcul du nombre de jours écoulés depuis le début de l'année
    if date1[1] == "01" :
        days = date1[0]
    elif date1[1] == "02" :
        days = ja + int(date1[0])
    elif date1[1] == "03" :
        days = ja + fev + int(date1[0])
    elif date1[1] == "04" :
        days = ja + fev + ma + int(date1[0])
    elif date1[1] == "05" :
        days = ja + fev + ma + av + int(date1[0])
    elif date1[1] == "06" :
        days = ja + fev + ma + av + mai + int(date1[0])
    elif date1[1] == "07" :
        days = ja + fev + ma + av + mai + ju + int(date1[0])
    elif date1[1] == "08" :
        days = ja + fev + ma + av + mai + ju + jui + int(date1[0])
    elif date1[1] == "09" :
        days = ja + fev + ma + av + mai + ju + jui + ao + int(date1[0])
    elif date1[1] == "10" :
        days = ja + fev + ma + av + mai + ju + jui + ao + sep + int(date1[0])
    elif date1[1] == "11" :
        days = ja + fev + ma + av + mai + ju + jui + ao + sep + oct + int(date1[0])
    elif date1[1] == "12" :
        days = ja + fev + ma + av + mai + ju + jui + ao + sep + oct + nov + int(date1[0])

    # Conversion du nombre de jours en jour de la semaine correspondant
    if int(days) % 7 == 1:
        return jour_sem
    elif int(days) % 7 == 0:
        return switch_week_days(jour_sem, 6)
    elif int(days) % 7 == 2 :
        return switch_week_days(jour_sem, 1)
    elif int(days) % 7 == 3:
        return switch_week_days(jour_sem, 2)
    elif int(days) % 7 == 4 :
        return switch_week_days(jour_sem, 3)
    elif int(days) % 7 == 5 :
        return switch_week_days(jour_sem, 4)
    elif int(days) % 7 == 6:
        return switch_week_days(jour_sem, 5)



# On créé une variable par jour de la semaine pour stocker le nombre de fois que sera itéré ce jour là dans la liste des dates

def count_dates_per_day_of_week(dates):
    """
    Cette fonction prend une liste de dates et retourne une liste contenant le nombre d'occurrences de chaque jour de la semaine.

    Args:
        dates (list): Une liste de dates.

    Returns:
        list: Une liste contenant le nombre d'occurrences de chaque jour de la semaine. Les éléments sont dans l'ordre suivant : Lundi, Mardi, Mercredi, Jeudi, Vendredi, Samedi, Dimanche.
    """
    # Initialisation des compteurs pour chaque jour de la semaine.
    monday_count = 0
    tuesday_count = 0
    wednesday_count = 0
    thursday_count = 0
    friday_count = 0
    saturday_count = 0
    sunday_count = 0

    # On itère sur chaque date pour compter le nombre de dates pour chaque jour de la semaine.
    for date in dates:
        # On utilise une structure conditionnelle pour identifier le jour de la semaine et incrémenter le compteur correspondant.
        if date == "Lundi":
            monday_count += 1
        elif date == "Mardi":
            tuesday_count += 1
        elif date == "Mercredi":
            wednesday_count += 1
        elif date == "Jeudi":
            thursday_count += 1
        elif date == "Vendredi":
            friday_count += 1
        elif date == "Samedi":
            saturday_count += 1
        elif date == "Dimanche":
            sunday_count += 1

    # On retourne une liste contenant le nombre de dates pour chaque jour de la semaine, dans l'ordre suivant : Lundi, Mardi, Mercredi, Jeudi, Vendredi, Samedi, Dimanche.
    return [monday_count, tuesday_count, wednesday_count, thursday_count, friday_count, saturday_count, sunday_count]


# On crée une liste des jours de la semaine pour chaque ligne de données dans la table.
days_list = []
for i in range(1, len(table) - 1):
    days_list.append(day_of_week(table[i]))

# On compte le nombre de dates pour chaque jour de la semaine dans la liste de jours.
dates_per_day_of_week = count_dates_per_day_of_week(days_list)

# On affiche les résultats.
print("Nombre de dates pour chaque jour de la semaine : ")
print("Lundi :", dates_per_day_of_week[0])
print("Mardi :", dates_per_day_of_week[1])
print("Mercredi :", dates_per_day_of_week[2])
print("Jeudi :", dates_per_day_of_week[3])
print("Vendredi :", dates_per_day_of_week[4])
print("Samedi :", dates_per_day_of_week[5])
print("Dimanche :", dates_per_day_of_week[6])
print("\n\n\n")



from datetime import date

##liste de toutes les dates de pleine lune comprise entre le 1er janvier 2000 et le 31 décembre 2008 en format DD/MM/YYYY
dates_pleine_lune=[[21, 1, 2000], [19, 2, 2000], [20, 3, 2000], [18, 4, 2000], [18, 5, 2000], [16, 6, 2000], [16, 7, 2000], [15, 8, 2000], [13, 9, 2000], [13, 10, 2000], [11, 11, 2000], [11, 12, 2000], [9, 1, 2001], [8, 2, 2001], [9, 3, 2001], [8, 4, 2001], [7, 5, 2001], [6, 6, 2001], [5, 7, 2001], [4, 8, 2001], [2, 9, 2001], [2, 10, 2001], [1, 11, 2001], [30, 12, 2001], [28, 1, 2002], [27, 2, 2002], [28, 3, 2002], [27, 4, 2002], [26, 5, 2002], [24, 6, 2002], [24, 7, 2002], [22, 8, 2002], [21, 9, 2002], [21, 10, 2002], [20, 11, 2002], [19, 12, 2002], [18, 1, 2003], [16, 2, 2003], [18, 3, 2003], [16, 4, 2003], [16, 5, 2003], [14, 6, 2003], [13, 7, 2003], [12, 8, 2003], [10, 9, 2003], [10, 10, 2003], [9, 11, 2003], [8, 12, 2003], [7, 1, 2004], [6, 2, 2004], [6, 3, 2004], [5, 4, 2004], [4, 5, 2004], [3, 6, 2004], [2, 7, 2004], [30, 8, 2004], [28, 9, 2004], [28, 10, 2004], [26, 11, 2004], [26, 12, 2004], [25, 1, 2005], [24, 2, 2005], [25, 3, 2005], [24, 4, 2005], [23, 5, 2005], [22, 6, 2005], [21, 7, 2005], [19, 8, 2005], [18, 9, 2005], [17, 10, 2005], [16, 11, 2005], [15, 12, 2005], [14, 1, 2006], [13, 2, 2006], [14, 3, 2006], [13, 4, 2006], [13, 5, 2006], [11, 6, 2006], [11, 7, 2006], [9, 8, 2006], [7, 9, 2006], [7, 10, 2006], [5, 11, 2006], [5, 12, 2006], [3, 1, 2007], [2, 2, 2007], [3, 3, 2007], [2, 4, 2007], [2, 5, 2007], [1, 6, 2007], [30, 7, 2007], [28, 8, 2007], [26, 9, 2007], [26, 10, 2007], [24, 11, 2007], [24, 12, 2007], [22, 1, 2008], [21, 2, 2008], [21, 3, 2008], [20, 4, 2008], [20, 5, 2008], [18, 6, 2008], [18, 7, 2008], [16, 8, 2008], [15, 9, 2008], [14, 10, 2008], [13, 11, 2008], [12, 12, 2008]]

#définition de ma foction qui attend une date de format [DD, MM, YYYY]
def j_depuis_lune(date_DD_MM_YYYY):
    liste_delta=[]
    delta_final=0
    for date_lune in dates_pleine_lune:
        #convertion de la date d'entrée en format YYYY/MM/DD attendu par le module
        d0=date(date_DD_MM_YYYY[2], date_DD_MM_YYYY[1], date_DD_MM_YYYY[0])
        #convertion de la date de pleine lune testée en format YYYY/MM/DD attendu par le module
        d1=date(date_lune[2], date_lune[1], date_lune[0])
        #tri des résultats du delta de temps entre entre la date donnée et la date de pleine lune testée, les résultats négatifs ne sont pas intéressants car se rapportant à une pleine lune qui n'a pas encore eu lieu par rapport à la date donnée.
        #".day" : Entre 1 et le nombre de jours du mois donné de l'année donnée, à partir de "1 days, 0:00:00" on obtient 1
        if ((d0 - d1).days)>=0:
            liste_delta.append((d0 - d1).days)
    #tri des résultats précédemment obtenus pour ne garder que le plus petit, se rapportant donc à la pleine lune la plus proche de la date donnée
    for i in range(len(liste_delta)):
        if liste_delta[i]<=liste_delta[i-1]:
            delta_final=liste_delta[i]
    return delta_final



# Initialisation d'un dictionnaire vide pour stocker les données
dico = {}

# Parcours des lignes du tableau, sauf la première et la dernière
for i in range(1, len(table) - 1):
    # Extraction de la date et conversion en une liste de trois entiers représentant le jour, le mois et l'année
    decomposed_date = table[i][0].split(('/'))
    # Appel de la fonction j_depuis_lune pour obtenir le nombre de jours depuis la dernière pleine lune
    j_depuis_lune_value = j_depuis_lune([int(decomposed_date[0]), int(decomposed_date[1]), int(decomposed_date[2])])

    # Vérification si le nombre de jours depuis la dernière pleine lune a déjà été enregistré dans le dictionnaire
    if (not j_depuis_lune_value in dico):
        # Si non, on l'ajoute avec une valeur initiale de 1
        dico[j_depuis_lune_value] = 1
    else:
        # Si oui, on incrémente simplement la valeur correspondante
        dico[j_depuis_lune_value] += 1

# Parcours des clés du dictionnaire triées par ordre croissant
for i in range(len(dico)):
    # Vérification si la clé i est présente dans le dictionnaire
    if i in dico:
        # Si oui, affichage du nombre de personnes nées à i jours de la pleine lune correspondante
        print("À " + str(i) + (' ' if i < 10 else '') + " jours de la pleines lune " + str(dico[i]) + (' ' if dico[i] < 10 else '') + " personnes sont nées")






# ---------------------------------------------------------------------------------------|
# ---------------------------------------------------------------------------------------|
#                                                                                        |
# ON PEUT DONC EN CONCLURE QUE IL N'Y À PAS SPÉCIFIQUEMENT PLUS DE NAISSANCE LE DIMANCHE,|
# MAIS QU'IL Y EN À LÉGÈREMENT PLUS LE JEUDI                                             |
#                                                                                        |
# ON PEUT CEPENDANT AFFIRMER AVEC CERTITUDE QU'IL Y À EFFECTIVEMENT PLUS DE NAISSANCE LES|
# JOURS DE PLEINE LUNE.                                                                  |
#                                                                                        |
# ---------------------------------------------------------------------------------------|
# ---------------------------------------------------------------------------------------|
print("\n\n\n\n\n")
print("|-------------------------------------------------------------------------------------------------|")
print("|-------------------------------------------------------------------------------------------------|")
print("|                                                                                                 |")
print("|     ON PEUT DONC EN CONCLURE QUE IL N'Y À PAS SPÉCIFIQUEMENT PLUS DE NAISSANCE LE DIMANCHE,     |")
print("|     MAIS QU'IL Y EN À LÉGÈREMENT PLUS LE JEUDI                                                  |")
print("|                                                                                                 |")
print("|     ON PEUT CEPENDANT AFFIRMER AVEC CERTITUDE QU'IL Y À EFFECTIVEMENT PLUS DE NAISSANCE LES     |")
print("|     JOURS DE PLEINE LUNE.                                                                       |")
print("|                                                                                                 |")
print("|-------------------------------------------------------------------------------------------------|")
print("|-------------------------------------------------------------------------------------------------|")