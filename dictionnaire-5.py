# Crée un tuple nommé etudiant_info contenant les informations suivantes dans cet ordre : Prénom : "Yasmine", Âge : 22, Filière : "Informatique", Moyenne générale : 17.4
# Affiche le contenu du tuple étudiant_info etudiant_info = ("Yasmine", 22, "Informatique", 17.4)
etudiant_info = ("Yasmine", 22, "Informatique", 17.4)
# Affiche le contenu du tuple étudiant_info
print(etudiant_info)



# Affiche les informations stockées dans le tuple, une par ligne, avec un texte explicite. (ex: “Prénom : Yasmine”)
print("Prénom : ", etudiant_info[0])
print("Âge : ", etudiant_info[1])
print("Filière : ", etudiant_info[2])
print("Moyenne générale : ", etudiant_info[3])

# Tente de modifier la filière dans le tuple. Que se passe-t-il ? Explique pourquoi.
try:
    etudiant_info[2] = "Mathématiques"
except TypeError as e:
    print("Erreur :", e)
    print("Les tuples sont immuables, donc on ne peut pas modifier leurs éléments.")
    # Crée un nouveau tuple nommé etudiant_info_modifiee contenant les informations de etudiant_info, mais avec la filière modifiée en "Mathématiques".
    etudiant_info_modifiee = (etudiant_info[0], etudiant_info[1], "Mathématiques", etudiant_info[3])
# Affiche le nouveau tuple etudiant_info_modifiee
print("Nouveau tuple avec la filière modifiée :", etudiant_info_modifiee)   

# Utilise l'opérateur de slicing pour afficher uniquement le prénom et l'âge.
prenom_age = etudiant_info[:2]
print("Prénom et Âge :", prenom_age)

# Crée un nouveau tuple en combinant etudiant_info avec un second tuple contenant la mention "Très Bien" et l’année d’obtention du diplôme (2024), puis affiche le tuple final.
mention_annee = ("Très Bien", 2024)
etudiant_info_final = etudiant_info + mention_annee
print("Tuple final avec mention et année :", etudiant_info_final)




# -----------------------------------------------------
# Affiche la longueur du tuple etudiant_info_final.
print("Longueur du tuple final :", len(etudiant_info_final))
# Affiche le type du tuple etudiant_info_final.
print("Type du tuple final :", type(etudiant_info_final))
# Affiche le nombre d'occurrences de l'élément "Informatique" dans le tuple etudiant_info_final.
print("Occurrences de 'Informatique' dans le tuple final :", etudiant_info_final.count("Informatique"))
# Affiche l'index de l'élément "Très Bien" dans le tuple etudiant_info_final.
print("Index de 'Très Bien' dans le tuple final :", etudiant_info_final.index("Très Bien"))
# Affiche les éléments du tuple etudiant_info_final en utilisant une boucle for.
print("Éléments du tuple final :")
for element in etudiant_info_final:
    print(element)
# Affiche les éléments du tuple etudiant_info_final en utilisant une compréhension de liste.
elements_liste = list(etudiant_info_final)
print("Éléments du tuple final (comprehension de liste) :", elements_liste)
