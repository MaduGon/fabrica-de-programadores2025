def soma_dos_quadrados(area):
    soma =quadrado(area) + quadrado(area)
    return soma

def quadrado():
    lado = int(input("digete o valor do lado: "))
    area = lado**2 # lado * lado
    print(area)
#quadrado()

#ex:2
def porcentagem():
    salario=float(input("qual o salario")) 
    aumento = 15
    print(salario + (salario * aumento / 100))
#porcentagem()

#ex:3
def base_e_altura_triangulo():
    base= int(input("qual é a base do triangulo?"))
    altura=int(input("qual é a altura do triangulo"))
    calculo= (base*altura)/3
    print("area do triangulo:", calculo),
#base_e_altura_triangulo()

#ex:4
def temperatura():
    celsius=int(input("qual a temperatura em graus celsius"))
    calculo=(9*celsius + 160)/5
    print("valor da temperatura em fahrenheit", calculo),
#temperatura()


#ex6
def valores():
    x=int(input("digete o valor de x:"))
    y=int(input("digete o valor de y:"))
    z = x
    x = y
    y = z
    print("efetue a troca x, y = y, x", x , y)
valores()


#ex7
def paralelepipedo():
    altura=int(input("defina o valor da altura do paralelepipedo"))
    comprimento=int(input("defina o valor do comprimento do paralelepipedo"))
    largura=int(input("defina  o valor da largura do paralelepipedo"))
    volume=(altura*comprimento*largura)
    print("qual o volume do paralelepipedo", volume),
#paralelepipedo()


 