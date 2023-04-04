# -*- coding: utf-8 -*-
import csv

# Ouvrir le fichier """
fichier = open('N:/P_NSI/Projet Naissance/PN_01.csv', "r")
table = list(csv.reader(fichier, delimiter=";"))
fichier.close()


nvliste = []

# On trie la liste table pour obtenir une liste par personne qui est ordonnée selon le format [DD,MM,YYYY,G]
for elt in table :
    person = elt[0].split('/')
    person.append(elt[1])
    nvliste.append(person)

print(nvliste)

