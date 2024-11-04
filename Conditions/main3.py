        #JOB 1
valeur1 = int(input("stocke une valeur"))
valeur2 = int(input("stocke une deuxième valeur"))
if valeur1 == valeur2:
    print("valeur1 et valeur2 sont égales")
else:
    print("valeur1 et valeur2 ne sont pas égales")


        #JOB 2
age = 18
if age >= 18:
    print("Tu peux voter")
else:
    print("Tu ne peux pas voter")


        #JOB 3
for nombre in range(101):  
    if nombre in [26, 37, 88]:
        continue  
    print(nombre)


        #JOB 4
for nombre in range(1, 101):
    if nombre % 3 == 0 and nombre % 5 == 0:
        print("FizzBuzz")
    elif nombre % 3 == 0:
        print("Fizz")
    elif nombre % 5 == 0:
        print("Buzz")
    else:
        print(nombre)


        #JOB 5
def nombrePremier(nombre):
    for n in range(2, nombre):
        if nombre % n == 0:
            return False
        return True
print(nombrePremier(3))

for x in range(2, 1000):
    if nombrePremier(x):
        print(x)


        #JOB 6 
nombre = int(input("nombre pair"))
if nombre == int:
    print("le nombre x est pair")
else:
    print("le nombre est impair")


        #JOB 7
chaine = "abcdefghijklmnopqrstuvwxyz" * 10
print(chaine)
