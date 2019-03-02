from googlesearch import search

print("@Nxrman_ - BUSCADOR DE LINKS ONION (DEEP WEB)")
print("")
input('Aperte ENTER para continuar')
print("Exemplos de conteúdo: Hacking, Forum, eBooks")
conteudo = str(input("coloque o conteúdo:"))

dork = f'{conteudo} site:onion.link | site:onion.cab | site:onion.sh | site:tor2web.fi | site:onion.direct'

def menu():
    print("0 - Sair")
    print("1 - Procurar sites onion")


while True:
    menu()
    menuzinho = int(input("Selecione uma opção: "))
    if menuzinho == 0:
        print("Até a proxima")
        break
    elif menuzinho == 1:
        with open("sitesonion.txt", "w") as stream:
            for url in search(dork, stop=100 or 1):
                print(url, file=stream)
                print("Os URLS dos sites foram salvos em um arquivo chamado: sitesonion.txt")
    else:
        print("Essa opção não existe, tente novamente!")
