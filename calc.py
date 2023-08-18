def tela():
    a = int(input("digite valor de a:"))
    b = int(input("digite valor de b:"))
    print("a+b =",somar(a,b))
    print("a-b =",subtrair(a,b))
    print("a*b =",multiplicar(a,b))
    print("a/b =",dividir(a,b))
    print("a**b =",exponencial(a,b))
    print("calcular = ",calcular(a,b))

def somar(a,b):
    return (a+b)

def subtrair(a,b):
    return (a-b)

def multiplicar(a,b):
    return (a*b)

def dividir(a,b):
    return (a/b)

def exponencial(a,b):
    return (a**b)

def calcular(a,b):
    x=(a+b)**2
    y=(a-b)**3
    z=(b+3)/5
    w=((a-4)/3)**2
    return (x+y)/(z*w)

if __name__ == "__main__":
    tela()