        #JOB 1
def obtenir_fruits():
    fruits = ["pomme", "cerise", "orange"]
    return fruits
print(obtenir_fruits())


        #JOB 2
def ObtenirFruits():
    fruits = ["pomme", "cerise", "orange"]
    print(fruits[1])
ObtenirFruits()


        #JOB 3
def get_fruits():
    fruits = ["pomme", "cerise", "orange"]
    fruits.append("Melon")
    return fruits
print(get_fruits())


        #JOB 4
def ajouter_mangue():
    fruits = ['pomme', 'cerise', 'orange', 'melon'] 
    fruits.insert(2, 'mangue')  
    return fruits  

liste_fruits = ajouter_mangue()
print(liste_fruits)


        #JOB 5
L = [1, 2, 3, 4, 5]
print("Deuxième valeur de la liste:", L[1])
def remplacer_valeur():
    L[3] = L[2] + L[4]
remplacer_valeur()
print("Liste après modification:", L)
print("Dernière valeur de la liste:", L[-1])


        #JOB 6 
L = [1, 2, 3, 4, 5]
print("première valeur de la liste:", L[0])
def échanger_valeur():
    L[0], L[4] = L[4], L[0]
échanger_valeur()
print("liste après modification", L)
print("dernière valeur de la liste:", L[4])


        #JOB 7
L = [8, 24,48,2,16]
compteur = 0
for nombre in L:
    if nombre % 3 == 0:
        compteur += 1
print("Nombre de multiples de 3 dans la liste:", compteur)


        #JOB 8
L = [8, 24, 27, 48, 2, 16, 9, 7, 84, 91]
somme_paires = 0
for nombre in L:
    if nombre % 2 == 0:
        somme_paires += nombre
print("Somme des valeurs paires dans la liste:", somme_paires)


        #JOB 9
L = [8, 24, 27, 48, 2,16, 9, 102, 7, 84, 91]
print("afficher valeur maximum", L[7])
print("afficher valeur minimum", L[4])


        #JOB 10
L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]
produit = 1
for nombre in L:
    if 25 <= nombre <= 90:
        produit *= nombre
print("produit des valeurs dans l'intervalle [25, 90] :", produit)
