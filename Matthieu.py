
def open_file(chemin, type_action, encoding):
    #"N:/Spé NSI/Projet Naissance/PN_01.csv", "r", encoding="UTF-8-sig"
    fichier = open(chemin, type_action, encoding=encoding)
    liste_dates = fichier.read()
    fichier.close()




# Année 2000 (bissextile):

# Janvier 1-31: Début Samedi-Lundi
# Février 1-29: Mardi-Mardi
# Mars 1-31: Mercredi-Vendredi
# Avril 1-30: Samedi-Dimanche
# Mai 1-31: Lundi-Mercredi
# Juin 1-30: Jeudi-Vendredi
# Juillet 1-31: Samedi-Lundi
# Aout 1-31: Mardi-Jeudi
# Septembre 1-30: Vendredi-Samedi
# Octobre 1-31: Dimanche-Mardi
# Novembre 1-30: Mercredi-Jeudi
# Décembre 1-31: -Dimanche

# Année 2001:

# Janvier 1-31: Lundi-
# Février 1-28:
# Mars 1-31:
# Avril 1-30:
# Mai 1-31:
# Juin 1-30:
# Juillet 1-31:
# Aout 1-31:
# Septembre:
# Octobre 1-31:
# Novembre:
# Décembre 1-31: -Lundi

# Année 2002:

# Janvier 1-31: Mardi-
# Février 1-28:
# Mars 1-31:
# Avril 1-30:
# Mai 1-31:
# Juin 1-30:
# Juillet 1-31:
# Aout 1-31:
# Septembre:
# Octobre 1-31:
# Novembre:
# Décembre 1-31: -Mardi

# Année 2003:
# Janvier 1-31: Mercredi-
# Février 1-28:
# Mars 1-31:
# Avril 1-30:
# Mai 1-31:
# Juin 1-30:
# Juillet 1-31:
# Aout 1-31:
# Septembre:
# Octobre 1-31:
# Novembre:
# Décembre 1-31: -Mercredi

# Année 2004 (bissextile):

# Janvier 1-31: Jeudi-
# Février 1-28:
# Mars 1-31:
# Avril 1-30:
# Mai 1-31:
# Juin 1-30:
# Juillet 1-31:
# Aout 1-31:
# Septembre:
# Octobre 1-31:
# Novembre:
# Décembre 1-31: -Vendredi

# Année 2005:

# Janvier 1-31: Samedi-
# Février 1-28:
# Mars 1-31:
# Avril 1-30:
# Mai 1-31:
# Juin 1-30:
# Juillet 1-31:
# Aout 1-31:
# Septembre:
# Octobre 1-31:
# Novembre:
# Décembre 1-31: -Samedi

# Année 2006:

# Janvier 1-31: Dimanche-
# Février 1-28:
# Mars 1-31:
# Avril 1-30:
# Mai 1-31:
# Juin 1-30:
# Juillet 1-31:
# Aout 1-31:
# Septembre:
# Octobre 1-31:
# Novembre:
# Décembre 1-31: -Dimanche

# Année 2007:

# Janvier 1-31: Lundi-
# Février 1-28:
# Mars 1-31:
# Avril 1-30:
# Mai 1-31:
# Juin 1-30:
# Juillet 1-31:
# Aout 1-31:
# Septembre:
# Octobre 1-31:
# Novembre:
# Décembre 1-31: -Lundi


ja = 31
fev = 28
ma = 31
av = 30
mai = 31
ju = 30
jui = 31
ao = 31
sep = 30
oct = 31
nov = 30
dec = 31

##Cette fonction permet de passer d'un jour à l'autre

def switch_week_days(actual_day, switch_size):

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
    return actual_day

## Cette fonction contient les éléments principaux comme :
##-le nom du premier jour pour chaque année
##-le changement de jour pour le mois de février(année bissextile)
##-la somme des jours (par exemple pour le 22/03/2006 = jours de janvier + jours de fevrier + 22)
##-et enfin la division euclidienne des jours par 7 et si par exemple le reste = 0 ça sera le jour - 1


def fonction(date):
    date1 = date.split("/")
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
        fev = 29

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


    if days % 7 == 1:
        return jour_sem
    elif days % 7 == 0:
        return switch_week_days(jour_sem, 6)
    elif days % 7 == 2 :
        return switch_week_days(jour_sem, 1)
    elif days % 7 == 3:
        return switch_week_days(jour_sem, 2)
    elif days % 7 == 4 :
        return switch_week_days(jour_sem, 3)
    elif days % 7 == 5 :
        return switch_week_days(jour_sem, 4)
    elif days % 7 == 6:
        return switch_week_days(jour_sem, 5)










































































##
##
##if date1[3] == 2000 or date1 == 2004:
##    days= 366
##else:
##    days= 365
##
##if date1[2]== 1:
##    days = date1[1]

























