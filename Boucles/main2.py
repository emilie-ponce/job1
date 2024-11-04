        #JOB 1
for loop in range(20):
    print(loop)


        #JOB 2
for nombre in range(0, 20, 2):
    print(nombre)


        #JOB 3
nombre = 0
while nombre < 21:
    print(nombre * nombre)
    nombre += 1
 

        #JOB 4
def table_multiplication(N):
    for i in range(1, 11):
        print(i, "*",N, "=",i*N)
while True :
    N = int(input("saisir un nombre"))
    if N > 0 : 
     break
table_multiplication(N)


        #JOB 5
N = 1
while N < 13:
    print(N)
    N += 1


        #JOB 7
for loop in range(13):
    print(loop)

Z = 0
while Z < 13:
    print("tour",  Z * 3 - 2)
    Z += 1
