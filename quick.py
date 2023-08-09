import qrcode

def tela():
    nome = (input("nome:"))
    email = (input("email:"))
    celular = (input("celular:"))
    x = " nome " + nome +" \n email " + email +" \n celular " + celular
    gerar_qrcode(x, celular)


def gerar_qrcode(dados, arquivo):
    img = qrcode.make(dados)
    arquivo = arquivo + ".png"
    img.save(arquivo)

if __name__ == "__main__":
    tela()