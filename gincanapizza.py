nome=input("qual o seu nome?")
número=int(input("qual o seu número?"))
email=input("qual seu email?")

cardapio={
    1:{"sabor":"calabresa","valor": 52.99},
    2:{"sabor":"toscana","valor": 43.99},
    3:{"sabor":"marguerita","valor": 53.99},
    4:{"sabor":"quatro queijos","valor":59.99},
}
while True:
    print("cardapio do dia")
    print("1 sabor calabresa valor--52.99")
    print("2 sabor toscana valor--43.99")
    print("3 sabor marguerita valor--53.99")
    print("4 sabor quatro queijos--59.99")

    escolha=input("o que você deseja")
    if escolha=="1" or escolha=="2" or escolha=="3" or escolha=="4":
        escolha=int(escolha)
        pizza=cardapio[escolha]

    else:
        print("opção invalida, tente novamente") 
        continue

    continuar=input("deseja continuar? Digete sim/finalizar").lower()
    if continuar =="sim":
        continue
    else:
        print("--Comprovante da compra:--")
    print(nome)
    print(número)
    print(email)
    from datetime import date
    dataAtual=date.today()
    print(dataAtual)
    valor=cardapio[escolha]
    break