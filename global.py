saldo = int( input("digete o saldo bancário"))
saque = int( input("digete o valor do saque"))

if saldo>= saque:
    saldo = saldo - saque
    print("você realizou um saque com sucesso" "seu saldo é", saldo)
else:
    print("você não possui saldo suficiente para realizar essa operação")

