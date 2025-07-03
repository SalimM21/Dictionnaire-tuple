# Utilisez update() pour fusionner trois dictionnaires différents.

dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
dict3 = {'e': 5, 'f': 6}

# Créer une copie du premier dictionnaire pour éviter de le modifier directement
resultat = dict1.copy()

# Fusionner les dictionnaires un par un avec update()
resultat.update(dict2)
resultat.update(dict3)

print(resultat)




# Vous pouvez également utiliser l'opérateur `|` pour fusionner les dictionnaires en Python 3.9 et versions ultérieures :
# resultat = dict1 | dict2 | dict3  
# Cela donne le même résultat.
# Notez que si des clés identiques existent dans les dictionnaires, la valeur de la clé dans le dernier dictionnaire écrasera les valeurs précédentes. Par exemple, si dict1 avait une clé 'a' avec une valeur de 10, le résultat final aurait {'a': 10, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}.
# Assurez-vous que les clés sont uniques dans les dictionnaires que vous fusionnez pour éviter les conflits de clés.
# Si vous souhaitez conserver les valeurs des clés en cas de conflit, vous pouvez utiliser une logique personnalisée pour gérer les conflits, par exemple en combinant les valeurs dans une liste ou en utilisant une fonction de fusion spécifique.
# Voici un exemple de fusion avec une logique personnalisée pour gérer les conflits de clés:
def merge_dicts(dict1, dict2):
    merged = dict1.copy()  # Créer une copie du premier dictionnaire
    for key, value in dict2.items():
        if key in merged:
            # Si la clé existe déjà, combiner les valeurs dans une liste
            merged[key] = [merged[key], value] if isinstance(merged[key], list) else [merged[key], value]
        else:
            merged[key] = value
    return merged
# Exemple d'utilisation
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
dict3 = {'c': 5, 'd': 6}
resultat = merge_dicts(merge_dicts(dict1, dict2), dict3)
print(resultat)
# Ce code fusionne trois dictionnaires en combinant les valeurs des clés en cas de conflit.
# Le résultat sera : {'a': 1, 'b': [2, 3], 'c': [4, 5], 'd': 6}
# Vous pouvez adapter la logique de fusion selon vos besoins spécifiques. 