# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Étape 1: sélectionner les mots ayant la bonne largeur


# Chemin vers le fichier contenant ma liste de mots
# Ici je prends une liste plus courte que ce soit plus rapide à calculer
fichier = 'dict/Francais_Lettre-A_1.txt'


# J’ouvre et je lis le fichier
mots = open(fichier, "r", encoding='utf-8')
mots = mots.readlines() 


# Sélection de la typo et du corps
font("Times", 100) 

# Largeur de mot recherchée, amuse-toi à modifier cette valeur
maLargeur = 400

# Je détermine une petite marge d'ajustement car les mots ayant exactement la bonne largeur sont rares…
marge = 1 # Amuse-toi à modifier cette valeur
largeurMin = maLargeur - marge
largeurMax = maLargeur + marge

# Dans cette liste sera stocké les mots correspondant à ma largeur recherchée
resultat = []

# Je parcours la liste de mots
for i in mots: 
    
    
    # Dans le fichier texte il y a un retour à la ligne après chaque mot
    # strip() me permet de supprimer ce retour à la ligne inutile
    mot = i.strip() 
    
    
    # Je calcule la taille du mot
    taille = textSize(mot) 
    
    # Je ne garde que la largeur
    largeur = taille[0]
    
    # Si la largeur du mot est comprise entre ma largeur minimale et maximale
    if largeurMin < largeur < largeurMax:
        
        # Afficher la taille dans la console
        print(f'{mot}: {largeur}')
        
        # J'ajoute mon mot à ma liste de résultat
        resultat.append(mot)
    
    
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Étape 2: afficher les mots sélectionnés

# Je dois transformer ma liste de résultat en un texte (variable de type “list” vers variable de type “string”)
# J’utilise la méthode “join” en lui disant de m'ajouter un retour à la ligne ”\n” entre chaque mot
texte = '\n'.join(resultat)
   
# Nouvelle page au format 2000 / 3000
newPage(2000, 3000) 

# Sélection de la typo et du corps
font("Times", 48) 

# J'affiche mon texte dans un bloc de texte
textBox(texte, (0, 0, 2000, 3000))

# J’exporte un fichier .PDF
#saveImage("mots.pdf")