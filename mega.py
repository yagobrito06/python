import random

def tela():
    a = int(input("quantos jogos vc que?:"))
    if a < 1:
        exit()
    mostrar_jogos(a)

def mostrar_jogos(j):
    for x in range(j):
        numeros = " "
        for y in range(6):
            numeros = numeros + str(random.randint(1,60)) + " , "
        
        print("numeros --> ", numeros ) 

if __name__ == "__main__":
    while True:
       tela()