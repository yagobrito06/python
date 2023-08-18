import hashlib

def tela():
    email = (input("email:"))
    senha = (input("senha:"))
    s= senha + email
    criptografar(s)

def criptografar(senha):
    s = senha 
    criptografado = hashlib.sha512(s.encode("utf-8")).hexdigest()
    print(senha)
    print("sua senha criptografada e  : " + criptografado)


if __name__ == "__main__":
    tela()