First_dict = { "Appareil": "Laptop", "Marque": "IBM", "Carte mère": "MSI Z490", "Carte Graphique":"GeForce RTX 3070", "RAM": "16G", "Processeur": "Intel core i7-G11", "SSD": "1 To" }

print("Voici les informations de l'appareil :")
for key, value in First_dict.items():
    print(f"{key} : {value}")  

# Corriger la valeur associée à la clé "RAM" pour qu’elle devienne "32G".
First_dict["RAM"] = "32G"

# Afficher le dictionnaire après la mise à jour
print("\nAprès la mise à jour de la RAM :")
for key, value in First_dict.items():
    print(f"{key} : {value}")  

# Affichage de la liste des clés
print("\nListe des clés du dictionnaire :")
keys_list = list(First_dict.keys())
for key in keys_list:
    print(key)

# Affichage de la liste des valeurs
print("\nListe des valeurs du dictionnaire :")
values_list = list(First_dict.values())
for value in values_list:
    print(value)
   
# Affichage de la liste des paires clé-valeur
print("\nListe des paires clé-valeur du dictionnaire :")
items_list = list(First_dict.items())
for item in items_list:
    print(f"{item[0]} : {item[1]}")
 
# Inverser les paires "Processeur" : "Intel core i7-G11" et "Carte Graphique" : "GeForce RTX 3070"
First_dict["Processeur"], First_dict["Carte Graphique"] = First_dict["Carte Graphique"], First_dict["Processeur"]

# Ajouter la paire clé-valeur suivante : "Système d’exploitation": "Windows 10"
First_dict["Système d’exploitation"] = "Windows 10"

# Afficher le dictionnaire après les modifications
print("\nAprès les modifications :")
for key, value in First_dict.items():
    print(f"{key} : {value}")   


