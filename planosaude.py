def tela():
    a = int(input("qual sua idade?:"))
    if a < 1:
        exit()
    print("voce e =",idade(a))

def idade(i):
    if i <= 12:
        return "crianca"

    if i >12 and  i <= 14:
        return "pre adolescente"

    if i >14 and i  <= 18:
        return "adolescente"

    if i >18 and i  <= 30:
        return "jovem"

    if i >30 and i < 65:
        return "adulto"

    if i >65:
        return "ta fazendo hora extra"

    return "nao sei"
    
if __name__ == "__main__":
    while True:
       tela()