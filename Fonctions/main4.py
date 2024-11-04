        #JOB 1
def My_print_hello():
    print("Hello world")
My_print_hello()


        #JOB 2
name = "emilie" 
def My_print_name(nom):
    print(nom)
My_print_name(name)


        #JOB 3
v1 = 3
v2 = 3
def add(valeur1, valeur2):
    print(valeur1 + valeur2) 
add(v1, v2)


        #JOB 4
def GetHello():
    return print("Hello la Plateforme")
GetHello()


        #JOB 5
def calcule(num1, operator, num2):
    if operator == '+':
        return print(num1 + num2)
    elif operator == '-':
        return print(num1 - num2)
    elif operator == '*':
        return print(num1 * num2)
    elif operator == '/':
        return print(num1 / num2)
    elif operator == "%":
        return print(num1 % num1)

calcule(8, '+', 8)
calcule(8, '-', 8)
calcule(8, '*', 8)
calcule(8, '/', 8)
calcule(8, '%', 8)


        #JOB 6
def nombre(number):
    if number > 0:
        print("positif")
    elif number < 0:
        print("negatif")

nombre(6)
nombre(-6)


        #JOB 7
def identifier(langage):
    if langage == "JavaScript":
        print("tu es un développeur web")
    elif langage == "python":
        print("tu es un développeur IA")
    elif langage == "java":
        print("tu es un développeur logiciel")
    elif langage == "reactjs":
        print("tu es un développeur mobile")
    else:
        print("un jour, je serai le meilleur développeur")
identifier("JavaScript")
identifier("python")
identifier("java")
identifier("reactjs")


        #JOB 8 
def fruit(type, saison):
    if type == "fruits" and saison == "hiver":
        print("orange, mandarine, kiwi")
    elif type == "fruits" and saison == "été":
        print("poire, fraise, cassis")
    elif type == "légume" and saison == "hiver":
        print("carotte, topinambour, endive")
    elif type == "légume" and saison == "été":
        print("artichaut, aubergine, navet")
fruit("fruits", "hiver")
fruit("fruits", "été")
fruit("légume", "hiver")
fruit("légume", "été")
