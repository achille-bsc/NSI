#5. Ecrire une fonction qui donne le nombre de jours depuis la précédente pleine lune pour une date comprise entre le 1er janvier 2000 et le 31 décembre 2008.

#module pour calculer un delta entre deux dates qui fonctionne sur le principe: Le 1 er janvier de l'année 1 est appelé jour numéro 1, le 2 janvier de l'année 1 est appelé jour numéro 2, et ainsi de suite.
#https://docs.python.org/fr/3/library/datetime.html
from datetime import date

#liste de toutes les dates de pleine lune comprise entre le 1er janvier 2000 et le 31 décembre 2008 en format DD/MM/YYYY
dates_pleine_lune=[[21, 1, 2000], [19, 2, 2000], [20, 3, 2000], [18, 4, 2000], [18, 5, 2000], [16, 6, 2000], [16, 7, 2000], [15, 8, 2000], [13, 9, 2000], [13, 10, 2000], [11, 11, 2000], [11, 12, 2000], [9, 1, 2001], [8, 2, 2001], [9, 3, 2001], [8, 4, 2001], [7, 5, 2001], [6, 6, 2001], [5, 7, 2001], [4, 8, 2001], [2, 9, 2001], [2, 10, 2001], [1, 11, 2001], [30, 12, 2001], [28, 1, 2002], [27, 2, 2002], [28, 3, 2002], [27, 4, 2002], [26, 5, 2002], [24, 6, 2002], [24, 7, 2002], [22, 8, 2002], [21, 9, 2002], [21, 10, 2002], [20, 11, 2002], [19, 12, 2002], [18, 1, 2003], [16, 2, 2003], [18, 3, 2003], [16, 4, 2003], [16, 5, 2003], [14, 6, 2003], [13, 7, 2003], [12, 8, 2003], [10, 9, 2003], [10, 10, 2003], [9, 11, 2003], [8, 12, 2003], [7, 1, 2004], [6, 2, 2004], [6, 3, 2004], [5, 4, 2004], [4, 5, 2004], [3, 6, 2004], [2, 7, 2004], [30, 8, 2004], [28, 9, 2004], [28, 10, 2004], [26, 11, 2004], [26, 12, 2004], [25, 1, 2005], [24, 2, 2005], [25, 3, 2005], [24, 4, 2005], [23, 5, 2005], [22, 6, 2005], [21, 7, 2005], [19, 8, 2005], [18, 9, 2005], [17, 10, 2005], [16, 11, 2005], [15, 12, 2005], [14, 1, 2006], [13, 2, 2006], [14, 3, 2006], [13, 4, 2006], [13, 5, 2006], [11, 6, 2006], [11, 7, 2006], [9, 8, 2006], [7, 9, 2006], [7, 10, 2006], [5, 11, 2006], [5, 12, 2006], [3, 1, 2007], [2, 2, 2007], [3, 3, 2007], [2, 4, 2007], [2, 5, 2007], [1, 6, 2007], [30, 7, 2007], [28, 8, 2007], [26, 9, 2007], [26, 10, 2007], [24, 11, 2007], [24, 12, 2007], [22, 1, 2008], [21, 2, 2008], [21, 3, 2008], [20, 4, 2008], [20, 5, 2008], [18, 6, 2008], [18, 7, 2008], [16, 8, 2008], [15, 9, 2008], [14, 10, 2008], [13, 11, 2008], [12, 12, 2008]]

#définition de ma foction qui attend une date de format DD/MM/YYYY
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


#6. Ecrire une fonction qui prend en argument une liste de dates et retourne une liste de valeurs correspondant aux nombres de ces dates par distance avec la précédente pleine lune.

#définition de ma foction qui attend une liste de dates de format DD/MM/YYYY
def classement_j_depuis_lune(liste_dates_DD_MM_YYYY):

    #définition d'une liste contenant le nombre de pleines lunes par delta de temps, première donnée delta de 0 jour et dernière donnée delta de 31 jours
    liste_classement=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    for date in liste_dates_DD_MM_YYYY:
        delta=j_depuis_lune(date)
        #en fonction du delta entre les deux dates testées le conteur correspondant dans 'liste_classement' est incrémenté
        liste_classement[delta]+=1
    return liste_classement

#liste_de_teste=[[30, 1, 2000], [19, 2, 2000], [22, 1, 2000], [1, 3, 2000], [17, 4, 2000], [11, 12, 2008]]
#9, 0, 1, 11,, 28, 28