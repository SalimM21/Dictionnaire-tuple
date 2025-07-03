# Dictionnaire original
notes_eleves = {"Alice": 12, "Bob": 8, "Claire": 15, "David": 9}

# 1. Obtenir les paires clé-valeur et les trier par valeur (ascendant)
paires_triees = sorted(notes_eleves.items(), key=lambda x: x[1])

# 2. Créer un nouveau dictionnaire à partir des paires triées
dictionnaire_trie = dict(paires_triees)

print(dictionnaire_trie)