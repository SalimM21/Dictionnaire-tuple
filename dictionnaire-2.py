notes_eleves = { "Amine": 15.5, "Yassine": 19.0, "Reda": 14.2, "Malak": 8.7, "Manal": 20.0, "Ahmed": 7.5,"Saad": 11.3, "Hannae": 9.8 }

# etudiantAdmis dont les clés sont les étudiants admis et les valeurs des clés sont les moyennes obtenues (moyenne supérieures ou égales à 10 )
etudiantAdmis = {etudiant: moyenne for etudiant, moyenne in notes_eleves.items() if moyenne >= 10}
print(etudiantAdmis)

# etudiantNonAdmis dont les clés sont les étudiants non admis et les valeurs des clés sont les moyennes obtenues (moyenne inférieure à 10 )
etudiantNonAdmis = {etudiant: moyenne for etudiant, moyenne in notes_eleves.items() if moyenne < 10}
print(etudiantNonAdmis)
